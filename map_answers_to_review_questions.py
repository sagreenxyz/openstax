import json

# Load the review questions JSON file
with open("review_questions.json", "r") as review_file:
    review_questions = json.load(review_file)

# Load the answer key JSON file
with open("answer_key.json", "r") as answer_file:
    answer_key = json.load(answer_file)

# Mapping of answers to integer values
answer_mapping = {"A": 0, "B": 1, "C": 3, "D": 4}

# Add the "correct" field to each question
for question in review_questions:
    chapter = question["chapter"]
    question_number = question["question_number"]
    if chapter in answer_key and question_number in answer_key[chapter]:
        correct_answer = answer_key[chapter][question_number]
        question["correct"] = answer_mapping[correct_answer]

# Save the updated review questions back to the JSON file
with open("review_questions.json", "w") as review_file:
    json.dump(review_questions, review_file, indent=4)