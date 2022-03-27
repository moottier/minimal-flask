import unittest, json
from app.services import services
from typing import List

class MockPost:
    """
    Mock for the post returnd by the API
    """
    def __init__(self, id: int, author: str, author_id: int, likes: int, popularity: float, reads: int, tags: List[str]):
        self.id = id
        self.author = author
        self.author_id = author_id
        self.likes = likes
        self.popularity = popularity
        self.reads = reads
        self.tags = tags

    def __getitem__(self, key):
        return self.to_dict()[key]

    def to_dict(self):
        return {
            'id': self.id,
            'author': self.author,
            'authorId': self.author_id,
            'likes': self.likes,
            'popularity': self.popularity,
            'reads': self.reads,
            'tags': self.tags,
        }

class MockHttpResponse:
    """
    Mock for the HTTPResponse sent by the API
    """
    def __init__(self, post_collection: List[MockPost]):
        self.post_collection = post_collection
    
    def read(self) -> bytes:
        return self

    def decode(self, encoding) -> str:
        d = {'posts': [post.to_dict() for post in self.post_collection]}
        return json.dumps(d)
    
class TestGetPosts(unittest.TestCase):
    def test_gets_n_tags(self):
        tags = [
            'tech',
            'bees',
            'cheese',
            'tony%20montana',
        ] 
        responses = services.request_posts(tags)
        for response in responses:
            with self.subTest(response=response):
                self.assertEqual(response.status, 200)

        self.assertEqual(len(tags), len(responses))
        

    def test_service_1_doesnt_do_this(self):
        return True

class TestParseTags(unittest.TestCase):
    def test_parse_tags_encodes_tags(self):
        expected = ['tech%20']
        self.assertEqual(
            services.parse_tags('tech '), 
            expected
        )

    def test_parse_tags_removes_blank_tags(self):
        expected = []
        self.assertEqual(
            services.parse_tags(',,,'),
            expected
        )

    def test_parse_tags_gets_all_tags(self):
        expected = ['ham', 'eggs', 'cheese']
        self.assertEqual(
            sorted(services.parse_tags('ham,eggs,cheese')),
            sorted(expected)
        )

class TestGetUrl(unittest.TestCase):
    def test_get_url_accepts_empty_args(self):
        expected = 'https://api.hatchways.io/assessment/blog/posts?tag='
        self.assertEqual(
            services.get_url(tag=''),
            expected
        )

    def test_get_url_accepts_all_args(self):
        expected = 'https://api.hatchways.io/assessment/blog/posts?tag=ham'
        self.assertEqual(
            services.get_url(tag='ham'),
            expected
        )
    pass

class TestGenerateUniquePostsResponses(unittest.TestCase):
    def test_generator_eliminates_duplicates(self):
        mock_post_1 = MockPost(id=1, author='Franz Ferdinand', author_id=123, likes=120, popularity=1.23, reads=12314, tags=['Europe'])
        mock_post_2 = MockPost(id=2, author='Franz Kafka', author_id=321, likes=20, popularity=103, reads=4114, tags=['Cockroaches'])
        post_collection = [
            mock_post_1,
            mock_post_2,
            mock_post_2,
        ]
        http_responses = [
            MockHttpResponse(post_collection),
            MockHttpResponse(post_collection)
        ]

        expected = [mock_post_1.to_dict(), mock_post_2.to_dict()]
        actual = []
        for post in services.generate_unique_posts_from_responses(http_responses):
            actual.append(post)

        self.assertEqual(
            actual,expected
        )

    def test_generator_accepts_empty_input(self):
        expected = []
        actual = []
        for post in services.generate_unique_posts_from_responses([]):
            actual.append(post)
            
        self.assertEqual(
            len(actual),
            len(expected)
        )

class TestGetSortedPosts(unittest.TestCase):
    def setUp(self):
        self.post_1 = MockPost(id=3, author='Franz Ferdinand', author_id=123, likes=99, popularity=300, reads=0, tags=['Europe'])
        self.post_2 = MockPost(id=1, author='Franz Ferdinand', author_id=123, likes=120, popularity=200, reads=900, tags=['Europe'])
        self.post_3 = MockPost(id=2, author='Franz Ferdinand', author_id=123, likes=123, popularity=100, reads=10000, tags=['Europe'])
        self.posts = [self.post_1, self.post_2, self.post_3]
    def test_sort_by_id_with_default_direction(self):
        expected = [self.post_2, self.post_3, self.post_1]
        actual = services.get_sorted_posts(self.posts, sort_by='id')
        self.assertEqual(expected, actual)

    def test_sort_by_id_reverse_default_sort_by(self):
        expected = [self.post_1, self.post_3, self.post_2]
        actual = services.get_sorted_posts(self.posts, direction='desc')
        self.assertEqual(expected, actual)

    def test_sort_by_reads(self):
        expected = [self.post_1, self.post_2, self.post_3]
        actual = services.get_sorted_posts(self.posts, sort_by='reads', direction='asc')
        self.assertEqual(expected, actual)

    def test_sort_by_reads_reverse(self):
        expected = [self.post_3, self.post_2, self.post_1]
        actual = services.get_sorted_posts(self.posts, sort_by='reads', direction='desc')
        self.assertEqual(expected, actual)

    def test_sort_by_likes(self):
        expected = [self.post_1, self.post_2, self.post_3]
        actual = services.get_sorted_posts(self.posts, sort_by='likes', direction='asc')
        self.assertEqual(expected, actual)

    def test_sort_by_likes_reverse(self):
        expected = [self.post_3, self.post_2, self.post_1]
        actual = services.get_sorted_posts(self.posts, sort_by='likes', direction='desc')
        self.assertEqual(expected, actual)

    def test_sort_by_popularity(self):
        expected = [self.post_3, self.post_2, self.post_1]
        actual = services.get_sorted_posts(self.posts, sort_by='popularity', direction='asc')
        self.assertEqual(expected, actual)

    def test_sort_by_likes_popularity(self):
        expected = [self.post_1, self.post_2, self.post_3]
        actual = services.get_sorted_posts(self.posts, sort_by='popularity', direction='desc')
        self.assertEqual(expected, actual)