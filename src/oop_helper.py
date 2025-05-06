import random
from urllib.request import urlopen

WORD_URL = 'http://learncodethehardway.org/words.txt'
WORDS = []
PHRASES = {
"class %%%(%%%):":
"Make a class named %%% that is-a %%%.",
"class %%%(object):\n\tdef __init__(self, @@@)" :
"class %%% has-a __init__ that takes self and @@@ params.",
"class %%%(object):\n\tdef ***(self, @@@)":
"class %%% has-a function *** that takes self and @@@ params.",
"*** = %%%()":
"Set *** to an instance of class %%%.",
"%%%().***(@@@)":
"From instance of %%% get the *** function, call it with params self, @@@.",
"self.*** = '***'":
"From *** get the *** attribute and set it to '***'."
}

for word in urlopen(WORD_URL).readlines():
  WORDS.append(str(word.strip(), encoding='utf-8'))

def convert_phrases(class_name, function_name, parameters):
  random_phrase_number = random.randint(0, 5)
  snippet = list(PHRASES.keys())[random_phrase_number]
  phrase = PHRASES[snippet]
  results = []
  for sentence in [snippet, phrase]:
    result = sentence[:]
    result = result.replace('%%%', class_name, 1)
    result = result.replace('***', function_name, 1)
    for parameter in parameters:
      result = result.replace("@@@", parameter, 1)
    results.append(result)

  return results

try:
  continue_explain = 'y' 
  class_name = input("Enter a class that you want to create ")
  function_name = input("Enter a function that you want to create ")
  parameters = str(input("Enter three comma separated parameters that you want to create ")).split(',')
  while continue_explain == 'y':
    question, answer = convert_phrases(class_name, function_name, parameters)
    print(question)
    print(f"ANSWER: {answer}\n\n")
    continue_explain = input("Do you want to continue? Y/N?")
except EOFError:
  print("\nBye")

# Example input output:
# Enter a class that you want to create Rectangle
# Enter a function that you want to create area
# Enter three comma separated parameters that you want to create length,width,output_unit
# area = Rectangle()
# ANSWER: Set area to an instance of class Rectangle.


# Do you want to continue? Y/N?y
# Rectangle().area(length)
# ANSWER: From instance of Rectangle get the area function, call it with params self, length.


# Do you want to continue? Y/N?y
# class Rectangle(object):
# 	def __init__(self, length)
# ANSWER: class Rectangle has-a __init__ that takes self and length params.


# Do you want to continue? Y/N?