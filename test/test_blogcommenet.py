import unittest 
from app.models import Blog,User,BlogComments
from app import db


class TestPitch(unittest.TestCase):

    def setUp(self):
        self.new_blog=Blog(blog_content="pitch one",blog_category='Academics')
        self.new_blogcomment=BlogComments(comment_content="one comment",blog=self.new_pitch)

    def tearDown(self):
        db.session.delete(self) 
        User.query.commit() 

    def test_instance(self):
        self.assertTrue(isinstance(self.new_blogcomment,Comment)) 

    def test_check_instance_variables(self):
        self.assertTrue(self.new_blogcomment.comment_content,"One comment") 
        self.assertEqual(self.new_blogcomment.blog,self.new_pitch, 'blog one') 