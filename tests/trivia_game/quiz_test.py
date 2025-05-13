import pytest
from src.trivia_game.quiz import Quiz
from src.trivia_game.question import Question

class TestQuiz:
  questions = [
      Question("Question 1", "Ans 1"),
      Question("Question 2", "Ans 2"),
      Question("Question 3", "Ans 3"),
    ]
  
  def test_quiz_start(self):
    quiz = Quiz(questions=TestQuiz.questions)
    quiz.start()
    assert(quiz.score) == 0
    assert(quiz.current_question_index) == 0

  def test_quiz_get_question(self):
    quiz = Quiz(questions=TestQuiz.questions)
    quiz.start()
    next_question = quiz.get_question()
    assert(next_question.question_text) == "Question 1"
    assert(quiz.current_question_index) == 1

  def test_quiz_get_question_should_return_none_if_no_more_questions(self):
    quiz = Quiz(questions=TestQuiz.questions)
    quiz.current_question_index = 2
    quiz.get_question()
    assert(quiz.current_question_index) == 3
    assert(quiz.get_question()) == None

  def test_is_complete_return_true_if_complete(self):
    quiz = Quiz(questions=TestQuiz.questions)
    quiz.current_question_index = 3
    assert(quiz.is_complete()) == True
    quiz.current_question_index = 4
    assert(quiz.is_complete()) == True

  def test_is_complete_return_false_if_not_complete(self):
    quiz = Quiz(questions=TestQuiz.questions)
    quiz.current_question_index = 1
    assert(quiz.is_complete()) == False