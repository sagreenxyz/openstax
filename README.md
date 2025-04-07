# OpenStax Importer

This project provides a command-line tool to import content from various sources into the OpenStax books format. It supports importing from Google Docs, HTML files, and potentially other formats in the future.

## Supported Commands

*   `import`: Imports content from a specified source into the OpenStax books format.
*   `html_to_md`: Converts OpenStax HTML chapter subsections to Markdown files, extracting content within the `<main>` tag.

## Usage

To use the import command:

```bash
./run import --help
```

For more detailed help on the import command, run:

```bash
./run import --help
```

To use the `html_to_md` script:

1.  Ensure you have Python 3 installed.
2.  Install the required packages: `pip install beautifulsoup4 html2text`
3.  Run the script: `python html_to_md.py`
    *   The script converts HTML files starting with a digit in the `OpenStax Anatomy and Physiology 2e` directory to Markdown files in the `markdown_output` directory.
    *   The script extracts content within the `<main>` tag.