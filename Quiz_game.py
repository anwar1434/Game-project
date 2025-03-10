import random
import json
import time

def load_question():
  with open("question.json", "r") as f:
    questions = json.load(f)["Question"]
    return questions

def get_random_question(questions, num_question):
  if num_question > len(questions):
    num_question = len(questions)
  random_questions = random.sample(questions, num_question)
  return random_questions

def ask_question(question):
  while True:
    print(question["question"])
    for i, options in enumerate(question["options"]):
      print(f"{i+1}.{options}")
    ans = input("Select the correct option: ")
    if not ans.isdigit() or not (1 <= int(ans) <= len(question["options"])):
        print("Invalid option selected.")
        continue
        # Convert user input to index for options
    selected_option = question["options"][int(ans) - 1]
    correct = selected_option == question["answer"]
    return correct

score = 0
num_question = int(input("Enter the number of question: "))
questions = load_question()
random_questions = get_random_question(questions, num_question)
for question in random_questions:
  is_correct = ask_question(question)
  if is_correct:
    print("It's the correct answer")
    score += 1
  else:
    print("It's an incorrect answer")
  time.sleep(1)
print("------------------------------")
print(f"your total score is {score}/{len(random_questions)}")