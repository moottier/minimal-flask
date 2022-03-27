import json
from typing import List, Generator
from urllib import parse
from http.client import HTTPResponse
from queue import Queue

from app.services.worker import HttpGetWorker

def parse_tags(tags: str) -> List[str]:
    """
    Purpose: separate & encode tags in comma separated string
    Input:   Comma separate string             E.g. 'toast,cheese,milk ,cheese'
    Output:  List with unique encodedtags      E.g. ['toast', 'cheese', 'milk%20']
    """
    tags = tags.split(',')
    tags = (parse.quote(tag) for tag in tags)
    tags = filter(lambda tag: tag != '', tags)
    return list(set(tags))

def get_url(tag: str) -> str:
    """
    Purpose: Return hatchways API url for given tag
    Input:   Str defining a tag, Str defining a sort key, Str defining a sort direction
    Output:  Url requesting posts for that tag
    """
    return f'https://api.hatchways.io/assessment/blog/posts?tag={tag}'

def process_request(tags: List[str], sort_by: str, direction: str) -> dict:
    """
    Purpose: Driver routine that processes a request for a set of posts for a tag
    Input:   Tags, sort key, sort direction
    Output:  Ordered dictionary of unique of posts with the given tag 
    """
    responses = request_posts(tags)
    posts = []
    for post in generate_unique_posts_from_responses(responses):
        posts.append(post)
    posts = get_sorted_posts(posts, sort_by, direction)
    return {'posts': posts}

def request_posts(tags: List[str], n_workers: int=20) -> List[HTTPResponse]:
    """
    Purpose: Run concurrent http requests against the hatchways API for the given tags
    Input:   
             A list of tags
             An option number of workers (default=20)
    Output:  A list of HttpResponses
    """
    def create_queue(urls, n_workers) -> Queue:
        queue = Queue()
        
        for url in urls:
            queue.put(url)
        
        for _ in range(n_workers):
            queue.put(None)
        
        return queue

    urls = [get_url(tag) for tag in tags]
    queue = create_queue(urls, n_workers)

    workers = []
    for worker in range(n_workers):
        worker = HttpGetWorker(queue)
        worker.join()
        workers.append(worker)

    responses = []
    for worker in workers:
        responses.extend(worker.responses)

    return responses

def generate_unique_posts_from_responses(responses: List[HTTPResponse]) -> Generator[dict, None, None]:
    """
    Purpose: Eliminate duplicate posts from the API response
    Input:   List of HTTPResponse objects
    Output:  Generator yields unique posts as a dictionary
    """
    already_seen = set()
    
    for response in responses:
        response = response.read().decode('utf-8')
        response = json.loads(response)
        posts = response['posts']
        
        for post in posts:
            post_id = post['id']
            
            if post_id in already_seen:
                continue
            already_seen.add(post_id)
            yield post

def get_sorted_posts(posts: List[dict], sort_by: str='id', direction: str='asc') -> List[dict]:
    """
    Purpose: Sort posts by the given sort_by key
    Input:   List of dictionaries, key [id, reads, likes, popularity], reverse [True, False]
    Output:  A list sorted in ascending or descending order by selected key
    """
    reverse = (direction == 'desc')
    key = lambda post: post[sort_by]
    return sorted(posts, key=key, reverse=reverse)

def validate_sort_by(sort_by: str) -> bool:
    """
    Purpose: Validate the sortBy query parameter
    """
    valid = [
        'id',
        'reads',
        'likes',
        'popularity'
    ]
    return sort_by in valid

def validate_direction(direction: str) -> bool:
    """
    Purpose: Validate the direction query parameter
    """
    valid = ['asc', 'desc']
    return direction in valid