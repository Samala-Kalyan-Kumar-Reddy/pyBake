
import tkinter as tk
from tkinter import ttk
from ..customers.customer import CreateCustomer
from ..orders.orders import Order
from .user_profile import UserProfile
# from .user_profile import UserProfile
import views.authentication as authentication
from controllers.utils import Utils
from datetime import datetime

class UserDashboard:
    def __init__(self,root,user_obj):
        self.root = root
        self.user = user_obj
        self.root.title("User Dashboard")
        self.root.minsize(760,480)
        self.root.maxsize(900,550)
        self.utils = Utils()
        # Create a Notebook
        self.tab_control = ttk.Notebook(self.root)
        self.tab_control.pack(expand=1, fill="both", side="left")

        # Create Frames for Tabs
        self.frame1 = ttk.Frame(self.tab_control)
        self.frame2 = ttk.Frame(self.tab_control)
        self.frame3 = ttk.Frame(self.tab_control)

        # Add Frames to the Notebook with Tab Names
        self.tab_control.add(self.frame1, text="Manage Profile")
        self.tab_control.add(self.frame2, text="Create Customers")
        self.tab_control.add(self.frame3, text="Manage Orders")


        # Create content for Tab 1
        self.create_customer = CreateCustomer(self.frame2)
       
    
        self.manage_profile = UserProfile(self.frame1,user_obj=self.user, user_dashboard = self)
        self.manage_orders = Order(self.frame3,user_obj = self.user,dashboard = self)

        # Show the initial frame (Tab 1)
        self.frame1.lift()

    
    #log out the current user
    def logout(self):
        from ..authentication import AuthenticationScreen
        # Close the current window
        self.root.destroy()
        import logging
        logging.info(f"User {self.user.get('email') } logged out at {datetime.now()}")
        # Create a new authentication screen
        auth_screen = AuthenticationScreen(tk.Tk())
        auth_screen.root.mainloop()
  


    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    user_dashboard = UserDashboard(root)
    user_dashboard.run()















































        # self.dashboard_frame = tk.Frame(self.root,background='red')
        # self.dashboard_frame.grid(rowspan=3 ,columnspan=3)


        

        # Add user-specific widgets here

        # Create the logout button inside the frame
        # self.logout_button = tk.Button(self.dashboard_frame, text="Logout", command=self.logout)
        # self.logout_button.pack(side=tk.TOP, anchor=tk.NE)  # Place the button in the top right corner

        # self.create_customer_button = tk.Button(self.dashboard_frame, text="Create Customer", command=self.create_customer)
        # self.create_customer_button.pack(side=tk.TOP, anchor=tk.NE)

    # def create_customer(self):
    #     create_customer_window = tk.Toplevel(self.root)
    #     CreateCustomer(create_customer_window)

    #   def logout(self):
    #     self.root.destroy()  # Close the dashboard and return to the login screen
    #     auth_screen = authentication.AuthenticationScreen(tk.Tk())
    #     auth_screen.root.mainloop()

  