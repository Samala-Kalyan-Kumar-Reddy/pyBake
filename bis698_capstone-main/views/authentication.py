import tkinter as tk
from .user_password_change import PasswordChange

# import ttkbootstrap as tb

# from ttkbootstrap import Style


from views.users.user_dashboard import UserDashboard 
from views.admin.admin_dashboard import AdminDashboard
from views.users.manager_dashboard import ManagerDashboard
from views.styles import Style

from controllers.users import User
from tkinter import messagebox
from config import Config
from datetime import datetime
from controllers.utils import Utils
from views.styles import Style
# from werkzeug.security import generate_password_hash

class AuthenticationScreen:
    def __init__(self, root):
        self.root = root
        self.user = {}
        self.root.title("User Login")
        self.root.resizable(False, False)
        self.utils = Utils()
        
        
        


        self.show_password_var = tk.IntVar()
        
        


        

        self.auth_title_frame = tk.Frame(self.root)
        self.auth_title_frame.pack(padx = 20)


        self.auth_frame = tk.Frame(self.root)
        self.auth_frame.pack(padx = 20)

        self.auth_button_frame = tk.Frame(self.root)
        self.auth_button_frame.pack(padx = 20,pady = (20,50))



        login_text = "Sign In"
        self.login_title = tk.Label(self.auth_title_frame,text=login_text,fg=Style.page_heading_color,font = Style.page_heading)
        self.login_title.grid(row=0,column =0, padx = (0,20),sticky="W")

        self.tk_image = Utils.resize_image((70,70),'images/account.png')
        # Create a Label widget with the resized image
        self.customer_image = tk.Label(self.auth_title_frame, image=self.tk_image)
        self.customer_image.grid(row = 0, column =1,pady = (10,0), padx = 20,sticky="E")
    

        self.auth_form_message = tk.Label(self.auth_title_frame,font = ('helvetica',12),fg="red")
        self.auth_form_message.grid(row = 1,column = 1, columnspan= 2,pady=(10,0))



       
        self.email_label = tk.Label(self.auth_frame, text="Username:")
        self.email_label.grid(row = 0, column = 0,padx = 5,sticky='E')
        self.email_entry = tk.Entry(self.auth_frame,width = 22)
        self.email_entry.grid(row = 0,column = 1,padx = 20, pady =10,sticky='W')
        


       

        self.password_label = tk.Label(self.auth_frame, text="Password:")
        self.password_label.grid(row =1, column = 0,padx = 5, ipady =5,sticky='E')
        self.password_entry = tk.Entry(self.auth_frame,width = 22,show="*")
        self.password_entry.grid(row =1, column = 1,padx=20,pady=10,sticky='E')
        # self.form_password_message = tk.Label(self.auth_frame,text = "",font = ('helvetica',9),fg="red")
        # self.form_password_message.grid(row = 4,column = 1,pady=0)

        self.show_password_checkbox = tk.Checkbutton(self.auth_frame, text="Show Password", variable=self.show_password_var, command=self.show_password)
        self.show_password_checkbox.grid(row = 2, column = 1,sticky='e',padx=20)

  

        self.login_button = tk.Button(self.auth_button_frame,text="Login",bg="#08A04B",width = 10, fg="black",command=self.authenticate)
        self.login_button.grid(row = 0, column = 0)
        self.login_button.config(bg = "#006064")

        self.reset_button = tk.Button(self.auth_button_frame,text="Reset",bg="#008FD3",width = 10, fg="black",command=self.reset_form)
        self.reset_button.grid(row = 0, column = 1)
       


        # self.login_message_frame = tk.LabelFrame(self.auth_frame,borderwidth=1)
        # self.login_message_frame.grid(row=6,column = 1, rowspan = 6, columnspan = 3)

        login_text = """Please enter a valid email address and password.\nPassword must be at least 8 characters"""
        self.login_text = tk.Label(self.auth_frame,text=login_text, \
                                    font = ('helvetica',11),justify="left")
        # self.login_text.grid(row=6,column =1)
      
        # Style.center_window(self.root) 

       

    def authenticate(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        user_obj = User(email = email,password=password)
        
        result = user_obj.authenticate_user()
        if len(result) == 2:
            auth_status,message = result
        else:
            auth_status,message,user = result

        if auth_status == "invalid_email":
            self.auth_form_message.config(text=message,bg = "#FFEBEE")
        elif auth_status == 'invalid_password':
            self.auth_form_message.config(text = message)

        elif auth_status == "change_password":
            response = messagebox.askyesno('Confirmation','Password change is required! Do you wish to proceed or cancel?')
            if response:
                self.user = user
                self.open_change_password()

        elif auth_status == 'authenticated':
            self.open_dashboard(user['role'],user)
            
       
        
        # #check if email matches email pattern
        # if self.utils.check_email_pattern(email):
        #     if self.utils.check_password_length(password):
        #         user_object = User()
        #         # password = generate_password_hash(password)
        #         user = user_object.authenticate(email,password)
        #         if user:
        #             #check if the user is logging for the first time
        #             if not user_object.is_active(email):
        #                 response = messagebox.askyesno('Confirmation','Password change is required! Do you wish to proceed or cancel?')
        #                 if response:
        #                     self.user = user
        #                     self.open_change_password()
        #                 else:
        #                     self.root.destroy()
        #                 #redirect user to login page 
        #             else:
        #                 self.open_dashboard(user['role_name'],user)

        #         else:
        #             messagebox.showerror("Error", "Invalid email or password")
        #     else:
        #         message = "password must be 8 characters or more"
        #         self.form_password_message.config(text = message)
        # else:
        #     message = "email must be a valid email"
        #     self.form_email_message.config(text=message)
       

   
   
    def open_dashboard(self, role,user):
        self.root.destroy()
        
        if role == "admin":
            root = tk.Tk()
            AdminDashboard(root,user)
            # import logging
            # logging.info(f"Admin user {user.get('email')} successfully logged in at {datetime.now()}")
            root.mainloop()

        elif role =='manager' :
            root = tk.Tk()
            # AdminDashboard(root)
            ManagerDashboard(root,user)
            # logging.info(f"Standard user {user.get('email')} successfully logged in at {datetime.now}")
            root.mainloop()
            

        elif role == 'sales associate':
            root = tk.Tk()
            # AdminDashboard(root)
            UserDashboard(root,user)
            # logging.info(f"Standard user {user.get('email')} successfully logged in at {datetime.now}")
            root.mainloop()


    def open_change_password(self):
        change_password_window = tk.Toplevel(self.root)
        PasswordChange(change_password_window,self.user)


    def reset_form(self):
        self.email_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.auth_form_message.config(text = "")


    def show_password(self):
        if self.show_password_var.get():
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")



          

    # def logout(self):
    #     self.root.destroy()
    #     #save the logout timestamp in the database
    #     self.utils.track_login_logout('logout', self.user['email'],datetime.now())
    #     import logging
    #     logging.info(f"{self.user.get('email')} successfully logged out at {datetime.now()}")
    #     # Create a new authentication screen
    #     auth_screen = AuthenticationScreen(tk.Tk())
    #     auth_screen.root.mainloop()
