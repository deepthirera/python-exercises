import random
import string
from src.random_password.password import Password, Rule
from typing import List

def generate_password(required_length=8, have_uppercase=False, have_digit=False, have_special_chars=False):
  lower_charset = string.ascii_lowercase
  upper_charset = string.ascii_uppercase
  digit_charset = string.digits
  special_charset = string.punctuation
  required_length = required_length if required_length >= 8 else 8
  all_chars = lower_charset
  chosen_chars = []
  password_rules: List[Rule] = [Rule(Rule.MIN_LENGTH, min_length=required_length)]
  if have_uppercase:
    password_rules.append(Rule(Rule.UPPERCASE))
    chosen_chars.append(random.choice(upper_charset))
    all_chars += upper_charset
  if have_digit:
    password_rules.append(Rule(Rule.DIGIT))
    chosen_chars.append(random.choice(digit_charset))
    all_chars += digit_charset
  if have_special_chars:
    password_rules.append(Rule(Rule.SPECIAL_CHARS))
    chosen_chars.append(random.choice(special_charset))
    all_chars += special_charset
  remaining_num_of_req_chars = required_length - len(chosen_chars)
  chosen_chars.extend(random.choices(all_chars, k=remaining_num_of_req_chars))
  random.shuffle(chosen_chars)
  password = Password("".join(chosen_chars))
  password.rules = password_rules
  if password.is_valid():
    return password.text
  else:
    return "Password is invalid"

print(generate_password(8, True, True, True))
print(generate_password(18, False, True, True))