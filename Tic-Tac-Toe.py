# Required modules
from tkinter import *
from tkinter import font
from tkinter import messagebox

# Functions
x_turn = True
count = 0
# Disabling the buttons


def disableButtons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

# Check the winner


def checkIfWon():
    global winner
    winner = False
    if b1['text'] == b2['text'] and b2['text'] == b3['text'] and b1['text'] != " ":
        b1.config(bg='#33ff00')
        b2.config(bg='#33ff00')
        b3.config(bg='#33ff00')
        disableButtons()
        txt = b1['text']
        messagebox.showinfo("Tic Tac Toe", f"Congratulations! \n {txt} wins!!")
        winner = True
    elif b4['text'] == b5['text'] and b5['text'] == b6['text'] and b4['text'] != " ":
        b4.config(bg='#33ff00')
        b5.config(bg='#33ff00')
        b6.config(bg='#33ff00')
        disableButtons()
        txt = b4['text']
        messagebox.showinfo("Tic Tac Toe", f"Congratulations! \n {txt} wins!!")
        winner = True
    elif b7['text'] == b8['text'] and b8['text'] == b9['text'] and b7['text'] != " ":
        b7.config(bg='#33ff00')
        b8.config(bg='#33ff00')
        b9.config(bg='#33ff00')
        disableButtons()
        txt = b7['text']
        messagebox.showinfo("Tic Tac Toe", f"Congratulations! \n {txt} wins!!")
        winner = True
    elif b1['text'] == b4['text'] and b4['text'] == b7['text'] and b1['text'] != " ":
        b1.config(bg='#33ff00')
        b4.config(bg='#33ff00')
        b7.config(bg='#33ff00')
        disableButtons()
        txt = b1['text']
        messagebox.showinfo("Tic Tac Toe", f"Congratulations! \n {txt} wins!!")
        winner = True
    elif b2['text'] == b5['text'] and b5['text'] == b8['text'] and b2['text'] != " ":
        b2.config(bg='#33ff00')
        b5.config(bg='#33ff00')
        b8.config(bg='#33ff00')
        disableButtons()
        txt = b2['text']
        messagebox.showinfo("Tic Tac Toe", f"Congratulations! \n {txt} wins!!")
        winner = True
    elif b3['text'] == b6['text'] and b6['text'] == b9['text'] and b3['text'] != " ":
        b3.config(bg='#33ff00')
        b6.config(bg='#33ff00')
        b9.config(bg='#33ff00')
        disableButtons()
        txt = b3['text']
        messagebox.showinfo("Tic Tac Toe", f"Congratulations! \n {txt} wins!!")
        winner = True
    elif b1['text'] == b5['text'] and b5['text'] == b9['text'] and b1['text'] != " ":
        b1.config(bg='#33ff00')
        b5.config(bg='#33ff00')
        b9.config(bg='#33ff00')
        disableButtons()
        txt = b1['text']
        messagebox.showinfo("Tic Tac Toe", f"Congratulations! \n {txt} wins!!")
        winner = True
    elif b3['text'] == b5['text'] and b5['text'] == b7['text'] and b3['text'] != " ":
        b3.config(bg='#33ff00')
        b5.config(bg='#33ff00')
        b7  .config(bg='#33ff00')
        disableButtons()
        txt = b3['text']
        messagebox.showinfo("Tic Tac Toe", f"Congratulations! \n {txt} wins!!")
        winner = True
    if count == 9 and winner == False:
        b1.config(bg="#030ffc")
        b2.config(bg="#030ffc")
        b3.config(bg="#030ffc")
        b4.config(bg="#030ffc")
        b5.config(bg="#030ffc")
        b6.config(bg="#030ffc")
        b7.config(bg="#030ffc")
        b8.config(bg="#030ffc")
        b9.config(bg="#030ffc")
        messagebox.showinfo("Tic Tac Toe", "It's A Tie!\n No One Wins!")
        disableButtons()
# Basic clicking


def turn(b):
    global x_turn, count

    if b["text"] == " " and x_turn == True:
        b["text"] = "X"
        x_turn = False
        count += 1
        checkIfWon()
    elif b["text"] == " " and x_turn == False:
        b["text"] = "O"
        x_turn = True
        count += 1
        checkIfWon()
    else:
        messagebox.showerror(
            "Tic Tac Toe", "Hey! That box has already been selected\nPick Another Box...")


def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, count
    clicked = True
    count = 0

    # Build our buttons
    b1 = Button(root, text=" ", font=("Helvetica", 20), height=3,
                width=6, bg="SystemButtonFace", command=lambda: turn(b1), relief=SOLID)
    b2 = Button(root, text=" ", font=("Helvetica", 20), height=3,
                width=6, bg="SystemButtonFace", command=lambda: turn(b2), relief=SOLID)
    b3 = Button(root, text=" ", font=("Helvetica", 20), height=3,
                width=6, bg="SystemButtonFace", command=lambda: turn(b3), relief=SOLID)

    b4 = Button(root, text=" ", font=("Helvetica", 20), height=3,
                width=6, bg="SystemButtonFace", command=lambda: turn(b4), relief=SOLID)
    b5 = Button(root, text=" ", font=("Helvetica", 20), height=3,
                width=6, bg="SystemButtonFace", command=lambda: turn(b5), relief=SOLID)
    b6 = Button(root, text=" ", font=("Helvetica", 20), height=3,
                width=6, bg="SystemButtonFace", command=lambda: turn(b6), relief=SOLID)

    b7 = Button(root, text=" ", font=("Helvetica", 20), height=3,
                width=6, bg="SystemButtonFace", command=lambda: turn(b7), relief=SOLID)
    b8 = Button(root, text=" ", font=("Helvetica", 20), height=3,
                width=6, bg="SystemButtonFace", command=lambda: turn(b8), relief=SOLID)
    b9 = Button(root, text=" ", font=("Helvetica", 20), height=3,
                width=6, bg="SystemButtonFace", command=lambda: turn(b9), relief=SOLID)

    # Grid our buttons to the screen
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)


# Creating the window
root = Tk()
root.title("Tic Tac Toe - By Nishanth")
root.iconbitmap("img/logo.ico")
root.resizable("False", "False")

# Menu bar
my_menu = Menu(root)
root.config(menu=my_menu)
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Rest Game", command=reset)
reset()

# Running the app
root.mainloop()
