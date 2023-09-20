# OpenAI Markdown Book Writer

OpenAI Markdown Book Writer is a Python utility for generating books in Markdown format using the power of the OpenAI GPT API.

## Features

- Generate books in Markdown format, compatible with GitHub READMEs and other Markdown renderers.
- Prompt the user to define their book's title and theme directly from the command line.
- Specify the number of chapters and words per chapter.
- Output is saved as a `.md` file.

## Prerequisites

- An OpenAI account with API access.
- Python 3.x

## Setup

1. Clone the repository:

```bash
git clone https://github.com/DevilsNerve/Python-openai-markdown-book-writer.git
```

2. Install the required packages:

```bash
pip install openai
```

3. Replace `'YOUR_OPENAI_API_KEY'` in the script with your actual OpenAI API key.

## Usage

To generate a book in Markdown format, run the script, and you will be prompted to input the title and theme for the book:

For example:

After entering the title as "My AI Generated Book" and the theme as "The Future of Technology", the script will produce a Markdown file titled "My AI Generated Book" with a theme centered on "The Future of Technology", containing 5 chapters and approximately 2000 words per chapter.

Alternatively, you can call the `write_book` function directly:

```python
write_book("Title of the Book", "Theme of the Book", num_chapters=5, words_per_chapter=2000)
```

## Caution

Generating a book will make multiple API calls to OpenAI. Be aware of the API rate limits and associated costs when generating large volumes of content.

## Contributing

Pull requests are welcome. If you have major changes in mind, kindly open an issue first to discuss the proposed changes.

## License

[MIT](https://choosealicense.com/licenses/mit/)
```

The key changes made:
1. Added information about prompting the user to define their book's title and theme directly from the command line.
2. Updated the Usage section to provide instructions on how to run the script and input the title and theme.
