import os
import re
from unittest import result
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


def paginate_questions(request, selection):
    page = request.args.get("page", 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    questions = [question.format() for question in selection]
    current_questions = questions[start:end]

    return current_questions

def paginate_categories(request, selection):
    page = request.args.get("page", 1, type=int)
    start = page - 1
    end = start + len(Category.query.all())

    category = [categoryz.format() for categoryz in selection]
    current_categories = category[start:end]

    return current_categories


    

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

   
    
   

    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS"
        )
        return response

   
    @app.route("/categories")
    def retrieve_categories():

        page = request.args.get('page', 1, type=int)
        start = (page - 1) * 10
        end = start + 10

        selection = Category.query.order_by(Category.id).all()
        #current_categories = paginate_categories(request, selection)
        result = [rezult.format() for rezult in selection]
       



        if len(result ) == 0:
            abort(404)
      
        
        return jsonify(
            {
                "success": True,
                "categories": result[start:end],
                
            }
        )




    """
   
    This endpoint should return a list of questions,
    number of total questions, current category, categories.

    TEST: At this point, when you start the application
    you should see questions and categories generated,
    ten questions per page and pagination at the bottom of the screen for three pages.
    Clicking on the page numbers should update the questions.
    """
   









    @app.route("/questions")
    def retrieve_questions():

        page = request.args.get('page', 1, type=int)
        start = (page - 1) * 10
        end = start + 10

        selection = Question.query.order_by(Question.id).all()
        result = [rezult.format() for rezult in selection]

        #current_questions = paginate_questions(request, selection)

        if len(result) == 0:
            abort(404)

        return jsonify(
            {
                "success": True,
                "questions": result[start:end],
                "total_questions": len(result),
            }
        )

    








    """
 
    @TODO:
    TEST: When you click the trash icon next to a question, the question will be removed.
    This removal will persist in the database and when you refresh the page.
    """

    @app.route("/questions/<int:id>", methods=["DELETE"])
    def delete_question(id):
        try:
            question_data = Question.query.filter(Question.id == id).one_or_none()

            if question_data is None:

                abort(404)

            question_data.delete()
            selection = Question.query.order_by(Question.id).all()
            current_question = paginate_questions(request, selection)

            return jsonify(
                {
                    "success": True,
                    "deleted": id,
                    "question": current_question,
                    "total_questions": len(Question.query.all()),
                }
            )

        except:
            abort(422)

    

    
    
















    """
    @TODO:
   

    TEST: When you submit a question on the "Add" tab,
    the form will clear and the question will appear at the end of the last page
    of the questions list in the "List" tab.
    """
    @app.route("/questions_post", methods=["POST"])
    def create_questions():
        body = request.get_json()

        new_question = body.get("question", None)
        new_answer = body.get("answer", None)
        new_category = body.get("category", None)
        new_difficulty = body.get("difficulty", None)

        try:
            Questionz = Question(question=new_question, answer=new_answer, category=new_category,difficulty=new_difficulty)
            Questionz.insert()

            selection = Question.query.order_by(Question.id).all()
            current_questions = paginate_questions(request, selection)

            return jsonify(
                {
                    "success": True,
                    "created": Questionz.id,
                    "question": current_questions,
                    "total_questions": len(Question.query.all()),
                    
                }
            )

        except:
            abort(422)













    """
    @TODO:
    Create a POST endpoint to get questions based on a search term.
    It should return any questions for whom the search term
    is a substring of the question.

    TEST: Search by any phrase. The questions list will update to include
    only question that include that string within their question.
    Try using the word "title" to start.
    """

    @app.route("/questions_search", methods=["POST"])
    def create_questionz():
        body = request.get_json()

        
        search = body.get("searchTerm", None)

        try:
            
                
            selection = Question.query.order_by(Question.id).filter(
            Question.question.ilike("%{}%".format(search))
            )
            current_questions = paginate_questions(request, selection)
            result = []
            for item in current_questions:
                result.append(item)
            return jsonify(

                {

                    "success": True,
                    "questions": result,
                    "total_questions": len(result),
                    }
                )
        except:

            abort(422)














    """
    @TODO:
    

    TEST: In the "List" tab / main screen, clicking on one of the
    categories in the left column will cause only questions of that
    category to be shown.
    """

    @app.route("/question/<id>")
    def retrieve_category(id):
        try:
            
            question_data = Question.query.filter(Question.category == id).all()

            if question_data is None:

                abort(404)

            
            selection = question_data
            
            categorical_question = paginate_questions(request, selection)
            result = []
            for item in categorical_question:
                result.append(item)


            return jsonify(
                {
                    "success": True,
                    "questions": result,
                    "total_questions": len(result),
                }
            )

        except:
            abort(422)













    """
    @TODO:
    Create a POST endpoint to get questions to play the quiz.
    This endpoint should take category and previous question parameters
    and return a random questions within the given category,
    if provided, and that is not one of the previous questions.

    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not.
    """
    @app.route("/quizzes", methods=["POST"])
    def create_quizzes():
        body = request.get_json()

        
        quiz_category = body.get("quiz_category", None)

        try:
            
                
            selection = Question.query.order_by(Question.id).filter(
            Question.category.ilike("%{}%".format(quiz_category))
            )
            current_questions = paginate_questions(request, selection)
            result = []
            previousQuestions= []
            
            random_quiz = []
            for item in current_questions:
                result.append(item)
                
                random_quiz.append(random.choice(result))
            rand_idx = random.randint(0, len(random_quiz)-1)
            random_num = random_quiz[rand_idx]

                


            return jsonify(

                {

                    "success": True,
                    "question": random_num,
                    
                    }
                )
        except:

            abort(422)

    





















    """
    @TODO:
    Create error handlers for all expected errors
    including 404 and 422.
    """


    @app.errorhandler(400)
    def not_found(error):
        return (
            jsonify({"success": False, "error": 400, "message": "bad request"}),
            400,
        )
    @app.errorhandler(404)
    def not_found(error):
        return (
            jsonify({"success": False, "error": 404, "message": "resource not found"}),
            404,
        )

    @app.errorhandler(422)
    def unprocessable(error):
        return (
            jsonify({"success": False, "error": 422, "message": "unprocessable"}),
            422,
        )

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True) 

