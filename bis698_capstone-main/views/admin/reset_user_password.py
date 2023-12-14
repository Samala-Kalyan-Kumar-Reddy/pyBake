import tkinter as tk
from controllers.users import User
from controllers.utils import Utils
from views.styles import Style
from tkinter import messagebox
from werkzeug.security import generate_password_hash,check_password_hash





class ResetUserPassword(tk.Toplevel):
    def __init__(self, root):
        self.root = root
        self.root.title("Reset User Password")
        # self.root.geometry("300x250")

        self.password_reset_frame = tk.Frame(master = self.root)
        self.password_reset_frame.pack(fill = 'x',padx = 20,pady = 20)

        self.p_reset_image = Utils.resize_image((30,30),'images/google/rotation-lock.png')
        self.pass_reset_image = tk.Label(self.password_reset_frame, image=self.p_reset_image)
        self.pass_reset_image.grid(row =0,column =1,sticky='e')
        
        tk.Label(self.password_reset_frame, text="Reset User",font = Style.subheading,fg = Style.page_heading_color).grid(row = 0, column =0,sticky = 'w')
    


        self.reset_message = tk.Label(self.password_reset_frame, text="")
        self.reset_message.grid(row = 1, column =0, columnspan = 2)

        tk.Label(self.password_reset_frame, text="Select User" ).grid(row = 2, column =0,sticky = 'w')
        self.user_email_entry = tk.Entry(self.password_reset_frame)
        self.user_email_entry.grid(row = 3, column = 0,pady=10)

        self.reset_button = tk.Button(self.password_reset_frame,text = "Reset Password",command = self.reset_user_password)
        self.reset_button.grid(row=3, column=1,padx=10,pady =10)

       




    def reset_user_password(self):
        self.user = User(email = self.user_email_entry.get())
       
        status,message = self.user.reset_password()
        if status == 'failure':
            self.reset_message.config(text = message,fg = 'red')
        elif status == 'success':
            messagebox.showinfo('success',message)
            self.root.destroy()
