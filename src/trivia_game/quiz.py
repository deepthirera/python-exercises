from src.trivia_game.question import Question

class Quiz:
  def __init__(self, questions: list[Question]):
    self.questions = questions
    
  def start(self):
    self.score = 0
    self.current_question_index = 0

  def is_complete(self):
    return self.current_question_index >= len(self.questions)

  def get_question(self):  
    question = self.questions[self.current_question_index] if (not self.is_complete()) else None
    self.current_question_index += 1
    return question

  def check_answer(self, question, user_answer):
    if user_answer == question.answer.strip().lower():
      self.score += 1