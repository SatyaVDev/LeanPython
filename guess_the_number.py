from random import randint

# Genarate number between 1 and 100

actual_number = randint(1, 100)

## Print welcome messsage

print("Welcome the number guessing Game!")
print("I am thinking of a number between 1 and 100.")

EASY_COUNTER = 10
HARD_COUNTER = 5


def set_difficulty():
  diffi = input(
      'Choose a difficulty: type "easy" or "hard".: ').lower().strip()

  if diffi == "easy":
    return EASY_COUNTER
  elif diffi == "hard":
    return HARD_COUNTER
  else:
    raise ValueError("Invalid input. Please type 'easy' or 'hard'.")


def guess(user_guess, actual_value, turn):

  if user_guess < actual_value:
    print("Too low\nGuess again.")
    return turn - 1
  elif user_guess > actual_value:
    print("Too hight\n Guess again.")
    return turn - 1
  else:
    print(f"You got it! The answer was {actual_value}")


def game():
  guessed_no = 0
  turns = set_difficulty()
  while guessed_no != actual_number:
    try:

      attempts = f"You have {turns} attempts remaining to guess the number"
      print(attempts)

      guessed_no = int(input("Make a guess : "))
      turns = guess(guessed_no, actual_number, turns)

      if turns == 0:
        print("You Loose!")
        break

    except ValueError as error:
      raise error


print("actual_number ", actual_number)

game()
'''import random

print("Welcome the number guessing Game!")

print("I am thinking of a number between 1 and 100.")

message = 'Choose a difficulty: type "easy" or "hard". : '

is_game_over = False
remaining = 0
compute_think_num = random.choice(range(1, 101))
level = input(message)
if level == "easy":
  remaining = 10
else:
  remaining = 5

while not is_game_over:
  attempts = f"You have {remaining} attempts remaining to guess the number"
  print(attempts)
  if remaining == 0:
    print("Game Over")
    is_game_over = True
    continue

  guessed_no = int(input("Make a guess : "))

  if guessed_no == compute_think_num:
    print(f"You got it! The answer was {compute_think_num}")
    is_game_over = True
  else:
    if guessed_no < compute_think_num:
      print("Too low \nGuess again. ")
    elif guessed_no > compute_think_num:
      print("Too high \nGuess again.")

  remaining -= 1
'''
