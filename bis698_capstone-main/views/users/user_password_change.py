from hashlib import new
import tkinter as tk
# from .customer import CreateCustomer
import views.authentication as authentication
from database import DB_Connection
from controllers.utils import Utils
from controllers.users import User
from tkinter import messagebox


util_object = Utils()
class PasswordChange(tk.Toplevel):
    def __init__(self, root,user):
        self.root = root
        self.user = user
        self.new_password = ""
        self.root.title("Change Password")
        # self.root.geometry("")


        self.old_password = self.user['password']
        self.email = self.user['email']
        self.auth_frame = tk.LabelFrame(self.root,text=f"{self.user.get('firstname').capitalize()} {self.user.get('lastname').capitalize()}")
        self.auth_frame.grid(row=0,column = 0, rowspan = 5, columnspan = 5, padx = 40, pady = 15)

       #old pasword
        self.old_pwd_label = tk.Label(self.auth_frame, text="Old Password:")
        self.old_pwd_label.grid(row = 0, column = 0,padx = 5)
        self.old_pwd_entry = tk.Entry(self.auth_frame,width=30,show = "*")
        self.old_pwd_entry.grid(row = 0,column = 1,padx = 20, pady = (20,0),sticky='w')
        self.old_pwd_message = tk.Label(self.auth_frame,text = "",fg="red")
        self.old_pwd_message.grid(row = 1,column = 1,pady=0)


        #new password
        self.new_pwd_label = tk.Label(self.auth_frame, text="New Password:")
        self.new_pwd_label.grid(row = 2, column = 0,padx = 5)
        self.new_pwd_entry = tk.Entry(self.auth_frame,width=30,show = "*")
        self.new_pwd_entry.grid(row = 2,column = 1,padx = 20, pady = (20,0),sticky='w')
        self.new_pwd_message = tk.Label(self.auth_frame,text = "",fg="red")
        self.new_pwd_message.grid(row = 3,column = 1,pady=0)
        
       
        #new password
        self.confirm_pwd_label = tk.Label(self.auth_frame, text="Confirm Password:")
        self.confirm_pwd_label.grid(row = 4, column = 0,padx = 5)
        self.confirm_pwd_entry = tk.Entry(self.auth_frame,width=30,show = "*")
        self.confirm_pwd_entry.grid(row = 4,column = 1,padx = 20, pady = (20,0),sticky='w')
        self.pwd_error_message = tk.Label(self.auth_frame,text = "",fg="red")
        self.pwd_error_message.grid(row = 5,column = 1,pady=0)


        self.change_pwd_button = tk.Button(self.auth_frame,width = 25, text="Change Password",command=self.change_password)
        self.change_pwd_button.grid(row = 6, column = 1,padx = 5, pady=10)


        
#change password logic here       
    def change_password(self):
        old_password = self.old_pwd_entry.get()
        new_password = self.new_pwd_entry.get()
        confirm_password = self.confirm_pwd_entry.get()

        self.user_obj = User()
        message = self.user_obj.change_password(self.user['email'],old_password,new_password,confirm_password)
        if message !=  "Password changed successfully!":
            self.pwd_error_message.config(text = message)
        else:
            messagebox.showinfo('Password Change',message)
            self.root.destroy()


       



     