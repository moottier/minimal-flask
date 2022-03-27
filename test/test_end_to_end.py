import unittest
from app.app import create_app

class TestAppPing(unittest.TestCase):
    def setUp(self):
        self.app = create_app('TestApp', 'TEST')
        self.client = self.app.test_client()

    def test_ping_responds_status_200(self):
        resp = self.client.get('/api/ping')
        self.assertEqual(resp.status_code, 200)

    def test_ping_responds_content_status_success(self):
        resp = self.client.get('/api/ping')
        self.assertEqual(
            resp.get_json(), 
            {'success': True}
        )

    def test_ping_responds_405_put(self):
        resp = self.client.put('/api/ping')
        self.assertEqual(resp.status_code, 405)

    def test_ping_responds_405_post(self):
        resp = self.client.post('/api/ping')
        self.assertEqual(resp.status_code, 405)

class TestAppGetPosts(unittest.TestCase):
    def setUp(self):
        self.app = create_app('TestApp', 'TEST')
        self.client = self.app.test_client()

    def test_get_posts_gets_posts_for_single_tag(self):
        resp = self.client.get('/api/posts?tags=tech')
        self.assertEqual(resp.status_code, 200)


    def test_get_posts_without_tag_responds_error(self):
        cases = [
            '/api/posts?tag=',
            '/api/posts?tag=&sortBy=id',
            '/api/posts?tag',
            '/api/posts?',
            '/api/posts',
        ]
        for case in cases:
            with self.subTest(case=case):
                resp = self.client.get(case)
                self.assertEqual(
                    resp.get_json(),
                    {'error': 'Tags parameter is required'}
                    )
                self.assertEqual(resp.status_code, 400)

    def test_get_posts_with_invalid_sortby_responds_error(self):
        cases = [
            '/api/posts?tags=tech&sortBy=favorites',
            '/api/posts?tags=tech&sortBy=ID'
        ]
        for case in cases:
            with self.subTest(case=case):
                resp = self.client.get(case)
                self.assertEqual(
                    resp.get_json(),
                    {'error': 'sortBy parameter is invalid'}
                    )
                self.assertEqual(resp.status_code, 400)

    def test_get_posts_with_invalid_direction_responds_error(self):
        cases = [
            '/api/posts?tags=tech&direction=dsc',
            '/api/posts?tags=tech&direction=DESC',
        ]
        for case in cases:
            with self.subTest(case=case):
                resp = self.client.get(case)
                self.assertEqual(
                    resp.get_json(),
                    {'error': 'direction parameter is invalid'}
                    )
                self.assertEqual(resp.status_code, 400)
