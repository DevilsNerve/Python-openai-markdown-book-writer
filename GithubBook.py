import openai
import time

# 1. Set up OpenAI credentials
openai.api_key = 'YOUR_OPENAI_API_KEY'

def write_book(title, theme, num_chapters=10, words_per_chapter=1000):
    # Create a file to save the content in Markdown format
    with open(f"{title}.md", "w") as book:
        # Title of the book
        book.write(f"# {title}\n\n")
        
        for chapter_num in range(1, num_chapters + 1):
            # Chapter title in Markdown
            chapter_title = f"## Chapter {chapter_num}: {theme} - Part {chapter_num}"
            book.write(chapter_title + '\n\n')
            
            # Initialize content for the chapter
            chapter_content = ''
            prompt = f"Write about {theme} - Part {chapter_num} in a style suitable for a book chapter."
            
            while len(chapter_content.split()) < words_per_chapter:
                response = openai.Completion.create(
                    engine="davinci",
                    prompt=prompt,
                    max_tokens=150  # Limiting to 150 tokens per API call for simplicity
                )
                chapter_content += response.choices[0].text.strip() + ' '
                prompt = chapter_content  # Continue from where we left
                
                # Wait to avoid hitting rate limits
                time.sleep(5)
            
            book.write(chapter_content + '\n\n')

# Usage
# write_book("My AI Generated Book", "The Future of Technology", num_chapters=5, words_per_chapter=2000)
