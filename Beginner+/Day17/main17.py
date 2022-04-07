from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question_number in range(len(question_data)):
    new_question = Question(question_data[question_number]['text'], question_data[question_number]['answer'])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f'Your final score was: {quiz.score}/{quiz.question_number}')

