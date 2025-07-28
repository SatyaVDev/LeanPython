from math import log
from random import choice
from .art import logo, vs

from .game_data import data


def assign():
  return choice(data)


def compare_answers(list1, list2, ans):

  print(f"{list1}")
  print(f"{list2}")
  follower_1 = list1["follower_count"]
  follower_2 = list2["follower_count"]

  if follower_2 > follower_1:
    return True
  else:
    return False


score = 0
is_game_over = False
# print logo

while not is_game_over:

  persion1 = assign()
  persion2 = assign()

  print(logo)

  print(persion1, "\n", persion2)

  print(
      f'Compare A: name: {persion1["name"]}, desc: {persion1["description"]} ')

  print(vs)

  print(
      f'Compare B:  name: {persion2["name"]}, desc: {persion2["description"]} '
  )

  ans = input("who has more followers? type A or B:")

  return_ansower = compare_answers(persion1, persion2, ans)

  if return_ansower:
    score += 1
    print(f"You are correct! Current_score: {score}")
  else:
    is_game_over = True

print(f"You score is {score}")
