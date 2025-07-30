from quiz_game.question_model import Questions
from quiz_game.questions import question_data
from quiz_game.quiz import QuizGame


def main():
    question_bank = []
    for question in question_data:
        init = Questions(
            question.get("question"),
            question.get("options"),
            question.get("answer")
        )
        question_bank.append(init)

    quiz_game = QuizGame(question_bank)

    quiz_game.start_game()


if __name__ == "__main__":
    main()
