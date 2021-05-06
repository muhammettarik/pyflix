import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import sqlite3
from mainPageClass import mainPage
from LangPack import I18N
import settings as settings


class LoginPage:
    def __init__(self):
        self.win = tk.Tk()
        self.i18n = I18N("en")
        self.win.title(self.i18n.login_page_title)
        self.win.geometry("300x350+710+290")
        self.win.resizable(0,0)
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.new_username = tk.StringVar()
        self.new_password = tk.StringVar()
        self.create_widgets()

    def login(self):
        with sqlite3.connect("Users.db") as db:
            cur = db.cursor()
        find_user = "SELECT * FROM Users WHERE username = ? AND password = ?"
        cur.execute(find_user,[(self.username.get()),(self.password.get())])
        results=cur.fetchall()
        if results:
            self.goToMainPage()
        else:
            msg.showerror("Oops!","Username or password is not correct!")

    def new_user(self):
        if len(self.new_username.get()) == 0 or len(self.new_password.get()) == 0:
            msg.showerror("Oops!", self.i18n.create_empty_error)
        else:
            with sqlite3.connect("Users.db") as db:
                cur = db.cursor()
            find_user = "SELECT username FROM Users WHERE username = ?"
            cur.execute(find_user,[(self.new_username.get())])
            if cur.fetchall():
                msg.showerror("Oops!","Username is taken!")
            else:
                msg.showinfo('Success!',"Account created!")
                self.log()
            insert = 'INSERT INTO Users(username, password, favs, favsMovies) VALUES(?,?,?,?)'
            cur.execute(insert, [(self.new_username.get()), (self.new_password.get()), "", ""])
            db.commit()

    def log(self):
        self.username.set("")
        self.password.set("")
        self.create_frame.pack_forget()
        self.head.configure(text=self.i18n.login_page_head)
        self.login_frame.pack()

    def create(self):
        self.new_username.set("")
        self.new_password.set("")
        self.head.configure(text=self.i18n.login_page_head2)
        self.login_frame.pack_forget()
        self.create_frame.pack()

    def goToMainPage(self):
        app = mainPage(self.username.get(),self)
        app.i18n = I18N(self.choice.get())
        app.win.mainloop()

    def reloadText(self):
        print(settings.language)
        settings.language=self.choice.get()
        self.i18n = I18N(settings.language)
        self.win.title(self.i18n.login_page_title)
        self.head.configure(text=self.i18n.login_page_head)

        self.lang_frame.configure(text=self.i18n.lang_frame_label)
        self.langLabel.configure(text=self.i18n.lang_frame_head)
        self.rd1.configure(text=self.i18n.lang_frame_rd1)
        self.rd2.configure(text=self.i18n.lang_frame_rd2)

        self.login_frame.configure(text=self.i18n.login_frame_label)
        self.name_label.configure(text=self.i18n.login_frame_username_label)
        self.psw_label.configure(text=self.i18n.login_frame_password_label)
        self.login_btn.configure(text=self.i18n.login_frame_login_button)
        self.create_btn.configure(text=self.i18n.login_frame_create_button)

        self.create_frame.configure(text=self.i18n.login_frame_label)
        self.name_label2.configure(text=self.i18n.login_frame_username_label)
        self.psw_label2.configure(text=self.i18n.login_frame_password_label)
        self.login_btn2.configure(text=self.i18n.create_frame_login)
        self.create_btn2.configure(text=self.i18n.create_frame_create)

    def create_widgets(self):
        # Head Label
        self.head = ttk.Label(self.win, text=self.i18n.login_page_head)
        self.head.pack(pady=20)

        # Lang Frame Elements
        self.lang_frame = ttk.LabelFrame(self.win, text=self.i18n.lang_frame_label)
        self.lang_frame.pack(pady=10)

        self.langLabel = ttk.Label(self.lang_frame, text=self.i18n.lang_frame_head)
        self.langLabel.grid(column=0, row=0, columnspan=2, padx=5, pady=5)

        
        self.choice = tk.StringVar()
        #settings.language="en"
        self.choice.set("en")

        self.rd1 = ttk.Radiobutton(self.lang_frame, text=self.i18n.lang_frame_rd1, variable=self.choice, value="en", command=self.reloadText)
        self.rd1.grid(column=0, row=1, padx=5, pady=5)

        self.rd2 = ttk.Radiobutton(self.lang_frame, text=self.i18n.lang_frame_rd2, variable=self.choice, value="tr", command=self.reloadText)
        self.rd2.grid(column=1, row=1, padx=5, pady=5)

        # Login Frame
        self.login_frame = ttk.LabelFrame(self.win, text=self.i18n.login_frame_label)
        self.login_frame.pack()

        self.name_label = ttk.Label(self.login_frame, text=self.i18n.login_frame_username_label)
        self.name_label.grid(column=0, row=0, padx=5, pady=(10, 5))

        self.name_entry = ttk.Entry(self.login_frame, textvariable=self.username)
        self.name_entry.grid(column=1, row=0, padx=5, pady=(10, 5))

        self.psw_label = ttk.Label(self.login_frame, text=self.i18n.login_frame_password_label)
        self.psw_label.grid(column=0, row=1, padx=5, pady=5)

        self.psw_entry = ttk.Entry(self.login_frame, textvariable=self.password, show="*")
        self.psw_entry.grid(column=1, row=1, padx=5, pady=5)

        self.login_btn = ttk.Button(self.login_frame, text=self.i18n.login_frame_login_button, command=self.login)
        self.login_btn.grid(column=0, row=4, columnspan=2, padx=5, pady=5)

        self.create_btn = ttk.Button(self.login_frame, text=self.i18n.login_frame_create_button, command=self.create)
        self.create_btn.grid(column=0, row=5, columnspan=2, padx=5, pady=5)

        self.psw_entry.bind("<Return>", lambda e: self.login())

        # Create Frame
        self.create_frame = ttk.LabelFrame(self.win, text=self.i18n.login_frame_label)

        self.name_label2 = ttk.Label(self.create_frame, text=self.i18n.login_frame_username_label)
        self.name_label2.grid(column=0, row=0, padx=5, pady=(10, 5))

        self.name_entry2 = ttk.Entry(self.create_frame, textvariable=self.new_username)
        self.name_entry2.grid(column=1, row=0, padx=5, pady=(10, 5))

        self.psw_label2 = ttk.Label(self.create_frame, text=self.i18n.login_frame_password_label)
        self.psw_label2.grid(column=0, row=1, padx=5, pady=5)

        self.psw_entry2 = ttk.Entry(self.create_frame, textvariable=self.new_password, show="*")
        self.psw_entry2.grid(column=1, row=1, padx=5, pady=5)

        self.login_btn2 = ttk.Button(self.create_frame, text=self.i18n.create_frame_login, command=self.log)
        self.login_btn2.grid(column=0, row=4, columnspan=2, padx=5, pady=5)

        self.create_btn2 = ttk.Button(self.create_frame, text=self.i18n.create_frame_create, command=self.new_user)
        self.create_btn2.grid(column=0, row=5, columnspan=2, padx=5, pady=5)
