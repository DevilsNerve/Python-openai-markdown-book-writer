import openai
import time

# 1. Set up OpenAI credentials
openai.api_key = 'YOUR_OPENAI_API_KEY'

def write_book(title, theme, num_chapters, words_per_chapter):
    """
    Function to write a book using OpenAI API.
    
    Parameters:
    - title (str): Title of the book.
    - theme (str): Theme of the book.
    - num_chapters (int): Number of chapters in the book.
    - words_per_chapter (int): Number of words per chapter.
    """
    
    # Create a file to save the content in Markdown format
    with open(f"{title}.md", "w") as book:
        # Write the title of the book
        book.write(f"# {title}\n\n")
        
        for chapter_num in range(1, num_chapters + 1):
            # Define the chapter title in Markdown
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

# Prompt the user for input
title = input("Enter the title of the book: ")
theme = input("Enter the theme of the book: ")
num_chapters = int(input("Enter the number of chapters you want in the book: "))
words_per_chapter = int(input("Enter the number of words per chapter: "))

# Call the function
write_book(title, theme, num_chapters, words_per_chapter)
