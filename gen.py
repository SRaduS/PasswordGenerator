from tkinter import *
import random
import string
import webbrowser

# set up the GUI
window = Tk()
window.title("Python Project - Password Generator")
window.geometry("500x400")

# provide a guide for creating a strong password
def callback(url):
    webbrowser.open_new(url)

link = Label(window, text = "Guide For Creating A Strong Password!", fg="blue", cursor="hand2")
link.bind("<Button-1>", lambda e: callback("https://blog.avast.com/strong-password-ideas"))
link.pack()

# function for input validation/enforcement
def callback(input):
    if input.isdigit():
        if int(input) > 3:
            return True
    else:
        return False
        print("Input must be a digit bigger than 3!")
reg = window.register(callback)

def rand_password():
    # clear box
    pass_entry.delete(0, END)

    # get length, convert to integer
    pass_length = int(entry.get())
    
    # create variable to store password
    actual_password = ""

    # make a third of the password be symbolic or numeric
    symbol = pass_length // 3
    numeric = pass_length // 3
    alpha = pass_length - numeric - symbol

    # loop through the 3 variables to create password
    for i in range(alpha):
        actual_password += random.choice(string.ascii_letters)
    for i in range(symbol):
        actual_password += random.choice(string.punctuation)
    for i in range(numeric):
        actual_password += random.choice(string.digits)
    
    # loop through password length
    #for i in range (alpha):
    #    actual_password += chr(randint(33, 126))
    
    # rearrange the password's characters randomly
    actual_password = list(actual_password)
    random.shuffle(actual_password)
    actual_password = "".join(actual_password)
    # output password 
    pass_entry.insert(0, actual_password)

def clip_password():
    # clear the clipboard
    window.clipboard_clear()
    
    # copy to clipboard
    window.clipboard_append(pass_entry.get())
    pass

# create label frame for input entry
label = LabelFrame(window, text="Password Length")
label.pack(pady=40)

# create entry for geting input
entry = Entry(label, font=("Times New Roman", 24))
entry.pack(padx=20, pady=20)
entry.config(validate="key", validatecommand=(reg, "%S"))

# display password
pass_entry = Entry(window, text="", font=("Times New Roman", 24), bd=0, bg="systembuttonface")
pass_entry.pack(pady=20)

# buttons frame
b_frame = Frame(window)
b_frame.pack(pady=20)

# create buttons
button = Button(b_frame, text="Generate Password", command=rand_password)
button.grid(row=0, column=0, padx=10)

clip_button = Button(b_frame, text="Copy To Clipboard", command=clip_password)
clip_button.grid(row=0, column=1, padx=10)


window.mainloop()