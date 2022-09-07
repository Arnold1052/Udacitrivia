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

    def test_get_paginated_question(self):
        res = self.client().get("/categories")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["categories"])


    def test_get_question_search_with_results(self):
        res = self.client().post("/questions_search", json={"searchTerm": "the"})
        data = json.loads(res.data)
       

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["total_questions"],10)
        self.assertEqual(len(data["questions"]), 10)

    
    def test_get_question_search_with_results(self):
        res = self.client().post("/questions_search", json={"searchTerm": "morty"})
        data = json.loads(res.data)
       

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["total_questions"],0)
        self.assertEqual(len(data["questions"]), 0)

    def test_422_if_question_does_not_exist(self):
        res = self.client().delete("/books/18")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")



   
        


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()