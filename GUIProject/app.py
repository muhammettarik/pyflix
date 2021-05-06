from loginPageClass import LoginPage
import database

database.create_databases()
database.fill_databases()
database.fill_databasesTr()

app = LoginPage()
app.win.mainloop()