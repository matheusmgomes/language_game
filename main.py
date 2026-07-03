import json
import random

WORDS_PATH = 'data/french_words_v2.json'

def clear_screen():
  print("\n" * 40)

def load_words(path):
  with open(path, 'r', encoding='utf-8') as file:
    data = json.load(file)
  
  return data['words']

def pick_word(word_list):
    index = random.randrange(len(word_list))
    return word_list.pop(index)

def normalize(text):
  return text.strip().lower()


def print_header():
  print("=" * 45)
  print("          LANGUAGE GUESSING GAME")
  print("=" * 45)

def menu():
  clear_screen()
  print_header()
  print("\nChoose an option:")
  print("[1] Play")
  print("[0] Exit")

  try:
      return int(input("\nOption: "))
  except ValueError:
      return -1

def print_round_info(question_count, total_questions, score):
  print("-" * 45)
  print(f"Question: {question_count}/{total_questions}")
  print(f"Score: {score}")
  print("-" * 45)  

def show_word_details(word):
  print(f"\nCorrect answer: {word['translation']}")
  print(f"\nMeaning:\n{word['meaning']}")
  print("\nExamples:")

  for sentence in word["sentences"]:
      print(f"- {sentence}")

def press_enter_to_continue():
    input("\nPress Enter to continue...")


def print_final_result(score, total_questions, remaining_words):
  clear_screen()
  print_header()

  if not remaining_words:
      print("\nCongratulations! You answered all words correctly.")
  else:
      print("\nGame over!")

  print(f"\nFinal score: {score}")
  print(f"Total questions: {total_questions}")
  print(f"Words remaining: {len(remaining_words)}")

def game_round(word_list):
  current_word = pick_word(word_list)
  print(f"What does {current_word['word']} mean in English?")
  answer = input().strip().lower()

  translations = current_word["translation"].split('/')
  translations = [x.strip().lower() for x in translations]

  if answer in translations:
    print("That's correct!")
    return True

  print("That is not correct.")
  show_word_details(current_word)
  return False

def play_game(word_list):
  current_word_list = word_list.copy()
  score = 0
  question_count = 1
  total_questions = len(current_word_list)
  keep_playing = True 
  while keep_playing and current_word_list:
    clear_screen()
    print_header()
    print_round_info(question_count, total_questions, score)

    keep_playing = game_round(current_word_list)

    if keep_playing:
      score += 1
      question_count += 1
    
    press_enter_to_continue()

  print_final_result(score, total_questions, current_word_list)
  press_enter_to_continue()

  
  if len(current_word_list) == 0:
    print("Congratulations! You answered all words correctly")
  else:
    print(f"Game over! Your score was {score}")

def main():
  word_list = load_words(WORDS_PATH)

  option = menu()

  while option:
    if option != 1:
      print("Type a valid option")
      press_enter_to_continue()
    else:
      play_game(word_list)

    option = menu()
  
  print("Goodbye")

if __name__ == "__main__":
  main()