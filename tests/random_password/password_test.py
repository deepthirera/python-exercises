from src.random_password.password import Password, Rule

class TestPassword:
  def test_multiple_rules_uppercase_length(self):
    valid_password_text = "ARandomPassword"
    invalid_password_text1 = "lowercase_password"
    invalid_password_text2 = "Short"
    password = Password(valid_password_text)
    password.rules.extend([Rule(Rule.UPPERCASE), Rule(Rule.MIN_LENGTH, min_length=7)])
    assert(password.is_valid()) == True
    password.text = invalid_password_text1
    assert(password.is_valid()) == False
    password.text = invalid_password_text2
    assert(password.is_valid()) == False

  def test_rules_uppercase(self):
    rule = Rule(Rule.UPPERCASE)
    assert(rule.is_valid("APassword")) == True
    assert(rule.is_valid("apassword")) == False

  def test_rules_digit(self):
      rule = Rule(Rule.DIGIT)
      assert(rule.is_valid("1Password")) == True
      assert(rule.is_valid("aPassword")) == False

  def test_rules_special_chars(self):
      rule = Rule(Rule.SPECIAL_CHARS)
      assert(rule.is_valid("p@ssword")) == True
      assert(rule.is_valid("a1Password")) == False

  def test_rules_length(self):
      rule = Rule(Rule.MIN_LENGTH, min_length=8)
      assert(rule.is_valid("p@ssword")) == True
      assert(rule.is_valid("p@sswords")) == True
      assert(rule.is_valid("a1Pa!")) == False
