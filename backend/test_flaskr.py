import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        #self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        #setup_db(self.app, self.database_path)
        self.database_path = "postgresql://{}:{}@{}/{}".format(
            "postgres", "engineerarnoldmr", "localhost:5432", self.database_name
        )
        setup_db(self.app, self.database_path)
        self.new_question = {"question": "In which MCU movie did Iron man die?", "answer": "End Game", "category": 4,"difficulty": 5}



        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    def test_get_paginated_category(self):
        res = self.client().get("/categories")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["categories"])

    

    def Failed_test_get_paginated_category(self):
        res = self.client().get("/categories?page=1000")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertTrue(data["categories"])


    def test_get_paginated_que(self):
        res = self.client().get("/questions")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["questions"])

    

    def Failed_test_get_paginated_que(self):
        res = self.client().get("/questions?page=1000")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertTrue(data["questions"])




    def test_get_question_search_with_results(self):
        res = self.client().post("/questions_search", json={"searchTerm": "the"})
        data = json.loads(res.data)
       

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["total_questions"],8)
        self.assertEqual(len(data["questions"]), 8)

    
    def failed_test_get_question_search_with_results(self):
        res = self.client().post("/questions_search", json={"searchTerm": "morty"})
        data = json.loads(res.data)
       

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["total_questions"],0)
        self.assertEqual(len(data["questions"]), 0)

    def test_422_if_question_does_not_exist(self):
        res = self.client().delete("/questions/118")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")
    

    
    def test_delete_question(self):
        res = self.client().delete("/questions/52")
        data = json.loads(res.data)

        question = Question.query.filter(Question.id == 52).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["deleted"], 52)
        self.assertTrue(data["total_questions"])
        #self.assertTrue(len(data["books"]))
        self.assertEqual(question, None)

    

    def test_create_new_question(self):
        res = self.client().post("/questions_post", json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["created"])
       

    def test_405_if_question_creation_not_found(self):
        res = self.client().post("/questions_post/45", json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")


    def retrieve_by_category_id(self):
        res = self.client().get("/question/3")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["total_questions"])

    
    def failed_retrieve_by_category_id(self):
        res = self.client().get("/question/135")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertTrue(data["total_questions"])


    def generate_random_question(self):
        res = self.client().post("/quizzes", json={"quiz_category": "2"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["total_questions"])

    
    def failed_to_generate_random_question(self):
        res = self.client().post("/quizzes", json={"quiz_category": "11"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertTrue(data["total_questions"])


    
        

  
        



   
        


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
