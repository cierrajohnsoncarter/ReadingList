reading_list = []
menu_prompt = """Enter one of the following:

- 'a' to add a book
- 'l' to list books
- 'q' to quit

What would you like to do?
"""

selected_input = input(menu_prompt).strip().lower()


def add_book():
    title = input('Title: ').strip().title()
    author = input('Author: ').strip().title()
    year = input('Year Published: ').strip()

    reading_list.append({
        'title': title, 'author': author, 'year': year})


def display_book():
    for book in reading_list:
        title, author, year = book.values()
        print(f'{title}, by{author} ({year})')


while True:
    if selected_input == 'q':
        break
    elif selected_input == 'a':
        add_book()
    elif selected_input == 'l':
        display_book()
    else:
        print('Your reading list is empty.')
