import os
import unittest
 
from app import app, db
from movieView import MovieView
 
 
TEST_DB = 'test.db'
 
 
class BasicTests(unittest.TestCase):
 
    ############################
    #### setup and teardown ####
    ############################
 
    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///' + \
        #     os.path.join(app.config['BASEDIR'], TEST_DB)
        self.app = app.test_client()
        db.drop_all()
        db.create_all()
 
    # executed after each test
    def tearDown(self):
        pass
 
 
###############
#### tests ####
###############
 
    def test_data_by_actorJD(self):
        results=MovieView.data_by_actor('Johnny Depp')
        self.assertTrue(len(results)>0)

    def test_data_by_actorJB(self):
        results=MovieView.data_by_actor('Joe Blackwell')
        self.assertEqual(len(results), 0)

    def test_top_ten_genres(self):
        results=MovieView.top_ten_genres()
        self.assertEqual(len(results), 10)
 
    def test_top_ten_actors(self):
        results=MovieView.top_ten_actors()
        self.assertEqual(len(results), 10)
 
if __name__ == "__main__":
    unittest.main()