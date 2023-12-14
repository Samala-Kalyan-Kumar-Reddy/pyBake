import tkinter as tk
from controllers.users import User
from tkinter import messagebox
from werkzeug.security import generate_password_hash,check_password_hash





class LoginActivity(tk.Toplevel):
    def __init__(self, root):
        self.root = root
        self.root.title("User Login Activities")
        # self.root.geometry("300x250")
        self.user = User()

        tk.Label(self.root, text=f"Users Login Activities{self.user.email}").pack()
        tk.Button(self.root,text = "get activities",command = self.get_login_activities).pack()

        self.scrollbar = tk.Scrollbar(root)
        self.scrollbar.pack(pady = 10,padx = 10, side = tk.RIGHT,fill = tk.Y)


        self.listbox = tk.Listbox(root,borderwidth = 0,width = 30, yscrollcommand=self.scrollbar.set)
        self.listbox.pack(ipadx = 10, ipady = 10, padx= 20,pady =20,fill=tk.BOTH, expand=True)
        # 

        self.scrollbar.config(command=self.listbox.yview)

        # Add items to the Listbox
       


        for user_login_info in self.get_login_activities():
            print(user_login_info)
            self.listbox.insert( tk.END, f"{user_login_info[0]} | {user_login_info[1]} | {user_login_info[2]}")


    def get_login_activities(self):
        result = self.user.get_users_login_info()
        return result

