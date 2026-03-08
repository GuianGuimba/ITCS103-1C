import tkinter as tk

# Creating A Window

window = tk.Tk()
window.title("My First Tkinter Window")
window.geometry("400x900")
window.resizable(False,False)
window.configure(bg="lightgreen")


# Creating A Label
# Label is a widget used to display a text or images in a window
# It is only read-only (Users cannot type into it)
# Commonly used for titles, Instruction, and output messages

Label = tk.Label(window, text = "Welcome to TKinter",
                 font=("Arial",14,"bold"),
                 fg=("black"),
                 bg=("white"),
                 width=20,
                 height=2,
                 anchor=("center")
                 )

# pack() is a layout manager in Tkinter
# It controls how and where a widget is placed inside its parent container
# A widget will not appear unless a layout manager is used
# By default, pack() places widgets from top to bottom and centers them horizontally
# Arrangement of packing matters.

Label.pack(side="top",
           padx=10,
           pady=20,
           fill='x',
           expand=False
           )

# There is no separate Image widget
# Images are displayed by assigning them to a Label’s image property.
# Tkinter only supports PNG, GIF
# Image file must be in the same folder as the .py file (or use full path)

img = tk.PhotoImage(file="logo2.png")

# Reduces the image size , accepts numbers for denominators
img = img.subsample(3,3) 

# Enlarges the image size, accepts numbers as multipliers for original size
# img = img.zoom(2,2)

image_label = tk.Label(window, image = img)
image_label.pack()

# Button widgets are used to display clickable buttons.
# Users press a button to perform an action.

def on_click():
    button['text'] = "Button Clicked"

button = tk.Button(
    window,
    text="Click Me",
    command=on_click,
    fg="white",
    bg="blue",
    font=("Arial",12,"bold"),
    width=15,
    height=2,
    bd=4,
    relief="raised",
    activebackground="navy",
    activeforeground="white"
)
button.pack(pady=10,
            padx=20,
            fill="x")

# An entry widget provides users with a single-line text field where they can type in a string value.


window.mainloop()
