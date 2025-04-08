import os
import re
from bs4 import BeautifulSoup
import html2text

def convert_html_to_markdown(html_file, output_dir):
    """
    Converts an HTML file to Markdown format.

    Args:
        html_file (str): Path to the HTML file.
        output_dir (str): Directory to save the Markdown file.
    """
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()

        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract the main content within the <main> tag
        main_content = soup.find('main')

        if not main_content:
            print(f"Warning: No '<main>' tag found in {html_file}. Skipping.")
            return

        # Convert HTML to Markdown
        h = html2text.HTML2Text()
        h.ignore_links = False  # Keep links
        markdown_content = h.handle(str(main_content))

        # Create the output file name
        output_file = os.path.join(output_dir, os.path.splitext(os.path.basename(html_file))[0] + '.md')

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(markdown_content)

        print(f"Converted {html_file} to {output_file}")

    except Exception as e:
        print(f"Error processing {html_file}: {e}")

def main(input_dir, output_dir):
    """
    Converts all HTML files in the input directory to Markdown files
    in the output directory.

    Args:
        input_dir (str): Directory containing the HTML files.
        output_dir (str): Directory to save the Markdown files.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith('.html'):
            html_file = os.path.join(input_dir, filename)
            convert_html_to_markdown(html_file, output_dir)

if __name__ == "__main__":
    input_directory = './OpenStax Anatomy and Physiology 2e/html'  # Updated to target the specific directory
    output_directory = './markdown_output'  # Replace with the desired output directory
    main(input_directory, output_directory)
