import tkinter as tk
# from database import DB_Connection
from tkinter import messagebox,ttk
from controllers.customers import Customer
from controllers.utils import Utils
from .user_password_change import PasswordChange

class ManageUsers():
    
    def __init__(self,parent,user_obj,user_dashboard):

        self.parent = parent
        self.user = user_obj
        self.user_dashboard = user_dashboard

        

        
        self.tk_image = Utils.resize_image((100,100),'images/user.png')
        # Create a Label widget with the resized image
        self.user_image = tk.Label(self.parent, image=self.tk_image)
        self.user_image.grid(row = 0, column =3,pady = 20, padx = 20,sticky="E")

        self.user_label = tk.Label(self.parent, text="User Profile",font= ('Helvetica',18),foreground ='#008fd3')
        self.user_label.grid(row = 0, column = 0, padx=20, pady=10)

        tk.Label(parent, text=f"{user_obj['firstname'].capitalize()} {user_obj['lastname'].capitalize()}",font = ('helvetica', 15)).grid(row = 1, column = 3,sticky='E')
        tk.Label(parent, text=f"Status: {user_obj['status']}",font = ('helvetica', 9)).grid(row = 2, column = 3,sticky='WE')

        # tk.Label(parent, text="Email:",font = ('helvetica', 12)).grid(row = 2, column = 0,sticky='E')
        # self.email_entry = tk.Entry(self.parent,font = ('helvetica', 11))
        # self.email_entry.grid(row = 2, column = 1,padx=20,pady=20,sticky='W')

        #CHANGE PASSWORD
        self.pass_image = Utils.resize_image((30,30),'images/reset-password.png')
        # Create a Label widget with the resized image
        self.password_image = tk.Label(self.parent, image=self.pass_image)
        self.password_image.grid(row = 3, column =0,pady = 20, padx = 10,sticky="E")

        self.change_password_label = tk.Label(parent, text="Change Password",font = ('helvetica', 10),cursor = "hand2")
        self.change_password_label.grid(row = 3, column =1,padx = 10,sticky='E')
        self.change_password_label.bind("<Button-1>",self.on_change_password_click)
        # self.address_entry = tk.Entry(self.parent,font = ('helvetica', 11))
        # self.address_entry.grid(row = 2, column = 3, padx = 20,pady=20)


        #CHANGE LOGOUT
        self.lg_image = Utils.resize_image((30,30),'images/logout.png')
        # Create a Label widget with the resized image
        self.logout_image = tk.Label(self.parent, image=self.lg_image)
        self.logout_image.grid(row = 3, column =3,pady = 20, padx = 10,sticky="E")
        self.logout_label = tk.Label(parent, text="Logout",font = ('helvetica', 10) ,cursor = "hand2")
        self.logout_label.grid(row = 3, column =4 ,padx = 10,sticky='E')
        self.logout_label.bind("<Button-1>",self.on_logout_label_click)
        tk.Button(parent,text="Logout", command=self.logout).grid(row =10,column =6,padx=20,pady=60,sticky='SE')
        

       

        # self.save_button = tk.Button(self.parent, text="Save Customer",background="#08A04B",font = ('helvetica', 10),fg="white",width= 15, command=self.save_customer)
        # self.save_button.grid(row = 6, column = 2, sticky='E',padx = 20,pady = 80,)

        # self.clear_button = tk.Button(self.parent, text="Clear Form",background="#008FD3",font = ('helvetica', 10),fg="white",width= 15,command=self.clear_customer_create_form)
        # self.clear_button.grid(row = 6, column = 3, padx=20, sticky='E',pady = 80)


        # self.logout_button = tk.Button(self.parent,text="Logout", command=self.logout)
        # self.logout_button.grid(row =0,column =0,sticky='E')
    def on_logout_label_click(self,event):
        result = messagebox.askyesno("Question","Are you sure you want to log out?")
        if result:
            #call the logout function in the user_dashboard
            self.user_dashboard.logout()


    def on_change_password_click(self,event):
        change_password_window = tk.Toplevel(self.parent)
        PasswordChange(change_password_window,self.user)
       

    def logout(self):
        self.user_dashboard.logout()
       
        
# if __name__ == "__main__":
#     root = tk.Tk()
#     create_customer_window = tk.Toplevel(root)
#     CreateCustomer(create_customer_window)
#     root.mainloop()
