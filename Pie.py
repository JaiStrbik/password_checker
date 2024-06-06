



import gooeypie as gp
from list_of_common_passwords import common_passwords
from random import choice

common_passwords = common_passwords()

def on_text_change(event):
    text = text_box.text
    invalid_symbols = {"!", "@", "#", "$", "%", "^", "&", "*", "~", "`", "-", "_", "+", "=", "<", ">", "?", "/", "[]", "{", "}", ":", ";", "|"}
    numbers = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}

    if text in common_passwords:
        label.text = "Your password is too common"
    elif any(character in invalid_symbols for character in text):
        label.text = "Your password has a symbol"
    elif any(character in numbers for character in text):
        label.text = "Your password has a number"
    elif len(text) >= 8:
        label.text = "Your password is strong"
    else:
        label.text = "Needs More Words Champ"

def generate_password(length, letters, digits, symbols):
    """Returns a new password within a 10 out of 10 ranked password upon clicked on the button"""
    available_chars = ''
    if letters:
        available_chars += ''.join(letters)
    if digits:
        available_chars += ''.join(digits)
    if symbols:
        available_chars += ''.join(symbols)
    
    new_password = ''.join(choice(available_chars) for _ in range(length))
    return new_password

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

symbols = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~'
]

length = 12

def show_new_password(event):
    """Populates the password box with a newly generated password"""
    new_password = generate_password(length, letters, digits, symbols)
    text_box.text = new_password

app = gp.GooeyPieApp('Password Checker')
app.width = 600
app.height = 500

check_button = gp.Button(app, 'Click Here for a Strong Password', show_new_password)
text_box = gp.Textbox(app, 60)
text_box.add_event_listener('change', on_text_change)
label = gp.Label(app, '')

app.set_grid(3, 1)
app.add(text_box, 1, 1)
app.add(check_button, 2, 1, align='center')
app.add(label, 3, 1)

app.run()
