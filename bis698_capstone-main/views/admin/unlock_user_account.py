import tkinter as tk
from controllers.users import User
from controllers.utils import Utils
from views.styles import Style
from tkinter import messagebox
from werkzeug.security import generate_password_hash,check_password_hash





class UnlockUserAccount(tk.Toplevel):
    def __init__(self, root):
        self.root = root
        self.root.title("Unlock User Account")
        # self.root.geometry("300x250")
        self.user = User()

        self.account_unlock_frame = tk.Frame(master = self.root)
        self.account_unlock_frame.pack(fill = 'x',padx = 20,pady = 20)

        self.a_unlock_image = Utils.resize_image((30,30),'images/google/unlock.png')
        self.acct_unlock_image = tk.Label(self.account_unlock_frame, image=self.a_unlock_image)
        self.acct_unlock_image.grid(row =0,column =1,sticky='e')
        
        tk.Label(self.account_unlock_frame, text="Lock/Unlock User",font = Style.subheading,fg = Style.page_heading_color).grid(row = 0, column =0,sticky = 'w')
    


        self.unlock_message = tk.Label(self.account_unlock_frame, text="")
        self.unlock_message.grid(row = 1, column =0,columnspan = 2)

        tk.Label(self.account_unlock_frame, text="Select User" ).grid(row = 2, column =0,sticky = 'w')
        self.user_email_entry = tk.Entry(self.account_unlock_frame)
        self.user_email_entry.grid(row = 3, column = 0,pady=10)

        self.unlock_button = tk.Button(self.account_unlock_frame,text = "Lock/Unlock",command = self.unlock_user_account)
        self.unlock_button.grid(row=3, column=1,padx=10,pady =10)



    def unlock_user_account(self):
        self.user.get_locked_users()
        self.user_email = self.user_email_entry.get()
        status,message = self.user.unlock_user_account(self.user_email)
        if status == 'failure':
            self.unlock_message.config(text = message,fg = 'red')
        elif status == 'success':
            messagebox.showinfo('success',message)
            self.root.destroy()


