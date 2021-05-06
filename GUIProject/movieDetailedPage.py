import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import sqlite3
from LangPack import I18N
#from loginPageClass import LoginPage
import settings  as settings

class movieDetailed:
    def __init__(self, mid, parent, user):
        self.win = tk.Toplevel()
        self.win.grab_set()
        self.win.geometry("350x290+770+340")
        # self.win.resizable(False, False)
        self.mid = mid
        self.parent = parent
        self.i18n = I18N(self.parent.master.master.choice.get())
        self.current_user = user
        self.create_widgets()
        #self.choice2=self.LoginPage.choice.get()

        if settings.language =="en" :
            self.get_movie_detail()
        
        else:
            self.get_movie_detail_tr()

    def get_movie_detail(self):
        con = sqlite3.connect("Movies.db")
        cur = con.cursor()
        cur.execute("SELECT mid, name, category, subject, release, imdb_rate FROM Movies WHERE mid=?", [self.mid])
        rec = cur.fetchone()
        con.close()
        self.fill_window(rec)

    def get_movie_detail_tr(self):
        con = sqlite3.connect("Movies.db")
        cur = con.cursor()
        cur.execute("SELECT mid, name, category, subject, release, imdb_rate FROM MoviesTr WHERE mid=?", [self.mid])
        rec = cur.fetchone()
        con.close()
        self.fill_window(rec)

    def fill_window(self, rec):
        self.win.title(rec[1])
        self.lbl_name.configure(text=rec[1],font=("Times New Roman", 16, "bold"))
        self.lbl_category.configure(text=rec[2])
        self.scr_subject.configure(state="normal")
        self.scr_subject.insert(tk.INSERT, rec[3])
        self.scr_subject.configure(state="disabled")
        self.lbl_release.configure(text=rec[4])
        self.lbl_imdb.configure(text=rec[5])

    def getFavState(self):
        con = sqlite3.connect("Users.db")
        cur = con.cursor()
        cur.execute("SELECT favsMovies FROM Users WHERE username=?", [self.current_user])
        rec = cur.fetchone()

        favList = rec[0].split(',')

        for i in favList:
            if i == str(self.mid):
                self.favAdd.configure(state="disabled")
                break
            else:
                self.favAdd.configure(state="normal")

        con.close()

    def getFavRemoveState(self):
        con = sqlite3.connect("Users.db")
        cur = con.cursor()
        cur.execute("SELECT favsMovies FROM Users WHERE username=?", [self.current_user])
        rec = cur.fetchone()

        favList = rec[0].split(',')

        for i in favList:
            if i == str(self.mid):
                self.favRemove.configure(state="normal")
                break
            else:
                self.favRemove.configure(state="disabled")

        con.commit()
        con.close()

    def addFavorite(self):
        con = sqlite3.connect("Users.db")
        cur = con.cursor()
        cur.execute("SELECT favsMovies FROM Users WHERE username=?", [self.current_user])
        rec = cur.fetchone()

        favList = rec[0].split(',')
        text = ""
        favList.append(str(self.mid))

        for i in favList:
            text += i + ","

        cur.execute("UPDATE Users SET favsMovies=:fav WHERE username=:user",
                    {"user": self.current_user,
                     "fav": text})

        con.commit()
        con.close()

        self.getFavState()
        self.getFavRemoveState()

        self.parent.master.list_favorites()

    def removeFavorite(self):
        con = sqlite3.connect("Users.db")
        cur = con.cursor()
        cur.execute("SELECT favsMovies FROM Users WHERE username=?", [self.current_user])
        rec = cur.fetchone()
        print(self.current_user)

        favList = rec[0].split(',')
        text = ""

        for i in favList:
            if i == self.mid:
                favList.remove(i)
            elif i == "":
                pass
            else:
                text += i + ","

        cur.execute("UPDATE Users SET favsMovies=:fav WHERE username=:user",
                    {"user": self.current_user,
                     "fav": text})

        con.commit()
        con.close()

        self.getFavState()
        self.getFavRemoveState()

        self.parent.master.list_favorites()
        
    def create_widgets(self):
        self.container = tk.LabelFrame(self.win)
        self.container.pack(padx=10, pady=10)

        self.lbl_name = ttk.Label(self.container, text="")
        self.lbl_name.grid(column=0, row=0, columnspan=3, padx=5, pady=(10, 5))
        self.lbl_category = ttk.Label(self.container, text="")
        self.lbl_category.grid(column=0, row=1, padx=5, pady=5)
        self.lbl_release = ttk.Label(self.container, text="")
        self.lbl_release.grid(column=1, row=1, padx=5, pady=5)
        self.lbl_imdb = ttk.Label(self.container, text="")
        self.lbl_imdb.grid(column=2, row=1, padx=5, pady=5)
        self.scr_subject = scrolledtext.ScrolledText(self.container, width=30, height=8, wrap=tk.WORD, state="disabled")
        self.scr_subject.grid(column=0, row=2, columnspan=3, padx=5, pady=5)

        self.favAdd = ttk.Button(self.container, text=self.i18n.detail_addToFav, command=self.addFavorite)
        self.favAdd.grid(column=0, row=3, pady=10)

        self.favRemove = ttk.Button(self.container, text=self.i18n.detail_removeFromFav, command=self.removeFavorite)
        self.favRemove.grid(column=2, row=3, pady=10)

        self.getFavState()
        self.getFavRemoveState()