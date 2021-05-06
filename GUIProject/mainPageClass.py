import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from moviePageClass import moviePage
from seriesPageClass import seriesPage
from LangPack import I18N
import sqlite3
#from loginPageClass import LoginPage
import settings as settings

class mainPage:
    def __init__(self,user,master):
        self.master = master
        self.i18n = I18N(self.master.choice.get())
        self.win = tk.Toplevel()
        self.win.grab_set()
        self.win.title(self.i18n.main_page_title)
        self.win.geometry("600x500+710+290")
        self.win.resizable(False, False)
        self.current_user = user
        self.create_widgets()
        #self.choice2=self.LoginPage.choice.get()

    def list_favorites(self):
        con = sqlite3.connect("Users.db")
        cur = con.cursor()
        cur.execute("SELECT favs FROM Users WHERE username=?", [self.current_user])
        rec = cur.fetchone()

        favSeries = rec[0].split(",")
        cur.execute("SELECT favsMovies FROM Users WHERE username=?", [self.current_user])
        rec = cur.fetchone()

        favMovies = rec[0].split(",")
        con.close()

        conn = sqlite3.connect("Movies.db")
        curr = conn.cursor()


        self.scr_text1.configure(state="normal")
        self.scr_text1.delete("1.0", tk.END)


        for i in favMovies:
            if i != "":
                curr.execute("SELECT name FROM Movies WHERE mid=?", [i])
                rec = curr.fetchone()
                self.scr_text1.insert(tk.INSERT, rec[0] + "\n")

        self.scr_text1.configure(state="disabled")

        conn.close()

        connn = sqlite3.connect("Series.db")
        currr = connn.cursor()

        self.scr_text2.configure(state="normal")
        self.scr_text2.delete("1.0", tk.END)

        for i in favSeries:
            if i != "":
                currr.execute("SELECT name FROM Series WHERE mid=?", [i])
                rec = currr.fetchone()
                print(rec[0])
                self.scr_text2.insert(tk.INSERT, rec[0] + "\n")

        self.scr_text2.configure(state="disabled")

        connn.close()

    def list_favoritesTR(self):
        con = sqlite3.connect("Users.db")
        cur = con.cursor()
        cur.execute("SELECT favs FROM Users WHERE username=?", [self.current_user])
        rec = cur.fetchone()

        favSeries = rec[0].split(",")
        cur.execute("SELECT favsMovies FROM Users WHERE username=?", [self.current_user])
        rec = cur.fetchone()

        favMovies = rec[0].split(",")
        con.close()

        conn = sqlite3.connect("Movies.db")
        curr = conn.cursor()


        self.scr_text1.configure(state="normal")
        self.scr_text1.delete("1.0", tk.END)


        for i in favMovies:
            if i != "":
                curr.execute("SELECT name FROM MoviesTr WHERE mid=?", [i])
                rec = curr.fetchone()
                self.scr_text1.insert(tk.INSERT, rec[0] + "\n")

        self.scr_text1.configure(state="disabled")

        conn.close()

        connn = sqlite3.connect("Series.db")
        currr = connn.cursor()

        self.scr_text2.configure(state="normal")
        self.scr_text2.delete("1.0", tk.END)

        for i in favSeries:
            if i != "":
                currr.execute("SELECT name FROM SeriesTr WHERE mid=?", [i])
                rec = currr.fetchone()
                print(rec[0])
                self.scr_text2.insert(tk.INSERT, rec[0] + "\n")

        self.scr_text2.configure(state="disabled")

        connn.close()

    def goToMoviePage(self):
        app = moviePage(self.current_user,self)
        app.win.mainloop()

    def goToSeriesPage(self):
        app = seriesPage(self.current_user,self)
        app.win.mainloop()

    def create_widgets(self):
        self.btn_movies = ttk.Button(self.win, text=self.i18n.main_page_movies_button, command=self.goToMoviePage)
        self.btn_movies.grid(column=0, row=0, padx=15, pady=5)

        self.btn_tv_series = ttk.Button(self.win, text=self.i18n.main_page_series_button, command=self.goToSeriesPage)
        self.btn_tv_series.grid(column=1, row=0, padx=15, pady=5)

        self.lbl_fav1 = ttk.Label(self.win, text=self.i18n.main_page_movies_fav)
        self.lbl_fav1.grid(column=0, row=1, padx=5, pady=2)

        self.lbl_fav2 = ttk.Label(self.win, text=self.i18n.main_page_series_fav)
        self.lbl_fav2.grid(column=1, row=1, padx=5, pady=2)

        self.scr_text1 = scrolledtext.ScrolledText(self.win, width=30, height=12, wrap=tk.WORD)
        self.scr_text1.grid(column=0, row=2, padx=5, pady=2)

        self.scr_text2 = scrolledtext.ScrolledText(self.win, width=30, height=12, wrap=tk.WORD)
        self.scr_text2.grid(column=1, row=2, padx=5, pady=2)

        self.btn_logoff = ttk.Button(self.win, text=self.i18n.main_page_logoff_button, command=self.win.destroy)
        self.btn_logoff.grid(column=0, row=3, columnspan=2, pady=10)

        if settings.language =="en":
            self.list_favorites()
        
        else:
            self.list_favoritesTR()
