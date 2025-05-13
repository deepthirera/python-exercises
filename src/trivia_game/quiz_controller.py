from src.trivia_game.question import Question
from src.trivia_game.quiz import Quiz

questions_catalogue = {
  "What is 1+1": "2",
  "What is the capital of India": "Delhi",
  "How many colours are in the rainbow": "7",
  "What is the national animal of India": "tiger"
}

questions = []
for question, answer in questions_catalogue.items():
  questions.append(Question(question_text=question, answer=answer))

quiz = Quiz(questions=questions)
quiz.start()
while not quiz.is_complete():
  question = quiz.get_question()
  print(question.question_text)
  user_answer = input("Your Answer: ")
  quiz.check_answer(question, user_answer)

print("Thank you for completing the quiz.\n Your score is ", quiz.score)
