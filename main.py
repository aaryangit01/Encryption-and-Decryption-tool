from tkinter import *
from tkinter import messagebox
import base64
import os

def decrypt():
    password = code.get()

    if password == "1234":
        message = text1.get(1.0, END)
        decode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(decode_message)
        decrypt_message = base64_bytes.decode("ascii")

        screen2 = Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="grey")

        Label(screen2, text="DECRYPT", font="arial", fg="white", bg="grey").place(x=10, y=0)
        text2 = Text(screen2, font="roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)
        text2.insert(END, decrypt_message)
        
    elif password=="":
        messagebox.showerror("encryption","Input Password")
        
    elif password !="1234":
        messagebox.showerror("encryption","Invalid Password")
#ENCRYPTION

def encrypt():
    password = code.get()

    if password == "1234":
        message = text1.get(1.0, END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt_message = base64_bytes.decode("ascii")

        screen1 = Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="grey")

        Label(screen1, text="ENCRYPT", font="arial", fg="white", bg="grey").place(x=10, y=0)
        text2 = Text(screen1, font="roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)
        text2.insert(END, encrypt_message)
        
    elif password=="":
        messagebox.showerror("encryption","Input Password")
        
    elif password !="1234":
        messagebox.showerror("encryption","Invalid Password")


def reset():
    code.set("")
    text1.delete(1.0, END)

def main_screen():
    global screen
    global code
    global text1

    screen = Tk()
    screen.geometry("375x398")
    screen.title("ENCRYPTION & DECRYPTION TOOL")
    Label(text="Enter text for encryption and decryption", fg="black", font=("calibri", 13)).place(x=10, y=10)
    text1 = Text(font="roboto 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)

    Label(text="Enter key", fg="black", font=("calibri", 13)).place(x=10, y=170)

    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font=("arial", 25), show="*").place(x=10, y=200)

    Button(text="ENCRYPT", height="2", width=18, bg="red", fg="white", bd=0, command=encrypt).place(x=10, y=250)
    Button(text="DECRYPT", height="2", width=18, bg="green", fg="white", bd=0, command=decrypt).place(x=200, y=250)
    Button(text="RESET", height="2", width=42, bg="blue", fg="white", bd=0, command=reset).place(x=10, y=300)

    screen.mainloop()

main_screen()
