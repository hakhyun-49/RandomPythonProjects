import random
import tkinter as tk
import string
# importing libraries.


char= string.ascii_letters+string.digits+string.punctuation
# we now have characters, digits and symbols we may need to use as in a password.
def pass_gen(length):
  # creating a re-usable function so we can use this again
  password=""
  for v in range(length):
    password=password+random.SystemRandom().choice(char)
  return password
def validate():
  user_input=length_entry.get()
  try:
    # Using try and except to ensure no invalid data type like str is entered and using an if loop to make sure no negative value is entered.
    user_input=int(user_input)
  except ValueError:
    result_label.config(text="That is not a valid whole number, try again: ")
    return
  if user_input<=0:
    result_label.config(text="Must be an positive integar, try again: ")
    return
  return result_label.config(text=pass_gen(user_input))

window =tk.Tk()
window.title("Password makerr")
window.geometry("250x200")
#window proportions.
# Widgets
label = tk.Label(window, text="Password length:")
label.pack(pady=10)
length_entry = tk.Entry(window)
length_entry.pack()

button=tk.Button(window,text="Generate",command=validate)
button.pack(pady=10)

result_label = tk.Label(window, text="", wraplength=230)
result_label.pack(pady=10)

window.mainloop()
    
