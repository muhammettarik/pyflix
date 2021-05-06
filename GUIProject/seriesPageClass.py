import tkinter as tk
from tkinter import ttk
from LangPack import I18N
import sqlite3
import seriesDetailedPage
#from loginPageClass import LoginPage
import settings as settings

class seriesPage:
    def __init__(self,user,master):
        self.master = master
        self.i18n = I18N(self.master.master.choice.get())
        self.win = tk.Toplevel()
        self.win.grab_set()
        self.win.title(self.i18n.series_page_title)
        self.win.geometry("600x400+650+300")
        self.win.resizable(False, False)
        self.current_user = user
        self.create_widgets()
        #self.choice2=self.LoginPage.choice.get()

        if settings.language =="en":
            self.list_series()
        else:
            self.list_seriesTr()

    def list_series(self):
        con = sqlite3.connect("series.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM Series")

        for i in self.tv.get_children():
            self.tv.delete(i)

        grades = cur.fetchall()
        for g in grades:
            self.tv.insert(parent="", index="end", iid=g[0], values=(g[1], g[2], g[4], g[5]))
        con.close()

    def list_seriesTr(self):
        con = sqlite3.connect("series.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM SeriesTr")

        for i in self.tv.get_children():
            self.tv.delete(i)

        grades = cur.fetchall()
        for g in grades:
            self.tv.insert(parent="", index="end", iid=g[0], values=(g[1], g[2], g[4], g[5]))
        con.close()


    def on_double_click(self, e):
        item = self.tv.selection()[0]
        seriesDetailedPage.seriesDetailed(mid=item, parent=self, user=self.current_user)

    def create_widgets(self):
        self.container = tk.Frame(self.win)
        self.container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.tv_frame = tk.Frame(self.container)
        self.tv_frame.pack()

        self.scr_bar = ttk.Scrollbar(self.tv_frame)
        self.scr_bar.pack(side=tk.RIGHT, fill=tk.Y)

        self.tv = ttk.Treeview(self.tv_frame, yscrollcommand=self.scr_bar.set)
        self.tv.bind("<Double-1>", self.on_double_click)
        self.tv.pack()

        self.scr_bar.configure(command=self.tv.yview)

        self.tv["columns"] = ("name", "category", "release", "imdb")

        self.tv.column("#0", width=0, stretch=tk.NO)
        self.tv.column("name", anchor=tk.W, width=125)
        self.tv.column("category", anchor=tk.W, width=125)
        self.tv.column("release", anchor=tk.CENTER, width=125)
        self.tv.column("imdb", anchor=tk.CENTER, width=125)

        self.tv.heading("#0", text="")
        self.tv.heading("name", text=self.i18n.movie_page_tv_name, anchor=tk.W)
        self.tv.heading("category", text=self.i18n.movie_page_tv_category, anchor=tk.W)
        self.tv.heading("release", text=self.i18n.movie_page_tv_release, anchor=tk.CENTER)
        self.tv.heading("imdb", text=self.i18n.movie_page_tv_imdb, anchor=tk.CENTER)

        self.mainButton = ttk.Button(self.container, text=self.i18n.movie_page_goMain, command=self.win.destroy)
        self.mainButton.pack(pady=10)