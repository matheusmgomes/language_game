import json
import random

def load_words(path):
  with open(path, 'r', encoding='utf-8') as file:
    data = json.load(file)
  
  return data['words']

def pick_word(word_list):
    index = random.randrange(len(word_list))
    return word_list.pop(index)

def menu():
  print("--- Welcome to language game ---")
  print(" 1 - Play")
  print(" 0 - Exit")

  try:
    return int(input())
  except ValueError:
    return -1

def game(word_list):
  current_word = pick_word(word_list)
  print(f"What does {current_word['word']} mean in English?")
  answer = input().strip().lower()

  translations = current_word["translation"].split('/')
  translations = [x.strip().lower() for x in translations]

  if answer in translations:
    print("That's correct!")
    return True
  else:
    print("That is not correct.")
    print(f"The answer is {current_word['translation']}")
    print(f"\nMeaning: {current_word['meaning']}")
    print("Examples: ")
    for sentence in current_word['sentences']:
      print(sentence)
    
    return False

def main():
  word_list = load_words('data/french_words_v2.json')

  option = menu()

  while option:
    if option != 1:
      print("Type a valid option")
    else:
      current_word_list = word_list.copy()
      score = 0
      question_count = 1
      keep_playing = True 
      while keep_playing and len(current_word_list) > 0:
        print(f"Question {question_count}/100")
        print(f"Score: {score}")
        keep_playing = game(current_word_list)

        if keep_playing:
          score += 1
          question_count += 1
      
      if len(current_word_list) == 0:
        print("Congratulations! You answered all words correctly")
      else:
        print(f"Game over! Your score was {score}")

    option = menu()
  
  print("Goodbye")

if __name__ == "__main__":
  main()