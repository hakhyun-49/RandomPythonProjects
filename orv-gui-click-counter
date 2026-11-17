#A simple orv based gui button interface.
import tkinter as tk
from tkinter import messagebox
# importing the tkinter module for the gui.
window = tk.Tk()

# color palette for aesthetics.
BG = "#1e1e2e"
TEXT = "#f5e0dc"
ACCENT = "#3A3B3C"
HOVER = "#4E4F50"

# hover effects for aesthetics.
def mouse_enter(event):
    button.config(bg=HOVER)

def mouse_leave(event):
    button.config(bg=ACCENT)

# window geometry and details.
window.geometry("400x400")
window.title("orv.")
window.configure(bg=BG)

# label number 1.
label1 = tk.Label(window, text="Omniscient Readers Viewport", font=("Arial", 15, "bold"), fg=TEXT, bg=BG)
label1.pack(pady=(30,10))

# button that runs the count function when clicked.
button = tk.Button(
    window,
    text="This story is just for that one reader.",
    font=("Ink Free", 10),
    fg=TEXT,
    bg=ACCENT,
    activeforeground=TEXT,
    activebackground=HOVER,
    relief="flat",
    padx=20,
    pady=10,
)

button.pack()

click = 0

# counts clicks and shows the value after each click.
def count():
    global click
    click += 1
    print(click)
    counter_label.config(text=str(click))
    if click==1864:
        print(("[The Oldest Dream has reached his ■■]")
)

counter_label = tk.Label(window, text=str(click), font=("Monaco", 15), fg=TEXT, bg=BG)
counter_label.pack(pady=10)

button.config(command=count)

# hover effect.
button.bind("<Enter>", mouse_enter)
button.bind("<Leave>", mouse_leave)

# resets the counter to zero.
def reset():
    #could actually have a reset button but not here.
    #global click
    #click = 0
    #counter_label.config(text="0")
    messagebox.showerror("Error", "Regression is disabled.")
    

reset_button = tk.Button(window, text="reset", command=reset)
reset_button.pack(pady=10)

window.mainloop()
