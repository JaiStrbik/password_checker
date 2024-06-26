import gooeypie as gp
from list_of_common_passwords import common_passwords
from random import choice
from zxcvbn import zxcvbn
common_passwords = common_passwords()
def on_text_change(event):
    points = 0  # Correctly initialize the points variable
    text = text_box.text
    feedback_messages = []
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
        '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '', '{', '|', '}', '~'
    ]
    # Use zxcvbn to get additional feedback
    zxcvbn_results = zxcvbn(text)
    zxcvbn_feedback = zxcvbn_results['feedback']
    
    if len(text) >= 13:
        points += 10
    else:
        points -= 30
        feedback_messages.append("Your password needs to have at least 13 characters.")
    if text in common_passwords:
        points -= 50
        feedback_messages.append("Your password is too common.")
    if any(character in symbols for character in text):
        points += 20
    else:
        feedback_messages.append("Your password needs a symbol.")
    if any(character in digits for character in text):
        points += 20
    else:
        feedback_messages.append("Your password needs digits.")
    if any(character in letters for character in text):
        points += 20
    else:
        feedback_messages.append("Your password needs letters.")
    if any(character in uppercase_letters for character in text):
        points += 20
    else:
        feedback_messages.append("Your password needs uppercase letters.")
    if zxcvbn_results['crack_times_display']['offline_slow_hashing_1e4_per_second'] == 'centuries':
        points += 10
    else:
        feedback_messages.append("For a full 10/10 score, your password needs to take centuries to crack.")
    if not feedback_messages:
        feedback.text = "Your password is a 10/10 ranked password"
    else:
        feedback.text = '\n'.join(feedback_messages)
    label.text = f'Password Score: {points}'
    ranking_value = ranking(points)
    ranking_label.text = f'Ranking: {ranking_value}/10'
    
    # Display estimated time to crack the password
    crack_times_label.text = f"Time to Crack: {zxcvbn_results['crack_times_display']['offline_slow_hashing_1e4_per_second']}"
def ranking(points):
    if points >= 100:
        rating = 10
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
    on_text_change(None)  # Update the score and ranking immediately
def toggle_mask(event):
    text_box.secret = not text_box.secret

# Character sets



def show_question_mark_info(event):
    show_info(event, """
The construction of SaintLock is as follows: 
I defined lowercase letters, uppercase letters, numbers, digits with a text box. 
Next, I set a points system. If any of the defining characters in each defined list are in the text box, points will be added. 
With extra variables of length and the time it takes to crack the password to add points to a ranking. 
If your password doesn't meet the perfect 10/10 ranking, feedback will be given to improve your password. 
If you don't want to write a password, a password generator is added to give you a perfect password 
which you can copy to your clipboard at any time. 
Thanks for using my app and keep your personal information safe!""")

def show_information_info(event):
    show_info(event, """
I am a 16-year-old computer scientist at Saint Augustine's College, Sydney, who has just begun my coding journey this year. 
I have created this app, SaintLock, to protect your personal information from hackers in this ever-changing technological world.""")

def show_info(event, info_text):
    """Creates a new window with the provided information text"""
    info_window = gp.GooeyPieApp('Information')
    info_label = gp.Label(info_window, info_text)
    info_window.set_grid(1, 1)
    info_window.add(info_label, 1, 1, align='center', valign='middle')
    info_window.run()


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
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '', '{', '|', '}', '~'
]
length = 16

# GooeyPie App setup
app = gp.GooeyPieApp('SaintLock')
app.width = 850
app.height = 600

text_box_label = gp.Label(app, 'Enter Password:')
text_box = gp.Secret(app)
text_box.width = 30  # Adjust width to make it smaller
text_box.add_event_listener('change', on_text_change)
check = gp.Checkbox(app, 'Show Password')
check.add_event_listener('change', toggle_mask)

check_button = gp.Button(app, 'Generate Password', show_new_password)
generate_button = gp.Button(app, 'Generate Password', show_new_password)
copy_button = gp.Button(app, 'Copy to Clipboard', copy_to_clipboard)
label = gp.Label(app, 'Password Score: 0')
ranking_label = gp.Label(app, 'Ranking: 0/10')
crack_times_label = gp.Label(app, 'Time to Crack: N/A')
feedback_label = gp.Label(app, 'Feedback:')
feedback = gp.Label(app, '')


question_mark_button = gp.ImageButton(app, 'q10.png', None, '')
information_button = gp.ImageButton(app, 'i1.png', None, '')

question_mark_button.add_event_listener('press', show_question_mark_info)
information_button.add_event_listener('press', show_information_info)

app.set_grid(10, 3)
app.add(text_box_label, 1, 2, align='center', valign='middle')
app.add(text_box, 2, 2, align='center', valign='middle')
app.add(check, 3, 2, align='center')
app.add(generate_button, 4, 2, align='center')
app.add(label, 5, 2, align='center')
app.add(ranking_label, 6, 2, align='center')
app.add(crack_times_label, 7, 2, align='center')
app.add(feedback_label, 8, 2, align='center')
app.add(feedback, 9, 2, align='center')
app.add(copy_button, 10, 2, align='center')
app.add(question_mark_button, 10, 3, align='center')
app.add(information_button, 10, 1, align='center')

app.run()