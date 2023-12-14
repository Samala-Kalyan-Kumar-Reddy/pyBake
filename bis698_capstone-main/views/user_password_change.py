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
        self.root.resizable(False,False)
        # self.root.geometry("")

        self.show_password_var = tk.IntVar()


        self.old_password = self.user['password']
        self.email = self.user['email']
        self.auth_frame = tk.LabelFrame(self.root,text=f"Change Password for {self.user.get('firstname').capitalize()} {self.user.get('lastname').capitalize()}",font =('Arial',15),borderwidth = 1,relief = tk.FLAT)
        self.auth_frame.pack(pady = 20,padx = 20)

       #old pasword
        self.old_pwd_label = tk.Label(self.auth_frame, text="Old Password: ")
        self.old_pwd_label.grid(row = 0, column = 0,sticky = 'e',pady = (20,0))
        self.old_pwd_entry = tk.Entry(self.auth_frame,width=25,show = "*")
        self.old_pwd_entry.grid(row = 0,column = 1,sticky='w',pady = (20,0))
        self.old_pwd_message = tk.Label(self.auth_frame,text = "",fg="red")
        self.old_pwd_message.grid(row = 1,column = 1,pady=0)


        #new password
        self.new_pwd_label = tk.Label(self.auth_frame, text="New Password: ")
        self.new_pwd_label.grid(row = 2, column = 0,padx = 5,sticky = 'e')
        self.new_pwd_entry = tk.Entry(self.auth_frame,width=25,show = "*")
        self.new_pwd_entry.grid(row = 2,column = 1,sticky='w')
        self.new_pwd_message = tk.Label(self.auth_frame,text = "",fg="red")
        self.new_pwd_message.grid(row = 3,column = 1,pady=0)
        
       
#new password
        self.confirm_pwd_label = tk.Label(self.auth_frame, text="Confirm Password: ")
        self.confirm_pwd_label.grid(row = 4, column = 0,padx = 5,sticky = 'e')
        self.confirm_pwd_entry = tk.Entry(self.auth_frame,width=25,show = "*")
        self.confirm_pwd_entry.grid(row = 4,column = 1,sticky='w')
        self.pwd_error_message = tk.Label(self.auth_frame,text = "",fg="red")
        self.pwd_error_message.grid(row = 5,column = 1,pady=0)


        self.show_password_checkbox = tk.Checkbutton(self.auth_frame, text="Show Password", variable=self.show_password_var, command=self.show_password)
        self.show_password_checkbox.grid(row = 6, column = 1,sticky='e',pady = (0,10))


        self.change_pwd_button = tk.Button(self.auth_frame, text="Change Password",command=self.change_password)
        self.change_pwd_button.config(bg = 'green')
        self.change_pwd_button.grid(row = 7, column = 1,sticky = 'e')

        self.reset_button = tk.Button(self.auth_frame,text="Reset",command=self.reset_form)
        self.reset_button.grid(row = 7, column = 1,sticky = 'w')

        
#change password logic here       
    def change_password(self):
        old_password = self.old_pwd_entry.get()
        new_password = self.new_pwd_entry.get()
        confirm_password = self.confirm_pwd_entry.get()

        self.user = User(email=self.email,password=self.old_password)
        message = self.user.change_password(new_password,confirm_password)
        if message !=  "Password changed successfully!":
            self.pwd_error_message.config(text = message)
        else:
            messagebox.showinfo('Password Change',message)
            self.root.destroy()


    def reset_form(self):
        self.old_pwd_entry.delete(0,'end')
        self.new_pwd_entry.delete(0,'end')
        self.confirm_pwd_entry.delete(0,'end')



    def show_password(self):
        if self.show_password_var.get():
            self.old_pwd_entry.config(show="")
            self.new_pwd_entry.config(show="")
            self.confirm_pwd_entry.config(show="")
        else:

            self.old_pwd_entry.config(show="*")
            self.new_pwd_entry.config(show="*")
            self.confirm_pwd_entry.config(show="*")




       



     