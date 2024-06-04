


# char_num = -
# symbol_detected = Falsesymbols = [@#$%^&*]
# while symbol_detected == False and char_num <= length of List_of_Common_Passwords
# #Check each character agaaninst the symbols list
# For I = 0 to length of symbols
# If password[char_num] == symbols[i]
# symbol_detected = True
# next i
# char_num +=



import gooeypie as gp
from list_of_common_passwords import common_passwords
from random import choice
common_passwords = common_passwords()

def on_text_change(event):
    text = text_box.text
    invalid_symbols = {"!", "@", "#", "$", "%", "^", "&", "*", "~", "`", "-", "_","+","=", "<",">","?","/","[]","{", "}", ":", ";", "|",}
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

def check_password(event):
    on_text_change(event)



def generate_password(length, letters, digits, symbols):
    """returns a new password within a 10 out of 10 ranked password upon clicked on the button"""
    #set characters from which to choose from
    #Make the password by using the string above
    available_chars = ''
    if letters:
        available_chars
    if digits:
        available_chars
    if symbols:
        available_chars
    #Make the new password by choosing from the avialble letters,digits and symbols above
    new_password = ''
    for count in range(length): #For Loop
        new_password += choice(available_chars)
    return new_password
    
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

symbols = [
    ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-',
    '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_',
    '`', '{', '|', '}', '~'
]
length = int(8)
def show_new_password(event):
    """Populates the password box with a newly generated password"""
    gp.Textbox= generate_password(length, letters, symbols, digits)

# Print the sections

app = gp.GooeyPieApp('Password Checker')
app.width = 600
app.height = 500
check_button = gp.Button(app, 'Click Here for a Strong Password', show_new_password)


text_box = gp.Textbox(app, 60)
text_box.add_event_listener('change', on_text_change)



label = gp.Label(app, 'blank')



app.set_grid(3, 1)
app.add(text_box, 1, 1)
app.add(check_button, 2, 1, align='center')
app.add(label, 3, 1)

app.run()
