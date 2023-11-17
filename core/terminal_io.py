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


def print_repos(repos):
    if len(repos) > 0:
        for repo in repos:
            print("-"*50)
            print("Name: " + (repos[repo] if repos[repo] else "Unknown"))
            print("Path: " + repo)
        
        print("-"*50)
    else:
        print("No repositories found.")