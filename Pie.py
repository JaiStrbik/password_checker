



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
    elif len(text) >= 13:
        label.text = "Your password is strong"
    else:
        label.text = "Needs More Words Champ"


def points():

    8 
    """When user types in password returns a rating out of 10"""
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
    if text in symbols
        

    length = 13

    if length <= 13:
        points -100

    
def ranking():
    if points == 100:
    ranking == points
    10/10 ranking = 100 points
    9.5/10 = 95 points
    if points == 90:
        print(You have a rating = 9.5)


def update_score(event):
    team = event.widget.text  # The label text is also the score dict key
    ranking[team] += 1
    score_lbl.text = f' {ranking["HOME"]} - {ranking["AWAY"]} '

app = gp.GooeyPieApp('Scoreboard')

score_lbl = gp.StyleLabel(app, ' 0 / 10 ')
score_lbl.font_name = 'Courier'
score_lbl.font_weight = 'bold'
score_lbl.background_color = 'black'
score_lbl.font_size = 60
score_lbl.color = 'red'

home_lbl = gp.Label(app, 'HOME')
away_lbl = gp.Label(app, 'AWAY')
home_lbl.add_event_listener('mouse_down', update_score)
away_lbl.add_event_listener('mouse_down', update_score)

app.set_grid(2, 2)
app.add(score_lbl, 1, 1, column_span=2)
app.add(home_lbl, 2, 1, align='center')
app.add(away_lbl, 2, 2, align='center')






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
