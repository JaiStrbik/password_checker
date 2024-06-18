



import gooeypie as gp
from list_of_common_passwords import common_passwords
from random import choice

common_passwords = common_passwords()

def on_text_change(event):
    ponits = 0
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
    if any(character in digits for character in text):
        points += 20
    if any(character in letters for character in text):
        points += 20
    if any(character in uppercase_letters for character in text):
        points += 20
    if len(text) >= 13:
        points += 15
    else:
        points -= 50
    
    
    label.text = f'Password Score: {points}'
    ranking_label.text = f'Ranking: {ranking(points)}/10'
    return points in text_box


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
        print("You need a new password")
    
    return rating


def generate_password(length, letters, digits, symbols):
    """Returns a new password within a 10 out of 10 ranked password upon clicked on the button"""
    available_chars = ''
    if letters:
        available_chars += ''.join(letters)
    if uppercase_letters:
        available_chars += ''.join(uppercase_letters)
    if digits:
        available_chars += ''.join(digits)
    if symbols:
        available_chars += ''.join(symbols)
    
    new_password = ''.join(choice(available_chars) for _ in range(length))
    return new_password

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

def show_new_password(event):
    """Populates the password box with a newly generated password"""
    new_password = generate_password(length, letters, uppercase_letters, digits, symbols)
    text_box.text = new_password
    return new_password in text_box.text

app = gp.GooeyPieApp('Password Checker')
app.width = 600
app.height = 500

text_box = gp.Textbox(app, 60)
text_box.add_event_listener('change', on_text_change)

check_button = gp.Button(app, 'Click Here for a Strong Password', show_new_password)

label = gp.Label(app, 'Password Score: 0')
ranking_label = gp.Label(app, 'Ranking: 0/10')

app.set_grid(4, 1)
app.add(text_box, 1, 1)
app.add(check_button, 2, 1, align='center')
app.add(label, 3, 1)
app.add(ranking_label, 4, 1)

app.run()
