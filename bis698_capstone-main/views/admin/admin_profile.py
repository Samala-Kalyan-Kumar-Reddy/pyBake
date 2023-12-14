import tkinter as tk
# from database import DB_Connection
from tkinter import messagebox,ttk
from controllers.customers import Customer
from controllers.utils import Utils
from ..user_password_change import PasswordChange
from ..styles import Style

class AdminProfile():
    
    def __init__(self,parent,user_obj,admin_dashboard):

        self.parent = parent
        self.user = user_obj
        self.admin_dashboard = admin_dashboard
        self.utils = Utils()
        

        #TITLE FRAME
        self.title_frame = tk.Frame(master = self.parent,background = "#EEEEEE")
        self.title_frame.pack(fill="x", expand=True,anchor='n')

        

        #PROFILE PICTURE AND LOGIN ACTIVITY FRAME
        # self.picture_frame = tk.Frame(master = self.parent,bg = "#EEEEEE")
        # self.picture_frame.pack(fill = "x", expand=True,anchor = 'n')


        self.user_info_wrapper_frame = tk.Frame(master = self.parent)
        self.user_info_wrapper_frame.pack(fill = 'both', expand=True,pady = 20)

        self.user_info1_frame = tk.Frame(master = self.user_info_wrapper_frame,bg = "#EEEEEE")
        self.user_info1_frame.pack(fill = "y", expand=True,anchor='w',side = "left",padx = 20,pady = 20)

       
        self.profile_picture_frame = tk.Frame(master = self.user_info_wrapper_frame,bg = "#EEEEEE")
        self.profile_picture_frame.pack(fill = "y", expand=True,anchor='center',side = 'left',padx = 20,pady = 20)

        self.user_status_frame = tk.Frame(master = self.user_info_wrapper_frame,bg = "#EEEEEE")
        self.user_status_frame.pack(fill = "y", expand=True,anchor='e',side = 'left',padx = 20,pady = 20)






        self.permissions_wrapper_frame = tk.Frame(master = self.parent)
        self.permissions_wrapper_frame.pack(fill = 'both',padx = 100, expand=True,pady = 20)

        self.permissions_frame = tk.Frame(master = self.permissions_wrapper_frame,bg = "#EEEEEE")
        self.permissions_frame.pack(fill = "y", expand=True,anchor='w',side = "left")

       
        self.product_frame = tk.Frame(master = self.permissions_wrapper_frame,bg = "#EEEEEE")
        self.product_frame.pack(fill = "y", expand=True,anchor='center',side = 'left')

        self.reporting_frame = tk.Frame(master = self.permissions_wrapper_frame,bg = "#EEEEEE")
        self.reporting_frame.pack(fill = "y", expand=True,anchor='e',side = 'left')





    

        self.user_settings_frame = tk.Frame(master = self.parent,bg = "#EEEEEE")
        self.user_settings_frame.pack(fill="both", expand=True)
        # self.user_settings_frame = tk.Frame(master = self.parent,bg = "#EEEEEE")
        # self.user_settings_frame.pack(fill="x", expand=True)


        
      
        self.user_label = tk.Label(self.title_frame, text="User Profile",font= Style.page_heading,fg = Style.page_heading_color)
        self.user_label.pack(side = "left")




        #LOGOUT
        self.lg_image = Utils.resize_image((25,25),'images/google/logout.png')
        self.logout_image = tk.Label(self.title_frame, image=self.lg_image,bg = "#EEEEEE",cursor = "hand2")
        self.logout_image.pack(side = "right")
        self.logout_image.bind("<Button-1>",self.on_logout_label_click)
        self.signout = tk.Label(self.title_frame, text="Sign Out",font = ('helvetica', 12),cursor = "hand2")
        self.signout.pack(side = 'right' )
        self.signout.bind("<Button-1>",self.on_logout_label_click)




        # tk.Label(self.user_info1_frame, text=f"{user_obj['firstname'].capitalize()} {user_obj['lastname'].capitalize()}",font = ('helvetica', 18,'bold')).grid(row = 1, column = 0,sticky = 'we')
        tk.Label(self.user_info1_frame, text=f"{self.utils.get_time_of_day_greeting()},",font = ('Poppins', 18,)).grid(row = 0, column = 0,sticky = 'w')
        tk.Label(self.user_info1_frame, text=f"{user_obj['firstname'].capitalize()}",font = ('Poppins', 18,)).grid(row = 1, column = 0,sticky = 'w')

        #PROFILE PICTURE WIDGET
        # self.tk_image = Utils.resize_image((100,100),'images/user.png')
        # self.user_image = tk.Label(self.picture_frame, image=self.tk_image)
        # self.user_image.pack(anchor="center")

        self.tk_image = Utils.resize_image((100,100),'images/user.png')
        self.user_image = tk.Label(self.profile_picture_frame, image=self.tk_image)
        self.user_image.grid(row = 0, column = 0,sticky = 'news')
        tk.Label(self.profile_picture_frame, text=f"{user_obj['firstname'].capitalize()} {user_obj['lastname'].capitalize()}",font = ('Poppins', 18,'bold')).grid(row = 1, column = 0,sticky = 'we')
        tk.Label(self.profile_picture_frame, text=f"({user_obj['email']})",font = ('Poppins', 12),fg = "#006064").grid(row = 2, column = 0,sticky = 'we')

       


        tk.Label(self.user_status_frame, text="Role:", font = ('helvetica', 12,"bold")).grid(row = 0, column = 0,sticky="w")
        tk.Label(self.user_status_frame, text=user_obj['role'],font = ('helvetica', 12)).grid(row = 0, column = 1,sticky='w')

        tk.Label(self.user_status_frame, text="Status:", font = ('helvetica', 12,"bold")).grid(row = 1, column = 0,sticky="w")
        self.stat_image = Utils.resize_image((15,15),'images/google/active-user.png')
        self.status_image = tk.Label(self.user_status_frame, image=self.stat_image)
        self.status_image.grid(row =1,column = 1,sticky = 'W')


        # tk.Label(self.user_status_frame, text=f"({user_obj['status']})",font = ('helvetica', 10)).grid(row = 1, column = 1)
        tk.Label(self.user_status_frame, text="Date Joined:", font = ('helvetica', 12,"bold")).grid(row = 2, column = 0,sticky='w')
        tk.Label(self.user_status_frame, text=self.utils.get_date_joined(user_obj['email']).strftime("%b. %d, %Y") ,font = ('helvetica', 11)).grid(row = 2, column = 1,sticky='w')
        tk.Label(self.user_status_frame, text="Logged In:", font = ('helvetica', 12,"bold")).grid(row = 3, column = 0,sticky='w')
        tk.Label(self.user_status_frame, text=self.utils.get_last_logged_in_time(user_obj['email']).strftime("%b. %d, %Y %H:%M"),font = ('helvetica', 11)).grid(row = 3, column = 1,sticky='w')

        for widget in self.user_status_frame.winfo_children():
            widget.grid_configure(pady=2)
        
       #PERMISSIONS
        self.perm_image = Utils.resize_image((20,20),'images/google/key.png')
        self.permission_image = tk.Label(self.permissions_frame, image=self.perm_image)
        self.permission_image.grid(row =0,column = 0,sticky='E')
        tk.Label(self.permissions_frame,  text="My Permissions",font = ('Poppins', 15,'bold'),bg = "#EEEEEE", fg = "#263238").grid(row = 0, column = 0,padx =(20,0),sticky = "W")
        tk.Label(self.permissions_frame, text="* Create User Account",font = ('helvetica', 11),bg = "#EEEEEE", fg = "#263238").grid(row = 1, column = 0,pady =5,padx =20,sticky = "w")
        tk.Label(self.permissions_frame, text="* Reset User Password",font = ('helvetica', 11),bg = "#EEEEEE", fg = "#263238").grid(row = 2, column = 0,padx =20,sticky = "w")
        tk.Label(self.permissions_frame, text="* Act/Deactivate User Account",font = ('helvetica', 11),bg = "#EEEEEE", fg = "#263238").grid(row = 3, column = 0,pady = 5,padx =20,sticky = "w")
        

        #PERMISSIONS
        tk.Label(self.product_frame,text = "",font = ('helvetica', 15,'bold'),bg = "#EEEEEE", fg = "#263238").grid(row = 0, column = 0,padx =20)
        tk.Label(self.product_frame, text="* Create Products",font = ('helvetica', 11),bg = "#EEEEEE", fg = "#263238").grid(row = 1, column = 0,padx =20,pady =5,sticky = "W")
        tk.Label(self.product_frame, text="* Edit and Delete Products",font = ('helvetica', 11),bg = "#EEEEEE", fg = "#263238").grid(row = 2, column = 0,padx =20,sticky = "W")
        tk.Label(self.product_frame, text="* Generate Product Reports",font = ('helvetica', 11),bg = "#EEEEEE", fg = "#263238").grid(row = 3, column = 0,padx =20,pady = 5,sticky = "W")
        


        tk.Label(self.reporting_frame, text="",font = ('helvetica', 15,'bold'),bg = "#EEEEEE", fg = "#263238").grid(row = 0, column = 0,padx =20)
        tk.Label(self.reporting_frame, text="* Create Customers",font = ('helvetica', 11),bg = "#EEEEEE", fg = "#263238").grid(row = 1, column = 0,padx =20,pady =5,sticky = "W")
        tk.Label(self.reporting_frame, text="* Generate Customer Reports",font = ('helvetica', 11),bg = "#EEEEEE", fg = "#263238").grid(row = 2, column = 0,padx =20,sticky = "W")
        tk.Label(self.reporting_frame, text="* Generate Users Report",font = ('helvetica', 11),bg = "#EEEEEE", fg = "#263238").grid(row = 3, column = 0,padx =20,pady = 5,sticky = "W")
        

        for column in range(8):  # Assuming you have 8 columns in the grid
            self.user_settings_frame.grid_columnconfigure(column, weight=1)


           #CHANGE PASSWORD
        self.pass_image = Utils.resize_image((30,30),'images/google/password.png')
        # Create a Label widget with the resized image
        self.password_image = tk.Label(self.user_settings_frame, image=self.pass_image,bg = "#EEEEEE")
        self.password_image.grid(row = 0, column =0,sticky='E')

        self.change_password_label = tk.Label(self.user_settings_frame, text="Change Password",fg = "#006064",font = ('helvetica', 12),bg = "#EEEEEE",cursor = "hand2")
        self.change_password_label.grid(row = 0, column =1,sticky='W')
        self.change_password_label.bind("<Button-1>",self.on_change_password_click)
        
       


        #VIEW LOGIN ACTIVITES 
        self.log_image = Utils.resize_image((30,30),'images/google/login_activities.png')
        # Create a Label widget with the resized image
        self.login_activities_image = tk.Label(self.user_settings_frame, image=self.log_image,bg = "#EEEEEE")
        self.login_activities_image.grid(row = 0, column =2,sticky = 'E')

        self.login_activities_label = tk.Label(self.user_settings_frame, text="View Login History",fg = "#006064",font = ('helvetica', 12),bg = "#EEEEEE",cursor = "hand2")
        self.login_activities_label.grid(row = 0, column =3,sticky='W')
        self.login_activities_label.bind("<Button-1>",self.on_login_activities_click)


         #PLACEHOLDER1
        self.p1_image = Utils.resize_image((30,30),'images/google/password.png')
        # Create a Label widget with the resized image
        self.placeholder1_image = tk.Label(self.user_settings_frame, image=self.p1_image,bg = "#EEEEEE")
        self.placeholder1_image.grid(row = 0, column =4,sticky='E')

        self.change_placeholder1_label = tk.Label(self.user_settings_frame, text="Change Password",fg = "#006064",font = ('helvetica', 12),bg = "#EEEEEE",cursor = "hand2")
        self.change_placeholder1_label.grid(row = 0, column =5,sticky='W')
        self.change_placeholder1_label.bind("<Button-1>",self.on_change_password_click)
        
        


        #PLACEHOLDER2
        self.p2_image = Utils.resize_image((30,30),'images/google/login_activities.png')
        # Create a Label widget with the resized image
        self.placeholder2_image = tk.Label(self.user_settings_frame, image=self.p2_image,bg = "#EEEEEE")
        self.placeholder2_image.grid(row = 0, column =6,pady = 20,sticky='E')

        self.placeholder2_label = tk.Label(self.user_settings_frame, text="View Login History",fg = "#006064",font = ('helvetica', 12),bg = "#EEEEEE",cursor = "hand2")
        self.placeholder2_label.grid(row = 0, column =7,sticky='W')
        self.placeholder2_label.bind("<Button-1>",self.on_login_activities_click)
       
    def on_logout_label_click(self,event):
        result = messagebox.askyesno("Question","Are you sure you want to log out?")
        if result:
            #call the logout function in the user_dashboard
            self.admin_dashboard.logout()


    def on_change_password_click(self,event):
        change_password_window = tk.Toplevel(self.parent)
        PasswordChange(change_password_window,self.user)

    def on_login_activities_click(self):
        pass
       

    def logout(self):
        self.admin_dashboard.logout()
