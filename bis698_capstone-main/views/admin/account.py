import tkinter as tk
# from database import DB_Connection
from tkinter import messagebox,ttk
from controllers.customers import Customer
from controllers.utils import Utils
from views.user_password_change import PasswordChange
from views.users.user import AddUser
from views.customers.customer import CreateCustomer
from .reset_user_password import ResetUserPassword
from .unlock_user_account import UnlockUserAccount
from .login_activity import LoginActivity
from views.styles import Style

class Account():
    
    def __init__(self,parent,user_obj,admin_dashboard):

        self.parent = parent
        self.user = user_obj
        self.admin_dashboard = admin_dashboard

        

        
        self.users_customers_wrapper_frame = tk.Frame(master = self.parent)
        self.users_customers_wrapper_frame.pack(fill = "both",expand = True)

        self.user_title_frame = tk.Frame(master = self.users_customers_wrapper_frame)
        self.user_title_frame.grid(row = 0,column = 0,pady = 20)

        self.customer_title_frame = tk.Frame(master = self.users_customers_wrapper_frame)
        self.customer_title_frame.grid(row = 0,column = 1,pady = 20)


        # self.user_title_frame = tk.Frame(master = self.users_customers_wrapper_frame,bg = 'red')
        # self.user_title_frame.pack(fill = 'both', expand=True,side = 'left',padx = 50)

        # self.customer_title_frame = tk.Frame(master = self.users_customers_wrapper_frame,bg = 'blue')
        # self.customer_title_frame.pack(fill = 'both', expand=True,side = 'right',padx = 50)

        self.user_frame = tk.Frame(master = self.users_customers_wrapper_frame)
        self.user_frame.grid(row = 1,column = 0,padx = 130)

        self.customer_frame = tk.Frame(master = self.users_customers_wrapper_frame)
        self.customer_frame.grid(row = 1,column = 1,padx = 70)

        # self.user_frame = tk.Frame(master = self.users_customers_wrapper_frame)
        # self.user_frame.pack(fill = 'both', expand=True,side = 'left',padx = 50)

        # self.customer_frame = tk.Frame(master = self.users_customers_wrapper_frame)
        # self.customer_frame.pack(fill = 'both', expand=True,side = 'right',padx = 50)

        

        tk.Label(self.user_title_frame,text = "Users",font = Style.page_heading,fg = Style.page_heading_color).grid(row=0,column = 0)
        tk.Label(self.customer_title_frame,text = "Customers",font = Style.page_heading,fg = Style.page_heading_color).grid(row=0,column = 0)


        # ADD A NEW USER
        self.user_image = Utils.resize_image((50,50),'images/google/add-user.png')
        self.add_user_image = tk.Label(self.user_frame, image=self.user_image)
        self.add_user_image.grid(row = 0, column =0,padx = 10,pady = (20,0))
        self.add_user_image.bind("<Button-1>",self.on_add_user_click)

        self.add_user = tk.Label(self.user_frame,text = "Add User",font = Style.subheading,fg = Style.subheading_color,cursor = "hand2")
        self.add_user.grid(row=1,column = 0,padx = 10)
        self.add_user.bind("<Button-1>",self.on_add_user_click)
        text = ""
        # text = """Add users who have who have been hired to become employees of the company"""
        tk.Label(self.user_frame,text = text,font = Style.caption,wraplength=150).grid(row=2,column = 0)

  

        # RESET USER PASSWORD
        self.reset_image = Utils.resize_image((50,50),'images/google/rotation-lock.png')
        self.reset_user_image = tk.Label(self.user_frame, image=self.reset_image)
        self.reset_user_image.grid(row = 3, column =0, padx = 10, pady = (20,0))
        self.reset_user_image.bind("<Button-1>",self.on_reset_user_password_click)

        self.reset_user = tk.Label(self.user_frame,text = "Reset User Password",font = Style.subheading,fg = Style.subheading_color,cursor = "hand2")
        self.reset_user.grid(row=4,column = 0, padx = 10,)
        self.reset_user.bind("<Button-1>",self.on_reset_user_password_click)
        # text = """Add users who have who have been hired to become employees of the company"""
        tk.Label(self.user_frame,text = text,font = Style.caption,wraplength=150).grid(row=5,column = 0)




        # LOCK USER PASSWORD
        self.unlock_image = Utils.resize_image((50,50),'images/google/unlock.png')
        self.unlock_user_image = tk.Label(self.user_frame, image=self.unlock_image)
        self.unlock_user_image.grid(row = 6, column =0, padx = 10,pady = (20,0))
        self.unlock_user_image.bind("<Button-1>",self.on_unlock_user_click)

        self.unlock_user = tk.Label(self.user_frame,text = "Unlock User",font = Style.subheading,fg = Style.subheading_color,cursor = "hand2")
        self.unlock_user.grid(row=7,column = 0,padx = 10)
        self.unlock_user.bind("<Button-1>",self.on_unlock_user_click)
        # text = """Add users who have who have been hired to become employees of the company"""
        tk.Label(self.user_frame,text = text,font = Style.caption,wraplength=150).grid(row=8,column = 0)



    #     self.unlock_image = Utils.resize_image((30,30),'images/rotation-lock.png')
    #     # Create a Label widget with the resized image
    #     self.reset_user_password_image = tk.Label(self.parent, image=self.reset_image)
    #     self.reset_user_password_image.grid(row = 5, column =0,pady = 20, padx = 20,sticky="E")

    #     self.reset_user_label = tk.Label(parent,text="Reset User Password",font = ('helvetica', 12),cursor = "hand2")
    #     self.reset_user_label.grid(row = 5, column =1,padx = 10,sticky='W')
    #     self.reset_user_label.bind("<Button-1>",self.on_reset_user_password_click)


    #     # UNLOCK A USER ACCOUNT
    #     self.unlock_image = Utils.resize_image((30,30),'images/unlocked.png')
    #     # Create a Label widget with the resized image
    #     self.unlock_user_password_image = tk.Label(self.parent, image=self.unlock_image)
    #     self.unlock_user_password_image.grid(row = 6, column =0,pady = 20, padx = 20,sticky="E")

    #     self.unlock_user_label = tk.Label(self.parent,text="Unlock User Account",font = ('helvetica', 12),cursor = "hand2")
    #     self.unlock_user_label.grid(row = 6, column =1,padx = 10,sticky='W')
    #     self.unlock_user_label.bind("<Button-1>",self.on_unlock_user_account_click)



    #     # LOGIN ACTIVITIES
    #     self.login_image = Utils.resize_image((30,30),'images/clock.png')
    #     # Create a Label widget with the resized image
    #     self.login_activities_image = tk.Label(self.parent, image=self.login_image)
    #     self.login_activities_image.grid(row = 7, column =0,pady = 20, padx = 20,sticky="E")

    #     self.login_activities_label = tk.Label(self.parent,text="Users Login Activities",font = ('helvetica', 12),cursor = "hand2")
    #     self.login_activities_label.grid(row = 7, column =1,padx = 10,sticky='W')
    #     self.login_activities_label.bind("<Button-1>",self.on_login_activities_click)



        #ADD CUSTOMER
        self.cus_image = Utils.resize_image((50,50),'images/google/add-customer.png')
        self.add_customer_image = tk.Label(self.customer_frame, image=self.cus_image)
        self.add_customer_image.grid(row = 0, column =0,padx = 10,pady = (20,0))
        self.add_customer_image.bind("<Button-1>",self.on_add_customer_click)

        self.add_customer = tk.Label(self.customer_frame,text = "Add Customer",font = Style.subheading,fg = Style.subheading_color)
        self.add_customer.grid(row=1,column = 0,padx = 10)
        self.add_customer.bind("<Button-1>",self.on_add_customer_click)
        # text = """Add customers who have signed contracts and are ready to join the system"""
        tk.Label(self.customer_frame,text = text,font = Style.caption,wraplength=150).grid(row=2,column = 0)


        # EDIT CUSTOMER
        self.edit_image = Utils.resize_image((50,50),'images/google/edit.png')
        self.edit_customer_image = tk.Label(self.customer_frame, image=self.edit_image)
        self.edit_customer_image.grid(row = 3, column =0,pady = (20,0), padx = 10)
        self.edit_customer_image.bind("<Button-1>",self.on_edit_customer_click)

        self.edit_user = tk.Label(self.customer_frame,text = " Edit Customer",font = Style.subheading,fg = Style.subheading_color,cursor = "hand2")
        self.edit_user.grid(row=4,column = 0,padx = 10)
        self.edit_user.bind("<Button-1>",self.on_view_customer_click)
        # text = """Add users who have who have been hired to become employees of the company"""
        tk.Label(self.customer_frame,text = text,font = Style.caption,wraplength=150).grid(row=5,column = 0)



        # VIEW CUSTOMER
        self.view_image = Utils.resize_image((50,50),'images/google/view.png')
        self.view_customer_image = tk.Label(self.customer_frame, image=self.view_image)
        self.view_customer_image.grid(row = 6, column =0,pady = (20,0), padx = 10)
        self.view_customer_image.bind("<Button-1>",self.on_view_customer_click)

        self.view_user = tk.Label(self.customer_frame,text = " View Customer",font = Style.subheading,fg = Style.subheading_color,cursor = "hand2")
        self.view_user.grid(row=7,column = 0,padx = 10)
        self.view_user.bind("<Button-1>",self.on_view_customer_click)
        # text = """Add users who have who have been hired to become employees of the company"""
        tk.Label(self.customer_frame,text = text,font = Style.caption,wraplength=150).grid(row=8,column = 0)



    #     #LOGOUT 
    #     self.lg_image = Utils.resize_image((30,30),'images/logout.png')
    #     # Create a Label widget with the resized image
    #     self.logout_image = tk.Label(self.parent, image=self.lg_image)
    #     self.logout_image.grid(row = 3, column =3,pady = 20, padx = 20,sticky="E")
    #     self.logout_label = tk.Label(parent, text="Logout",font = ('helvetica', 10) ,cursor = "hand2")
    #     self.logout_label.grid(row = 3, column =4 ,padx = 10,sticky='E')
    #     self.logout_label.bind("<Button-1>",self.on_logout_label_click)
    #     tk.Button(parent,text="Logout", command=self.logout).grid(row =10,column =6,padx=20,pady=60,sticky='SE')
        

       

    # def on_logout_label_click(self,event):
    #     result = messagebox.askyesno("Question","Are you sure you want to log out?")
    #     if result:
    #         #call the logout function in the user_dashboard
    #         self.admin_dashboard.logout()


    def on_add_user_click(self,event):
        add_user_window = tk.Toplevel(self.parent)
        AddUser(add_user_window)

    def on_reset_user_password_click(self,event):
        reset_user_password_window = tk.Toplevel(self.parent)
        ResetUserPassword(reset_user_password_window)
       




    def on_add_customer_click(self,event):
        create_customer_window = tk.Toplevel(self.parent)
        CreateCustomer(create_customer_window)


    def on_edit_customer_click(self,event):
        pass

    def on_unlock_user_click(self,event):
        unlock_user_account_window = tk.Toplevel(self.parent)
        UnlockUserAccount(unlock_user_account_window)


    def on_view_customer_click(self,event):
        pass

    # def on_login_activities_click(self,event):
    #     login_activities_window = tk.Toplevel(self.parent)
    #     LoginActivity(login_activities_window)

    # def logout(self):
    #     self.admin_dashboard.logout()
       
