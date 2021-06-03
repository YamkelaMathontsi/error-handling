from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Authenfication")
root.geometry("400x500")
root.config(bg="pink")

def clear_text():
    username_ent.delete(0, END)
    password_ent.delete(0, END)

def destroy():
    msg_box = messagebox.askquestion("Closing Programing, Are You Sure")
    root.destroy()

# Labels
header = Label(root, text="Please Enter Login Details")
header.place(x=100, y=10)
username = Label(root, text="Username:")
username.place(x=150, y=70)
password = Label(root, text="Password:")
password.place(x=150, y=140)

#Entries

username_ent = Entry(root, text="")
username_ent.place(x=100, y=100)
password_ent = Entry(root, text="")
password_ent.place(x=100, y=170)


def user_pass_search():

    user_pass = {'Yamkela': '@merclife'}

    if username_ent.get() in user_pass:
        if password_ent.get() == user_pass[username_ent.get()]:
            root.destroy()
            import expection

        else:
            messagebox.showerror("STATUS", "ACCESS GRANTED!")
    else:
        messagebox.showerror("ERROR", "ACCESS NOT GRANTED!")

verify = Button(root, text='Login', bg="tan",  command=user_pass_search, width=10 )
verify.place(x=130, y=200)
# clear_btn = Button(root, text='Clear', bg="tan", command=clear_text)
# clear_btn.place(x=120, y=200)
# exit = Button(root, text='Exit', bg="tan", command=destroy)
# exit.place(x=220, y=200)


root.mainloop()

