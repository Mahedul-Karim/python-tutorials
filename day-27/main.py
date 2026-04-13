from tkinter import *

window = Tk()
window.title("Python GUI")
window.minsize(600,550)

label = Label(text="This is a label",font=("Arial",36))
label.pack()

def on_click():
    label.config(text="Button clicked!")

button = Button(text="Click Me",font=("Arial",24),command=on_click)
button.pack()

### FUNCTIONS WITH DEFAULT PARAMETERS
def add_total(n1=199,n2=254):
    return n1+n2

### FUNCTIONS WITH ANYNUMBER OF PARAMETERS
def add(*args):
    total = 0
    for n in args:
        total += n
    return total

### FUNCTIONS WITH KEYWORD ARGUMENTS
def calculate(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

window.mainloop()