
import tkinter as tk
from tkinter import ttk
from ..customers.customer import CreateCustomer
from .manager_profile import ManagerProfile
from ..reports.reports import Report
from ..orders.orders import Order
# from .user_profile import UserProfile
import views.authentication as authentication
from controllers.utils import Utils
from datetime import datetime

class ManagerDashboard:
    def __init__(self,root,user_obj):
        self.root = root
        self.user = user_obj
        self.root.title("Manager Dashboard")
        # self.root.geometry("800x500")
        # self.root.resizable(False, False)
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
        self.frame4 = ttk.Frame(self.tab_control)

        # Add Frames to the Notebook with Tab Names
        self.tab_control.add(self.frame1, text="Manage Profile")
        self.tab_control.add(self.frame2, text="Create Customers")
        self.tab_control.add(self.frame3, text="Manage Orders")
        self.tab_control.add(self.frame4, text="Reports")
        # Create content for Tab 1
        self.create_customer = CreateCustomer(self.frame2)
       


        #create content for Tab 2
        # self.manage_profile = UserProfile(self.frame2)

        #create content for Tab 3
        # self.tk_image1 = Utils.resize_image((50,50),'images/woman.png')
        # # Create a Label widget with the resized image
        # self.profile_image = tk.Label(self.frame3, image=self.tk_image1)
        # # self.profile_image.grid(row = 0, column=1,pady = 20, padx = 20,sticky="E")
        # self.profile_image.grid(row=0,column=0)

        # self.profile_label = tk.Label(self.frame3, text="User Profile",font= ('Helvetica',18),foreground ='#008fd3')
        # self.profile_label.grid(row = 1, column = 0, padx=20, pady=10)

        # self.label2 = tk.Label(self.frame3, text="User Profile Two0",font= ('Helvetica',18),foreground ='#008fd3')
        # self.label2.grid(row = 0, column = 2, padx=20, pady=10)
        self.manager_profile = ManagerProfile(self.frame1,user_obj=self.user, manager_dashboard = self)
        self.manage_order = Order(self.frame3,user_obj = self.user,dashboard = self)
        self.report = Report(self.frame4,self.user,dashboard =self)

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
    user_dashboard = ManagerDashboard(root)
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

  