


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


common_passwords = common_passwords()
# for password in common_passwords:
#     print(password)



import gooeypie as gp

def on_text_change(event):
    text = text_box.text
    invalid_symbols = {"!", "@", "#", "$", "%", "^", "&", "*", "~", "`", "-", "_"}
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

app = gp.GooeyPieApp('Password Checker')
app.width = 600
app.height = 500

text_box = gp.Textbox(app, 60)
text_box.add_event_listener('change', on_text_change)

label = gp.Label(app, 'blank')

app.set_grid(2, 1)
app.add(text_box, 1, 1)
app.add(label, 2, 1)


app.run()


