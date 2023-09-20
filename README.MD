# OpenAI Markdown Book Writer

OpenAI Markdown Book Writer is a Python utility for generating books in Markdown format using the power of the OpenAI GPT API.

## Features

- Generate books in Markdown format, compatible with GitHub READMEs and other Markdown renderers.
- Prompt the user to define their book's title, theme, number of chapters, and words per chapter directly from the command line.
- The content generation uses a dynamic continuation approach, ensuring the content is coherent and contextually consistent.
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

To generate a book in Markdown format, run the script, and you will be prompted to input:

- The title of the book.
- The theme of the book.
- The number of chapters you desire.
- The number of words per chapter.

For example:

After entering the title as "My AI Generated Book" and the theme as "The Future of Technology", and specifying the number of chapters and words per chapter, the script will produce a Markdown file titled "My AI Generated Book" with content centered on "The Future of Technology".

Alternatively, you can call the `write_book` function directly:

```python
write_book("Title of the Book", "Theme of the Book", num_chapters=5, words_per_chapter=2000)
```

## Note on `max_tokens`

In the API call to OpenAI, the `max_tokens` parameter limits the response to a certain number of tokens (words, punctuation, etc.) for each request. In our script, this is set to 150 tokens for simplicity and to ensure we don't hit the API's token limit in one call. The script will make multiple calls to generate content up to the specified number of words per chapter, combining the responses to form the chapter content.

## Caution

Generating a book will make multiple API calls to OpenAI. Be aware of the API rate limits and associated costs when generating large volumes of content.

## Contributing

Pull requests are welcome. If you have major changes in mind, kindly open an issue first to discuss the proposed changes.

## License

[MIT](https://choosealicense.com/licenses/mit/)
