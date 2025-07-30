import random


class QuizGame:

    def __init__(self, questions):
        self.questions = questions

    def print_options(self, options):
        for index, option in enumerate(options, 1):
            print(f"{index}. {option}")

    def start_game(self):
        # print(self.questions)

        random.shuffle(self.questions)
        for index, item in enumerate(self.questions, 1):
            print(f"Q.{index}: {item.question}")
            self.print_options(item.options)
            your_ans = input("Your answer: ")
