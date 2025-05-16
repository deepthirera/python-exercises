import string
from typing import List

class Rule:
  UPPERCASE = lambda text: Rule.text_has_char_from(text, string.ascii_uppercase)
  MIN_LENGTH = lambda text, min_length: len(text) >= min_length
  DIGIT = lambda text: Rule.text_has_char_from(text, string.digits)
  SPECIAL_CHARS = lambda text: Rule.text_has_char_from(text, string.punctuation)

  def text_has_char_from(text, charset):
    for single_char in charset:
      if single_char in text:
        return True
    return False

  def __init__(self, rule_type, **kwargs):
    self.rule_type = rule_type
    if kwargs.get("min_length"):
      self.min_length = kwargs.get("min_length")

  def is_valid(self, text):
    if self.rule_type == Rule.MIN_LENGTH:
      return self.rule_type(text, self.min_length)
    return self.rule_type(text)
  
class Password:
  def __init__(self, text):
    self.text = text
    self.rules: List[Rule] = []
    self.errors = []

  def is_valid(self):
    for rule in self.rules:
      if not rule.is_valid(self.text):
        return False
    return True

