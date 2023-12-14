import tkinter as tk
# from database import DB_Connection
from tkinter import messagebox,ttk
from controllers.customers import Customer
from controllers.utils import Utils
from views.user_password_change import PasswordChange
from views.orders.create_order import CreateOrder
from views.orders.update_order import UpdateOrder
from views.styles import Style
# from .reset_user_password import ResetUserPassword
# from .unlock_user_account import UnlockUserAccount
# from .login_activity import LoginActivity

class Order():
    
    def __init__(self,parent,user_obj,dashboard):

        self.parent = parent
        self.user = user_obj
        self.dashboard = dashboard


        self.order_title = tk.Frame(master = self.parent,bg='#EEEEEE')
        self.order_title.pack(fill = 'both', expand = True,side = 'top')

        self.order_section = tk.Frame(master = self.parent,bg='#EEEEEE')
        self.order_section.pack(fill = 'both', expand = True,side = 'top')



        tk.Label(self.order_title, text = "Manage Orders",font = Style.page_heading,fg = Style.page_heading_color).grid(row = 0,column = 0,padx = 20, pady = 20)
        # CREATE A NEW ORDER
        self.order_image = Utils.resize_image((70,70),'images/order/shopping-bag.png')
        # Create a Label widget with the resized image
        self.order_create_image = tk.Label(self.order_section, image=self.order_image,cursor = "hand2")
        self.order_create_image.grid(row = 0, column =0)

        self.order_create_label = tk.Label(self.order_section, text="Create Order", font = Style.subheading,cursor = "hand2")
        self.order_create_label.grid(row = 1, column =0,pady=(0,200))
        self.order_create_label.bind("<Button-1>",self.on_order_create_click)
        self.order_create_image.bind("<Button-1>",self.on_order_create_click)

         # EDIT EXISTING ORDER
        self.ord_edit_image = Utils.resize_image((70,70),'images/order/checklist.png')
        # Create a Label widget with the resized image
        self.order_edit_image = tk.Label(self.order_section, image=self.ord_edit_image)
        self.order_edit_image.grid(row = 0, column =1)

        self.order_edit_label = tk.Label(self.order_section, text="Edit Customer Order", font = Style.subheading,cursor = "hand2")
        self.order_edit_label.grid(row = 1, column =1,pady=(0,200))
        self.order_edit_label.bind("<Button-1>",self.on_order_edit_click)
        self.order_edit_image.bind("<Button-1>",self.on_order_edit_click)

        # UPDATE ORDER
        self.ord_update_image = Utils.resize_image((70,70),'images/order/product-chain.png')
        # Create a Label widget with the resized image
        self.order_update_status_image = tk.Label(self.order_section, image=self.ord_update_image)
        self.order_update_status_image.grid(row = 0, column =2)

        self.order_update_status_label = tk.Label(self.order_section, text="Update Order Status", font = Style.subheading,cursor = "hand2")
        self.order_update_status_label.grid(row = 1, column =2,pady=(0,200))
        self.order_update_status_label.bind("<Button-1>",self.on_order_update_click)
        self.order_update_status_image.bind("<Button-1>",self.on_order_update_click)


        for column in range(3):  # Assuming you have 8 columns in the grid
            self.order_section.grid_columnconfigure(column, weight=1)



        # for widget in self.order_section.winfo_children():
        #     widget.grid_configure(padx = 20)
    #   # EDIT EXISTING ORDER
    #     self.reset_image = Utils.resize_image((30,30),'images/rotation-lock.png')
    #     # Create a Label widget with the resized image
    #     self.reset_user_password_image = tk.Label(self.parent, image=self.reset_image)
    #     self.reset_user_password_image.grid(row = 5, column =0,pady = 20, padx = 20,sticky="E")

    #     self.reset_user_label = tk.Label(parent,text="Edit Order",font = ('helvetica', 12),cursor = "hand2")
    #     self.reset_user_label.grid(row = 5, column =1,padx = 10,sticky='W')
    #     self.reset_user_label.bind("<Button-1>",self.on_reset_user_password_click)


    #     # REVIEW AND CONFIRM ORDER
    #     self.unlock_image = Utils.resize_image((30,30),'images/unlocked.png')
    #     # Create a Label widget with the resized image
    #     self.unlock_user_password_image = tk.Label(self.parent, image=self.unlock_image)
    #     self.unlock_user_password_image.grid(row = 6, column =0,pady = 20, padx = 20,sticky="E")

    #     self.unlock_user_label = tk.Label(self.parent,text="Review & Confirm Order",font = ('helvetica', 12),cursor = "hand2")
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


    def on_order_create_click(self,event):
        create_order_window = tk.Toplevel(self.parent)
        CreateOrder(create_order_window,self.user,self.dashboard)


    def on_order_edit_click(self,event):
        pass


    def on_order_update_click(self,event):
        update_order_window = tk.Toplevel(self.parent)
        UpdateOrder(update_order_window,self.user,self.dashboard)

    # def on_rese_user_password_click(self,event):
    #     reset_user_password_window = tk.Toplevel(self.parent)
    #     ResetUserPassword(reset_user_password_window)
       

    # def on_unlock_user_account_click(self,event):
    #     unlock_user_account_window = tk.Toplevel(self.parent)
    #     UnlockUserAccount(unlock_user_account_window)

    # def on_login_activities_click(self,event):
    #     login_activities_window = tk.Toplevel(self.parent)
    #     LoginActivity(login_activities_window)

    # def logout(self):
    #     self.admin_dashboard.logout()
       
        
# if __name__ == "__main__":
#     root = tk.Tk()
#     create_customer_window = tk.Toplevel(root)
#     CreateCustomer(create_customer_window)
#     root.mainloop()
