import json
import random

def load_words(path):
  with open(path, 'r', encoding='utf-8') as file:
    data = json.load(file)
  
  return data['words']

def pick_word(word_list):
  return random.choice(word_list)

def menu():
  print("--- Welcome to langue game ---")
  print(" 1 - Play")
  print(" 0 - Exit")
  return int(input())

def game(word_list):
  current_word = pick_word(word_list)
  print(f"What means {current_word['word']}?")
  answer = input()

  if answer.lower() == current_word["translation"].lower():
    print("That's correct!")
    return True
  else:
    print("That is not correct.")
    return False

def main():
  word_list = load_words('data/german_words.json')

  option = menu()

  while option:
    if option != 1:
      print("Type a valid option")
    else:
      keep_playing = True 
      while keep_playing:
        keep_playing = game(word_list)
    option = menu()
  
  print("Goodbye")

if __name__ == "__main__":
    main()