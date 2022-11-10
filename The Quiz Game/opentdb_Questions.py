import os
import requests
import json
from data import category_dict
from question_model import Question

# Functions to return a question bank to main progrm could be a class


def clear():
    os.system('cls')


class FetchQuestions:
    def __init__(self):
        self.question_bank = []

    def get_Questions(self):
        """
            Fetching questions from open triva DB, by category if no questions exists fetching random questions
            And returns a question bank
        """
        cat = self.choose_category()
        url = f'https://opentdb.com/api.php?amount=10&category={cat}&type=boolean'
        response = requests.post(url).text
        response_json = json.loads(response)
        print(response_json["response_code"])

        # If Error Code i will fetch Random questions.
        if (response_json["response_code"] > 0):
            # Random choice if there is no questions for that category.
            print(
                f"Random Questions: (No questions available for category {category_dict[cat]})")
            url = 'https://opentdb.com/api.php?amount=10&type=boolean'
            response = requests.post(url).text
            response_json = json.loads(response)
        else:
            print(f"Questions about {category_dict[cat]}")

        for question in response_json["results"]:
            new_question = Question(
                question["question"], question["correct_answer"])
            self.question_bank.append(new_question)

    def choose_category(self):
        print("===Categories===")
        for k in category_dict:
            print(f' {category_dict[k]} ->   {k}')
        key = int(
            input("Choose a Category by enering the number of the Category: "))
        clear()
        return key


""" 
OpenTB.com 
Code 0: Success Returned results successfully.
Code 1: No Results Could not return results. The API doesn't have enough questions for your query. (Ex. Asking for 50 Questions in a Category that only has 20.)
Code 2: Invalid Parameter Contains an invalid parameter. Arguements passed in aren't valid. (Ex. Amount = Five)
Code 3: Token Not Found Session Token does not exist.
Code 4: Token Empty Session Token has returned all possible questions for the specified query. Resetting the Token is necessary.
"""
