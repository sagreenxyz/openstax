import json
import os

def load_questions(filepaths):
    all_questions = []
    for filepath in filepaths:
        with open(filepath, 'r', encoding='utf-8') as file:
            questions = json.load(file)
            all_questions.extend(questions)
    return all_questions

def sort_questions(questions):
    return sorted(questions, key=lambda q: (int(q['chapter']), int(q['question_number'])))

def save_questions(questions, output_filepath):
    with open(output_filepath, 'w', encoding='utf-8') as file:
        json.dump(questions, file, indent=4)

def main():
    input_folder = "/workspaces/openstax/OpenStax Anatomy and Physiology 2e"
    output_filepath = os.path.join(input_folder, "review_questions_answered.json")
    
    # List of input files
    filepaths = [
        os.path.join(input_folder, f"review_questions_chapter_{i}.json") for i in range(1, 29)
    ]
    
    all_questions = load_questions(filepaths)
    sorted_questions = sort_questions(all_questions)
    save_questions(sorted_questions, output_filepath)

if __name__ == "__main__":
    main()
