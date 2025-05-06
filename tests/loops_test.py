import pytest
from src.loops import multiplication_table

def test_multiplication_table():
  actual_output = multiplication_table(5)
  assert(actual_output[0]) == "5 * 1 = 5"
  assert(actual_output.__len__()) == 10