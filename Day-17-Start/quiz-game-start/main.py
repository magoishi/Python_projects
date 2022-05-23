from data import question_data
from question_model import Question
from quiz_brain import QuizzBrain

question_bank = []

for q in question_data:
    ques = Question(q["question"], q["correct_answer"])
    question_bank.append(ques)

quiz = QuizzBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quizz!")
print(f"You final score was: {quiz.score}/{quiz.question_number}")