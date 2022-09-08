
# Udacitrivia Project

This project is a trivia game that contains questions and answers. Users can add to the question list and with the frontend they can also confirm their answers by toggling the show answer button.





# Getting Started
### Pre-requisites and Local Development
Developers using this project should already have Python3, pip and node installed on their local machines.

### Backend
From the backend folder run pip install requirements.txt. All required packages are included in the requirements file.

To run the application run the following commands:
```
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```
These commands put the application in development and directs our application to use the __init__.py file in our flaskr folder. Working in development mode shows an interactive debugger in the console and restarts the server whenever changes are made. If running locally on Windows, look for the commands in the Flask documentation.
```
The application is run on http://127.0.0.1:5000/ by default and is a proxy in the frontend configuration.
```
### Frontend
From the frontend folder, run the following commands to start the client:
```
npm install // only once to install dependencies
npm start 
```
By default, the frontend will run on localhost:3000.

### Tests
In order to run tests navigate to the backend folder and run the following commands:

```
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
All tests are kept in that file and should be maintained as updates are made to app functionality.

### API Reference
Getting Started
Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, 
```
http://127.0.0.1:5000/
```
which is set as a proxy in the frontend configuration.
Authentication: This version of the application does not require authentication or API keys.
### Error Handling
Errors are returned as JSON objects in the following format:
```
{
    "success": False, 
    "error": 422,
    "message": "unprocessable"
}
```
The API will return three error types when requests fail:
```
400: Bad Request
404: Resource Not Found
422: UnProcessable
```
### Endpoints
```
GET /questions
```
General:
Returns a list of questions objects, success value, and total number of questions
Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1.
Sample: 
```
curl http://127.0.0.1:5000/questions?page=1
```
```
  {
  "questions": [
    {
      "answer": "Apollo 13",
      "category": "5",
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": "5",
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Maya Angelou",
      "category": "4",
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": "5",
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": "4",
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Brazil",
      "category": "6",
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Lake Victoria",
      "category": "3",
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "Agra",
      "category": "3",
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    },
    {
      "answer": "Escher",
      "category": "2",
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    },
    {
      "answer": "Mona Lisa",
      "category": "2",
      "difficulty": 3,
      "id": 17,
      "question": "La Giaconda is better known as what?"
    }
  ],
  "success": true,
  "total_questions": 19
}
```
```
POST /questions_post
```
General:
Creates a new question using the submitted question, answer, category and difficulty. Returns the id of the created question, success value, total question, and question list.
```
curl http://127.0.0.1:5000/questions_post -X POST -H "Content-Type: application/json" -d '{"question":"Who is the founder of Google?", "answer":"Larry Page", "category":"3","difficulty":"5"}'
```

For Window Pc use:
```
curl -X POST -H "Content-Type:application/json" -d "{\"question\":\"Who is the founder of Google?\", \"answer\":\"Larry Page\", \"category\":\"3\",\"difficulty\":\"5\"}" http://127.0.0.1:5000/questions_post 
```
```
{
  "created": 31,
  "question": [
    {
      "answer": "Apollo 13",
      "category": "5",
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": "5",
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Maya Angelou",
      "category": "4",
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": "5",
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": "4",
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Brazil",
      "category": "6",
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Lake Victoria",
      "category": "3",
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "Agra",
      "category": "3",
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    },
    {
      "answer": "Escher",
      "category": "2",
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    },
    {
      "answer": "Mona Lisa",
      "category": "2",
      "difficulty": 3,
      "id": 17,
      "question": "La Giaconda is better known as what?"
    }
  ],
  "success": true,
  "total_questions": 23
}
```
DELETE
```
/questions/{id}
```
General:
Deletes the question of the given ID if it exists. Returns the id of the deleted question, success value, total questions, and question list based on current page number to update the frontend.
```
curl -X DELETE http://127.0.0.1:5000/questions/7 
```
```
{
  "deleted": 31,
  "question": [
    {
      "answer": "Apollo 13",
      "category": "5",
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": "5",
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Maya Angelou",
      "category": "4",
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": "5",
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": "4",
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Brazil",
      "category": "6",
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Lake Victoria",
      "category": "3",
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "Agra",
      "category": "3",
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    },
    {
      "answer": "Escher",
      "category": "2",
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    },
    {
      "answer": "Mona Lisa",
      "category": "2",
      "difficulty": 3,
      "id": 17,
      "question": "La Giaconda is better known as what?"
    }
  ],
  "success": true,
  "total_questions": 22
}
```
SEARCH
```
/questions_search
```
### General:
This aids in query of a question based on a keyword.Returns the success value, total questions and questions list.
```
curl -X POST -H "Content-Type:application/json" -d "{"searchTerm":"the"}" http://127.0.0.1:5000/questions_search
```
For Window Pc
```
curl -X POST -H "Content-Type:application/json" -d "{\"searchTerm\":\"the\"}" http://127.0.0.1:5000/questions_search
```
```
{
  "questions": [
    {
      "answer": "Tom Cruise",
      "category": "5",
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Maya Angelou",
      "category": "4",
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": "5",
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Brazil",
      "category": "6",
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Lake Victoria",
      "category": "3",
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "Agra",
      "category": "3",
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    },
    {
      "answer": "The Liver",
      "category": "1",
      "difficulty": 4,
      "id": 20,
      "question": "What is the heaviest organ in the human body?"
    },
    {
      "answer": "Blood",
      "category": "1",
      "difficulty": 4,
      "id": 22,
      "question": "Hematology is a branch of medicine involving the study of what?"
    },
    {
      "answer": "Scarab",
      "category": "4",
      "difficulty": 4,
      "id": 23,
      "question": "Which dung beetle was worshipped by the ancient Egyptians?"
    },
    {
      "answer": "Nikola Tesla",
      "category": "1",
      "difficulty": 5,
      "id": 24,
      "question": "Who invented the electric motor?"
    }
  ],
  "success": true,
  "total_questions": 10
}
```
GET
```
/categories
```
General:
Gets all categories available in the db.Returns the success value and categories list.
```
curl http://127.0.0.1:5000/categories
```
```
{
  "categories": [
    {
      "id": 1,
      "type": "Science"
    },
    {
      "id": 2,
      "type": "Art"
    },
    {
      "id": 3,
      "type": "Geography"
    },
    {
      "id": 4,
      "type": "History"
    },
    {
      "id": 5,
      "type": "Entertainment"
    },
    {
      "id": 6,
      "type": "Sports"
    }
  ],
  "success": true
}
```
GET 
```
/question/{id}
```
General:
Gets questions that have a particular category id.Returns the success value ,questions list and total questions that have that category id.
```
curl http://127.0.0.1:5000/question/5
```
```
{
  "questions": [
    {
      "answer": "Apollo 13",
      "category": "5",
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": "5",
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": "5",
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Arnold Kabare",
      "category": "5",
      "difficulty": 2,
      "id": 25,
      "question": "Who is Africa Richest Person?"
    }
  ],
  "success": true,
  "total_questions": 4
}

```

POST
```
/quizzes
```
General:
Posts the user selected category and generates random questions based on that category number.Returns the success value and current question.
```
curl -X POST -H "Content-Type:application/json" -d "{"quiz_category":"3"}" http://127.0.0.1:5000/quizzes
```

Windows pc
```
curl -X POST -H "Content-Type:application/json" -d "{\"quiz_category\":\"3\"}" http://127.0.0.1:5000/quizzes
```
```
{
  "question": {
    "answer": "Larry Page",
    "category": "3",
    "difficulty": 5,
    "id": 28,
    "question": "Who is the founder of Google?"
  },
  "success": true
}

```


### Authors
Yours truly, Arnold Kabare

### Acknowledgements
The awesome team at Udacity. 
