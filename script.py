reading_list = []
menu_prompt = """Enter one of the following:

- 'a' to add a book
- 'l' to list books
- 'q' to quit

What would you like to do?
"""

selected_input = input(menu_prompt).strip().lower()

# Takes book info


def add_book():
    title = input('Title: ').strip().title()
    author = input('Author: ').strip().title()
    year = input('Year Published: ').strip()

# Adds book to reading list
    reading_list.append({
        'title': title,
        'author': author,
        'year': year
    })

# Lists the books in the reading list


def display_book():
    print()

    for book in reading_list:
        title, author, year = book.values()
        print(f'{title}, by{author} ({year})')

    print()


# Runs 'add_book' and 'display_book' depending on user input and lets the user know if the reading list is empty or if they didn't enter a valid input
while selected_input != 'q':
    if selected_input == 'a':
        add_book()
    elif selected_input == 'l':
        if reading_list:
            display_book()
        else:
            print('Your reading list is empty')
    else:
        print('Sorry,your input is not valid')

# Allows user to change selection after each iteration
    selected_input = input(menu_prompt).strip().lower()
