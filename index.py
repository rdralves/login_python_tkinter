from atexit import register
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import dataBaser

# Criar nossa Janela
jan = Tk()
jan.title("DP System - Acess Panel")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)
jan.iconbitmap(default="icons\LogoIcon.ico")
jan.attributes("-alpha", 0.8)
# ===========Carregando Imagens =================

logo = PhotoImage(file="D:\login\icons\logo.png")

# ================== Widgets ======================================================
leftFrame = Frame(jan, width=200, height=300,
                  bg="MIDNIGHTBLUE", relief="raise")
leftFrame.pack(side=LEFT)

rightFrame = Frame(jan, width=395, height=300,
                   bg="MIDNIGHTBLUE", relief="raise")
rightFrame.pack(side=RIGHT)

LogoLabel = Label(leftFrame, image=logo, bg="MIDNIGHTBLUE")
LogoLabel.place(x=50, y=100)

userLabel = Label(rightFrame, text="Username", font=(
    "Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
userLabel.place(x=5, y=100)

userEntry = ttk.Entry(rightFrame, width=30)
userEntry.place(x=150, y=110)

passLabel = Label(rightFrame, text="Password", font=(
    "Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
passLabel.place(x=5, y=150)

passEntry = ttk.Entry(rightFrame, width=30, show="🔏")
passEntry.place(x=150, y=160)


def Login():
    user = userEntry.get()
    passw = passEntry.get()

    dataBaser.cursor.execute("""
        SELECT * FROM Users 
        WHERE (User = ? and Password = ?) 
    """, (user, passw))

    verificacao = dataBaser.cursor.fetchone()
    try:
        if (user in verificacao and passw in verificacao):
            messagebox.showinfo(title="login info",
                                message="Acesso confirmado.Seja Bem Vindo")
            print("Logado com sucesso...🎉🎉🎉🎉")
    except:
        messagebox.showinfo(title="Login info",
                            message="Acesso Negado.Veja se esta cadastrado!!!")


# ======== Botões
loginButton = ttk.Button(rightFrame, text="login", width=30, command=Login)
loginButton.place(x=100, y=225)


def Register():
    # removendo widgets de loggin
    loginButton.place(x=5000)
    registerButton.place(x=5000)
    # Inserindo widgets de cadastro
    nomeLabel = Label(rightFrame, text="Name", font=(
        "Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
    nomeLabel.place(x=5, y=5)

    nomeEntry = ttk.Entry(rightFrame, width=30)
    nomeEntry.place(x=100, y=17)

    emailLabel = Label(rightFrame, text="Email", font=(
        "Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
    emailLabel.place(x=5, y=55)

    emailEntry = ttk.Entry(rightFrame, width=30)
    emailEntry.place(x=100, y=66)

    def registerToDataBase():
        name = nomeEntry.get()
        email = emailEntry.get()
        user = userEntry.get()
        password = passEntry.get()

        if (name == '' and email == '' and user == '' and password == ''):
            messagebox.showerror(title="Register Error",
                                 message="Preencha todos os campos")
        else:
            dataBaser.cursor.execute(""" 
            INSERT INTO Users (name, email, user, password) VALUES( ?, ?, ?, ?)
            """, (name, email, user, password))
            dataBaser.conn.commit()
            messagebox.showinfo(title="Register Info",
                                message="Conta criada com sucesso")

    register = ttk.Button(rightFrame, text="Register",
                          width=30, command=registerToDataBase)
    register.place(x=100, y=225)

    def BackToLogin():
        # removendo widgets de Cadastro
        nomeLabel.place(x=50000)
        nomeEntry.place(x=50000)
        emailLabel.place(x=50000)
        emailEntry.place(x=50000)
        register.place(x=50000)
        Back.place(x=50000)
        # trazendo de volta os widgets de login
        loginButton.place(x=100)
        registerButton.place(x=125)

    Back = ttk.Button(rightFrame, text="Back", width=20, command=BackToLogin)
    Back.place(x=125, y=260)


registerButton = ttk.Button(
    rightFrame, text="Register", width=30, command=Register)
registerButton.place(x=100, y=260)


jan.mainloop()
