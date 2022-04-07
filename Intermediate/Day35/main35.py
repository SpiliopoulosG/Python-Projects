from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface
import requests

question_bank = []

parameters = {
    "amount": 20,
    "type": "boolean"
}

response = requests.get("https://opentdb.com/api.php", parameters)
response.raise_for_status()
question_data = response.json()
question_data = question_data["results"]

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)


# while quiz.still_has_questions():
#     quiz.next_question()

