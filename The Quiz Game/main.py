
from data import category_dict
from quiz_brain import QuizBrain
from opentdb_Questions import FetchQuestions


questions = FetchQuestions()
questions.get_Questions()

quiz = QuizBrain(questions.question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
