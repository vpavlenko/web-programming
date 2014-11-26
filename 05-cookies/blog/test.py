import os
import blog
import data
import unittest
import tempfile
from flask import url_for


INIT_DATA = "[{'title': 'TITLE1', 'abstract': 'ABSTRACT1', 'content': 'CONTENT1'}]"


class BlogTestCase(unittest.TestCase):
    def setUp(self):
        # raise Exception(data)
        self.tempfile_fd, self.tempfile_filename = tempfile.mkstemp()
        with open(self.tempfile_filename, 'w') as data_file:
            data_file.write(INIT_DATA)
        data.init_with_file(self.tempfile_filename)
        self.app = blog.app.test_client()
        self.ctx = blog.app.test_request_context()
        self.ctx.push()

    def tearDown(self):
        os.close(self.tempfile_fd)
        os.unlink(self.tempfile_filename)
        self.ctx.pop()

    def test_blog_shows_title_and_abstract_for_post_from_init_data(self):
        response = self.app.get('/')
        response_data = response.data.decode('utf-8')
        assert 'TITLE1' in response_data
        assert 'ABSTRACT1' in response_data
        assert 'CONTENT1' not in response_data

    def test_blog_shows_all_post_fields_on_field_view(self):
        response = self.app.get(url_for('post', post_id=1))
        response_data = response.data.decode('utf-8')
        assert 'TITLE1' in response_data
        assert 'ABSTRACT1' in response_data
        assert 'CONTENT1' in response_data


if __name__ == '__main__':
    unittest.main()
