# /workspaces/openstax/extract_review_questions.py

import os
import json
from bs4 import BeautifulSoup

def extract_questions_from_html(file_path):
    """Extracts multiple-choice questions from an HTML file."""
    questions = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')
            # Debug: Print the file being processed
            print(f"Processing file: {file_path}")
            
            # Extract chapter number from the filename
            chapter_number = None
            if "Ch." in file_path:
                try:
                    chapter_number = file_path.split("Ch. ")[1].split(" ")[0]
                except IndexError:
                    print(f"Warning: Could not extract chapter number from {file_path}")

            # Locate the container with multiple-choice questions
            question_containers = soup.find_all('div', class_='os-problem-container')
            if question_containers:
                for container in question_containers:
                    # Extract the question number
                    question_number_tag = container.find_previous('span', class_='os-number')
                    if question_number_tag:
                        question_number = question_number_tag.get_text(strip=True)
                    else:
                        print("Warning: No question number found.")
                        continue
                    
                    # Extract the question text
                    question_text_tag = container.find('p')
                    if question_text_tag:
                        question_text = question_text_tag.get_text(strip=True)
                    else:
                        print("Warning: No question text found.")
                        continue
                    
                    # Extract the options
                    options = [li.get_text(strip=True) for li in container.find_all('li')]
                    if not options:
                        print("Warning: No options found.")
                        continue
                    
                    # Append the question, options, chapter, and question number as a dictionary
                    questions.append({
                        'chapter': chapter_number,
                        'question_number': question_number,
                        'question': question_text,
                        'options': options
                    })
            else:
                # Debug: Print a warning if no questions are found
                print(f"Warning: No multiple-choice questions found in {file_path}")
    except Exception as e:
        # Debug: Print any errors encountered while processing the file
        print(f"Error processing file {file_path}: {e}")
    return questions

def main():
    # Correct the input folder path
    input_folder = "/workspaces/openstax/OpenStax Anatomy and Physiology 2e/html"
    output_file = "/workspaces/openstax/review_questions.json"
    all_questions = []

    for root, _, files in os.walk(input_folder):
        for file in files:
            # Debug: Print the file being checked
            print(f"Checking file: {file}")
            if "Review Questions" in file and file.endswith(".html"):
                file_path = os.path.join(root, file)
                questions = extract_questions_from_html(file_path)
                all_questions.extend(questions)

    # Sort questions by chapter number and question number
    all_questions.sort(key=lambda q: (int(q['chapter']), int(q['question_number'])))

    # Debug: Print the total number of questions extracted
    print(f"Total questions extracted: {len(all_questions)}")

    # Write sorted questions to the JSON file
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(all_questions, json_file, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    main()