import json
import os

def split_review_questions(input_filepath):
    # Load the original JSON file
    with open(input_filepath, 'r') as file:
        questions = json.load(file)
    
    # Create a directory for chapter files if it doesn't exist
    output_dir = os.path.dirname(input_filepath)
    
    # Group questions by chapter
    chapters = {}
    for question in questions:
        chapter = question["chapter"]
        if chapter not in chapters:
            chapters[chapter] = []
        chapters[chapter].append(question)
    
    # Write each chapter's questions to a separate file
    for chapter, chapter_questions in chapters.items():
        output_filepath = os.path.join(output_dir, f"review_questions_chapter_{chapter}.json")
        with open(output_filepath, 'w') as chapter_file:
            json.dump(chapter_questions, chapter_file, indent=4)
        print(f"Created: {output_filepath}")

# Specify the input file path
input_filepath = "/workspaces/openstax/OpenStax Anatomy and Physiology 2e/review_questions.json"

# Run the function
split_review_questions(input_filepath)
