
import gooeypie as gp
from list_of_common_passwords import common_passwords
from random import choice
from zxcvbn import zxcvbn

common_passwords = common_passwords()

def on_text_change(event):
    points = 0
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
        feedback_messages.append("For a full 10/10 Ranking, your password needs to take centuries to crack.")
    if not feedback_messages:
        feedback.text = "Your password is a 10/10 ranked password"
    else:
        feedback.text = '\n'.join(feedback_messages)
    label.text = f'Password Score: {points}'
    ranking_value = ranking(points)
    ranking_label.text = f'Ranking: {ranking_value}/10'
    crack_times_label.text = f"Time to Crack: {zxcvbn_results['crack_times_display']['offline_slow_hashing_1e4_per_second']}"

def ranking(points):
    if points >= 100:
        rating = 10
    elif points >= 90:
        rating = 9.0
    elif points >= 80:
        rating = 8.0
    elif points >= 70:
        rating = 7.0
    elif points >= 60:
        rating = 6.0
    elif points >= 50:
        rating = 5.0
    else:
        rating = 0
    
    return rating

def generate_password(length, uppercase_letters, letters, digits, symbols):
    available_chars = letters + uppercase_letters + digits + symbols
    new_password = ''.join(choice(available_chars) for _ in range(length))
    return new_password

def copy_to_clipboard(event):
    app.copy_to_clipboard(text_box.text)

def show_new_password(event):
    new_password = generate_password(length, uppercase_letters, letters, digits, symbols)
    text_box.text = new_password
    on_text_change(None)

def toggle_mask(event):
    text_box.secret = not text_box.secret

def show_question_mark_info(event):
    show_info(event, """
The construction of SaintLock is as follows: 
I defined lowercase letters, uppercase letters, digits and symbols in lists with a simple text box.
Next, I set a points system. If any of the defining characters in each defined list are in the text box, points will be added. 
With extra variables of password length and the time it takes to crack the password I added points up to 100
 and ratings to match the points.
If your password doesn't meet the perfect 10/10 ranking, feedback will be given to improve your password. 
If you don't want to write a password, a password generator is added to give you a 10/10 ranked password 
which you can copy to your clipboard at any time. 
Thanks for using my app and make sure to always keep your personal information safe at all times and
remember SaintLock can fortify your privacy fortress!""")

def show_information_info(event):
    show_info(event, """
My name is Jai and I’m a 16-year-old in my first year at learning software engineer at Saint Agustine's Colledge Sydney. 
Welcome to my password strength checker tool SaintLock. 
My mission is to enhance digital security by identifying vulnerabilities and strengthening protection measures of vital personal data. 
I believe in the importance of safety, protection and privacy in today’s ever-changing digital age. 
I am driven by the core values of hard work, innovation, and integrity. 
I strive to create tools and applications that not only serve a practical purpose but also to make a positive impact for the customer.  
Looking ahead, my aspiration is to continue learning and I am committed to putting in hard work to improve my skills as a Software engineer at the school and possibly out of school.
Thank you for using my app! """)

def show_info(event, info_text):
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

app = gp.GooeyPieApp('SaintLock')
app.width = 850
app.height = 600

text_box_label = gp.Label(app, 'Enter Password:')
text_box = gp.Secret(app)
text_box.width = 30
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

question_mark_image = gp.Image(app, 'q10.png')
information_image = gp.Image(app, 'i1.png')

question_mark_image.add_event_listener('mouse_down', show_question_mark_info)
information_image.add_event_listener('mouse_down', show_information_info)

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
app.add(question_mark_image, 10, 3, align='center')
app.add(information_image, 10, 1, align='center')

app.run()
