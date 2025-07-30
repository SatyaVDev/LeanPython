import json


class Questions:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def __str__(self):
        return json.dumps(self.__dict__, default=str, indent=4)
