import gooeypie as gp

# from list_of_common_passwords import common_passwords 
# def password_list():
#     password_list = common_passwords


# def on_text_change(event):
#     text = text_box.text
#     print(text)

#     if text == "Jai":
#         label.text = "Me"
#     elif text == "Gus":
#         label.text = "Toothbrush"
#     elif text == password_list():
#         label.text = "Your Password is common"

#         label.text = "Your password is unique"
#     elif text >= int(8):   
#         label.text = "Your password is strong"
#     else:
#         label.text = "Needs More Words Champ"
   

    
    
# app = gp.GooeyPieApp('Password Checker')
# app.width = 600
# app.height = 500
# text_box = gp.Textbox(app, 60, 10)
# text_box.add_event_listener('change', on_text_change)
# label = gp.Label(app, 'blank')

# app.set_grid(2,1)
# app.add(text_box, 1, 1)
# app.add(label, 2, 1)
# app.run()


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




def on_text_change(event):
    text = text_box.text
    if text in common_passwords:
        label.text = "Your password is too common"
    elif len(text) >= 8:
        label.text = "Your password is strong"
    else:
        label.text = "Needs More Words Champ"

app = gp.GooeyPieApp('Password Checker')
app.width = 600
app.height = 500

text_box = gp.Textbox(app, 60, 10)
text_box.add_event_listener('change', on_text_change)

label = gp.Label(app, 'blank')

app.set_grid(2, 1)
app.add(text_box, 1, 1)
app.add(label, 2, 1)
app.run()
