import json
import os
import sys

# Get file paths from command-line arguments or use defaults
review_questions_path = sys.argv[1] if len(sys.argv) > 1 else "review_questions.json"
answer_key_path = sys.argv[2] if len(sys.argv) > 2 else "OpenStax Anatomy and Physiology 2e/answer_key.json"

# Check if the required files exist
if not os.path.exists(review_questions_path):
    print(f"Error: File not found -> '{os.path.abspath(review_questions_path)}'.")
    print("Please ensure the file exists and provide the correct path.")
    sys.exit(1)

if not os.path.exists(answer_key_path):
    print(f"Error: File not found -> '{os.path.abspath(answer_key_path)}'.")
    print("Please ensure the file exists and provide the correct path.")
    sys.exit(1)

# Load the review questions JSON file
with open(review_questions_path, "r") as review_file:
    review_questions = json.load(review_file)

# Load the answer key JSON file
with open(answer_key_path, "r") as answer_file:
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
with open(review_questions_path, "w") as review_file:
    json.dump(review_questions, review_file, indent=4)