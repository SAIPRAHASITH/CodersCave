import random
from tkinter import *

# Define the character sets for the password
lowercase_characters = string.ascii_lowercase
uppercase_characters = string.ascii_uppercase
digits = string.digits
punctuation = "!@#$%^&*()-_+={}[]:;'<>?,./"

# Define the function to generate a random password
def generate_password():
  characters = lowercase_characters + uppercase_characters + digits + punctuation
  password = "".join(random.sample(characters, 8))
  label.config(text=password)

# Create the GUI window
window = Tk()
window.title("Password Generator")

# Create the label and entry widget
label = Label(window, text="Generated Password:")
label.pack()

# Create the button widget
button = Button(window, text="Generate Password", command=generate_password)
button.pack()

# Start the mainloop
window.mainloop()
