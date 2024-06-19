
# import gooeypie as gp
# from list_of_common_passwords import common_passwords
# from random import choice

# common_passwords = common_passwords()

# def on_text_change(event):
#     points = 0  # Correctly initialize the points variable
#     text = text_box.text
#     digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#     letters = [
#     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
#     'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
#     ]

#     uppercase_letters = [
#     'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
#     'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
#     ]
#     symbols = [
#     '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~'
#     ]     

#     if text in common_passwords:
#         points -= 50 
#     if any(character in symbols for character in text):
#         points += 20
#     else:
#         print("Your password needs a symbol")
#     if any(character in digits for character in text):
#         points += 20
#     if any(character in letters for character in text):
#         points += 20
#     if any(character in uppercase_letters for character in text):
#         points += 20
#     if len(text) >= 13:
#         points += 15
#     else:
#         points -= 50

#     label.text = f'Password Score: {points}'
#     rating_value = ranking(points)
#     ranking_label.text = f'Ranking: {ranking(points)}/10'
#     if rating_value >= 9.5:
#         check_button.enabled = True
#     else:
#         check_button.enabled = False

# def ranking(points):
#     if points >= 100:
#         rating = 10
#     elif points >= 95:
#         rating = 9.5
#     elif points >= 90:
#         rating = 9.0
#     elif points >= 85:
#         rating = 8.5
#     elif points >= 80:
#         rating = 8.0
#     elif points > 50:
#         rating = 5.0
#     else:
#         rating = 0
    
#     return rating


# def generate_password(length, uppercase_letters, letters, digits, symbols):
#     """Returns a new password within a 10 out of 10 ranked password upon clicked on the button"""
#     available_chars = letters + uppercase_letters + digits + symbols
#     new_password = ''.join(choice(available_chars) for _ in range(length))
#     return new_password

# def show_new_password(event):
#     """Populates the password box with a newly generated password"""
#     new_password = generate_password(length, uppercase_letters, letters, digits, symbols)
#     text_box.text = new_password
#     app.copy_to_clipboard(new_password)
#     on_text_change(None)  # Update the score and ranking immediately

# # Character sets
# digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# letters = [
#     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
#     'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
# ]

# uppercase_letters = [
#     'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
#     'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
# ]
# symbols = [
#     '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~'
# ]
# length = 13

# # GooeyPie App setup
# app = gp.GooeyPieApp('Password Checker')
# app.width = 600
# app.height = 500

# text_box = gp.Textbox(app)
# text_box.add_event_listener('change', on_text_change)

# check_button = gp.Button(app, 'Generate Password', show_new_password)

# label = gp.Label(app, 'Password Score: 0')
# ranking_label = gp.Label(app, 'Ranking: 0/10')

# app.set_grid(4, 1)
# app.add(text_box, 1, 1)
# app.add(check_button, 2, 1, align='center')
# app.add(label, 3, 1)
# app.add(ranking_label, 4, 1)

# app.run()

import gooeypie as gp
from list_of_common_passwords import common_passwords
from random import choice

common_passwords = common_passwords()

def on_text_change(event):
    points = 0  # Correctly initialize the points variable
    text = text_box.text
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]

    uppercase_letters = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    ]
    symbols = [
        '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~'
    ]

    if text in common_passwords:
        points -= 50 
    if any(character in symbols for character in text):
        points += 20
    else:
        feedback.text = "your password needs a symbol"
        print("Your password needs a symbol")
    if any(character in digits for character in text):
        points += 20
    else:
        feedback.text = "Your password needs digts"
    if any(character in letters for character in text):
        points += 20
    else:
        feedback.text = "Your password needs letters"
    if any(character in uppercase_letters for character in text):
        points += 20
    else:
        feedback.text = "Your password needs upercase letters"
    if len(text) >= 13:
        points += 15
    else:
        points -= 50 and feedback.text = "Your password needs to be atleast 13 characters in length"

    label.text = f'Password Score: {points}'
    rating_value = ranking(points)
    ranking_label.text = f'Ranking: {ranking(points)}/10'
    if rating_value >= 9.5:
        check_button.enabled = True
    else:
        check_button.enabled = False

def ranking(points):
    if points >= 100:
        rating = 10
    elif points >= 95:
        rating = 9.5
    elif points >= 90:
        rating = 9.0
    elif points >= 85:
        rating = 8.5
    elif points >= 80:
        rating = 8.0
    elif points > 50:
        rating = 5.0
    else:
        rating = 0
    
    return rating


def generate_password(length, uppercase_letters, letters, digits, symbols):
    """Returns a new password within a 10 out of 10 ranked password upon clicked on the button"""
    available_chars = letters + uppercase_letters + digits + symbols
    new_password = ''.join(choice(available_chars) for _ in range(length))
    return new_password

def copy_to_clipboard(event):
   app.copy_to_clipboard(text_box.text)

def show_new_password(event):
    """Populates the password box with a newly generated password"""
    new_password = generate_password(length, uppercase_letters, letters, digits, symbols)
    text_box.text = new_password
    copy_to_clipboard(new_password)
    on_text_change(None)  # Update the score and ranking immediately

# Character sets
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

uppercase_letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
]
symbols = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~'
]
length = 13

# GooeyPie App setup
app = gp.GooeyPieApp('Password Checker')
app.width = 600
app.height = 500

text_box = gp.Textbox(app)
text_box.add_event_listener('change', on_text_change)

check_button = gp.Button(app, 'Generate Password', show_new_password)

label = gp.Label(app, 'Password Score: 0')
ranking_label = gp.Label(app, 'Ranking: 0/10')

feedback = gp.Label(app, 'feedback: 0')

app.set_grid(5, 1)
app.add(text_box, 1, 1)
app.add(check_button, 2, 1, align='center')
app.add(label, 3, 1)
app.add(ranking_label, 4, 1)
app.add(feedback, 5, 1)

app.run()
