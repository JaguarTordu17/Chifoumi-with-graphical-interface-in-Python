import tkinter as tk
import random
import os

dirname = os.path.dirname(__file__)

# fenetre
    
window = tk.Tk()
window.title("Chifoumi")
window.geometry("400x400")
window.config(bg="#7FD7DF")
window.iconbitmap(os.path.join(dirname, 'assets/ico.ico'))
window.resizable(width=False, height=False)

# images

canvas = tk.Canvas(window, width=340, height=150, bg="#7FD7DF")

img11 = tk.PhotoImage(file=os.path.join(dirname, "assets/chisel vs chisel.png"))
img12 = tk.PhotoImage(file=os.path.join(dirname, "assets/chisel vs leaf.png"))
img13 = tk.PhotoImage(file=os.path.join(dirname, "assets/chisel vs pierre.png"))

img21 = tk.PhotoImage(file=os.path.join(dirname, "assets/leaf vs chisel.png"))
img22 = tk.PhotoImage(file=os.path.join(dirname, "assets/leaf vs leaf.png"))
img23 = tk.PhotoImage(file=os.path.join(dirname, "assets/leaf vs pierre.png"))

img31 = tk.PhotoImage(file=os.path.join(dirname, "assets/pierre vs chisel.png"))
img32 = tk.PhotoImage(file=os.path.join(dirname, "assets/pierre vs leaf.png"))
img33 = tk.PhotoImage(file=os.path.join(dirname, "assets/pierre vs pierre.png"))

# choix et scores

user_score = 0
script_score = 0

def add_user_score():
    
    global user_score, script_score
    user_score += 1

    label_user_score = tk.Label(window, text=user_score, bg="#7FD7DF", font=("Helvetica", 25), fg='white')
    label_user_score.place(x=75, y=18)

def add_script_score():
    
    global user_score, script_score
    script_score += 1

    label_script_score = tk.Label(window, text=script_score, bg="#7FD7DF", font=("Helvetica", 25), fg='white')
    label_script_score.place(x=298, y=18)

def choose_chisel():

    label_you = tk.Label(window, text="You :", bg="yellow")
    label_you.place(x=30, y=30)

    label_you = tk.Label(window, text="AI :", bg="yellow")
    label_you.place(x=260, y=30)
    
    label_welcome.destroy()
    script_tool = random.randint(1, 3)
    user_tool = 1

    if user_tool == 1 and script_tool == 1:
        image1 = canvas.create_image(170,77, image=img11)
        canvas.place(x=30, y=80)

    elif user_tool == 1 and script_tool == 2:
        image2 = canvas.create_image(170,77, image=img12)
        canvas.place(x=30, y=80)
        add_user_score()

    elif user_tool == 1 and script_tool == 3:
        image3 = canvas.create_image(170,77, image=img13)
        canvas.place(x=30, y=80)
        add_script_score()

def choose_leaf():
    
    global user_score, script_score

    label_you = tk.Label(window, text="You :", bg="yellow")
    label_you.place(x=30, y=30)

    label_you = tk.Label(window, text="AI :", bg="yellow")
    label_you.place(x=260, y=30)

    label_welcome.destroy()
    script_tool = random.randint(1, 3)
    user_tool = 2

    if user_tool == 2 and script_tool == 1:
        image1 = canvas.create_image(170,77, image=img21)
        canvas.place(x=30, y=80)
        add_script_score()

    elif user_tool == 2 and script_tool == 2:
        image2 = canvas.create_image(170,77, image=img22)
        canvas.place(x=30, y=80)

    elif user_tool == 2 and script_tool == 3:
        image3 = canvas.create_image(170,77, image=img23)
        canvas.place(x=30, y=80)
        add_user_score()

def choose_pierre():

    global user_score, script_score

    label_you = tk.Label(window, text="You :", bg="yellow")
    label_you.place(x=30, y=30)

    label_you = tk.Label(window, text="AI :", bg="yellow")
    label_you.place(x=260, y=30)
    
    label_welcome.destroy()
    script_tool = random.randint(1, 3)
    user_tool = 3

    if user_tool == 3 and script_tool == 1:
        image1 = canvas.create_image(170,77, image=img31)
        canvas.place(x=30, y=80)
        add_user_score()

    elif user_tool == 3 and script_tool == 2:
        image2 = canvas.create_image(170,77, image=img32)
        canvas.place(x=30, y=80)
        add_script_score()
        
    elif user_tool == 3 and script_tool == 3:
        image3 = canvas.create_image(170,77, image=img33)
        canvas.place(x=30, y=80)

# boutons

image_chisel = tk.PhotoImage(file=os.path.join(dirname, "assets/chisel.png"))
button_chisel = tk.Button(window, image=image_chisel, width=100, height=100, command=choose_chisel)
button_chisel.place(x=270, y=270)

image_leaf = tk.PhotoImage(file=os.path.join(dirname, "assets/leaf.png"))
button_leaf = tk.Button(window, image=image_leaf, width=100, height=100, command=choose_leaf)
button_leaf.place(x=150, y=270)

image_pierre = tk.PhotoImage(file=os.path.join(dirname, "assets/pierre.png"))
button_pierre = tk.Button(window, image=image_pierre, width=100, height=100, command=choose_pierre)
button_pierre.place(x=30, y=270)

# bienvenue

label_choose_weapon = tk.Label(window, text="Choose your weapon :", bg="#7FD7DF")
label_choose_weapon.place(x=135, y=221)

label_welcome = tk.Label(window, text="Welcome !", bg="#7FD7DF", font=("Helvetica", 30, "italic bold"), fg='white')
label_welcome.place(x=103, y=110)

window.mainloop()