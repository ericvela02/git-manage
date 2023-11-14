from InquirerPy import prompt
from pprint import pprint

def confirm_full_search():
    questions = [
        {
            "type": "confirm",
            "message": "Are you sure you want to search all drives?\n This may take a while.",
            "name": "confirm"
        }
    ]

    answers = prompt(questions)

    return answers['confirm']