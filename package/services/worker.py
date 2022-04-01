from queue import Queue
from urllib import request
from threading import Thread
from typing import List
from http.client import HTTPResponse

class HttpGetWorker(Thread):
    def __init__(self, queue: Queue):
        super().__init__()
        super().start()
        self.queue = queue
        self.responses = []
        self.work()

    def work(self):
        while True:
            url = self.queue.get()
            if not url:
                break
            response = request.urlopen(url)
            self.responses.append(response)
            self.queue.task_done()

def request_urls(urls: List[str], n_workers: int=20) -> List[HTTPResponse]:
    """
    Purpose: Run concurrent http requests against the given URLs
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
