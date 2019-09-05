from tkinter import *
from pymongo import MongoClient
from bson.json_util import dumps

client = MongoClient('localhost')

main_screen=()
db=()
collection=()
field=()
filename=()
query_entry=()

def main_account_screen():
    main_screen = Tk()
    main_screen.geometry("300x400")
    main_screen.title("MongoDb Utility")
    main_screen.configure(bg="#F9F0EA")
    Label(text="Choose from Menu", bg="#F9CBCA", width="300", height="1", font=("Calibri", 20)).pack()
    Label(text="").pack()
    Button(text="create db and collection", height="2",bg="#F9CBC6", width="50", command=create).pack()
    Button(text="run query", height="2",bg="#F9CBFA", width="50", command=query).pack()
    Button(text="Show in Files format", height="2", bg="#F9CBC6", width="50", command=create).pack()
    Label(text="").pack()
    main_screen.mainloop()


def query():
    global main_screen
    global db
    global collection
    global filename
    register_screen = Toplevel(main_screen)
    register_screen.title("Private Account")
    register_screen.configure(bg="#F9EBEA")
    register_screen.geometry("300x250")
    qu = StringVar()
    Label(register_screen, text="Please enter query", bg="#F9EBEA").pack()
    Label(register_screen, text="").pack()

    query_entry = Entry(register_screen, textvariable=qu)
    query_entry.pack()

    Button(register_screen, text="Run", width=10, height=1, bg="#B9EBEA", command=funprivate).pack()


def create():
    global main_screen
    global username_entry
    global password_entry
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Public Account")
    register_screen.configure(bg="#F9EBEA")
    register_screen.geometry("300x250")
    username = StringVar()
    Label(register_screen, text="Please enter details below", bg="#F9EBEA").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ",bg="#F9EBEA")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Submit", width=10, height=1, bg="#D9EBEA" , command=funpublic).pack()

def funpublic():
    global username_entry
    username = username_entry.get()

def funprivate():
    global query_entry
    q=query_entry.get()
    print(dumps(q))

main_account_screen()

