# OpenAI Markdown Book Writer

OpenAI Markdown Book Writer is a Python utility for generating books in Markdown format using the power of the OpenAI GPT API.

## Features

- Generate books in Markdown format, compatible with GitHub READMEs and other Markdown renderers.
- Define your book's title and theme.
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

To generate a book in Markdown format, call the `write_book` function:

```python
write_book("Title of the Book", "Theme of the Book", num_chapters=5, words_per_chapter=2000)
```

For example:

```python
write_book("My AI Generated Book", "The Future of Technology", num_chapters=5, words_per_chapter=2000)
```

This will produce a Markdown file titled "My AI Generated Book" with a theme centered on "The Future of Technology", containing 5 chapters and approximately 2000 words per chapter.

## Caution

Generating a book will make multiple API calls to OpenAI. Be aware of the API rate limits and associated costs when generating large volumes of content.

## Contributing

Pull requests are welcome. If you have major changes in mind, kindly open an issue first to discuss the proposed changes.

## License

[MIT](https://choosealicense.com/licenses/mit/)
