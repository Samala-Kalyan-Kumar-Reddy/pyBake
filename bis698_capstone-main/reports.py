
import tkinter as tk
from tkinter import ttk
from views.styles import Style
from views.authentication import AuthenticationScreen
from controllers.utils import Utils
# from tkinter import PhotoImage

# from PIL import Image, ImageTk


<<<<<<< HEAD
class Home:
    def __init__(self,root):
        self.root = root
        self.root.title("Bakery Management System")
=======
class Report:
    def __init__(self,root):
        self.root = root
        self.root.title("Report Dashboard")
>>>>>>> a7ab2ee8e45a4919a62e40497ec9ffedcc06a44a
        self.root.resizable(False,False)
        # self.root.geometry("800x650")
        # Style.center_window(self.root)



        # self.frame1  = tk.Frame(self.root,background="white")
        # self.frame1.pack(fill = 'both',expand = True)
        # self.frame2  = tk.Frame(self.frame1,bg = 'white',height = 150,width = 300,pady = 40, padx = 40)
        # self.frame2.pack(fill = 'y',side = "top",expand = True)
        # self.right_section  = tk.Frame(self.frame1,bg = '#424242',width = 100)
        # self.frame3.pack(fill = 'y',side = "left")
        # self.frame4  = tk.Frame(self.frame1,bg = '#424242',height = 100)
        # self.frame4.pack(fill = 'x',side = "bottom",expand = True)



        self.wrapper  = tk.Frame(self.root,background="white")
        self.wrapper.pack(fill = 'both',expand = True)
<<<<<<< HEAD
        self.left_nav  = tk.Frame(self.wrapper,bg = '#424242',width = 120)
        self.left_nav.pack(fill = 'y',side = "left")
        self.right_section  = tk.Frame(self.wrapper,bg = 'white')
        self.right_section.pack(fill = 'y',side = "right",expand = True)
=======
        self.left_nav  = tk.Frame(self.wrapper,bg = '#424242',height = 120)
        self.left_nav.pack(fill = 'x',side = "top")
        self.right_section  = tk.Frame(self.wrapper,bg = 'white')
        self.right_section.pack(fill = 'x',side = "bottom",expand = True)
>>>>>>> a7ab2ee8e45a4919a62e40497ec9ffedcc06a44a


        self.welcome_title = tk.Frame(self.right_section,bg = "white",pady = 40, padx = 40)
        self.welcome_title.pack(fill = "x",expand = True,side = 'top')




        self.login_as_title  = tk.Frame(self.right_section,bg = 'white')
        self.login_as_title.pack(fill = 'both', expand = True)

        self.login_as_section = tk.Frame(master = self.right_section,bg='white')
        self.login_as_section.pack(fill = 'both', expand = True)
       
       
       
       



        self.c1_image = Utils.resize_image((30,30),'images/google/cake3.png')
        self.cake1_image = tk.Label(self.left_nav, image=self.c1_image,bg = '#424242',cursor = "hand2")
        self.cake1_image.grid(row = 0,column = 0,pady = (50,20),padx = 20)


        self.c2_image = Utils.resize_image((35,35),'images/google/cake2.png')
        self.cake2_image = tk.Label(self.left_nav, image=self.c2_image,bg = '#424242',cursor = "hand2")
        self.cake2_image.grid(row =1,column = 0,pady = 20,padx = 20)

        self.c3_image = Utils.resize_image((30,30),'images/google/cake.png')
        self.cake3_image = tk.Label(self.left_nav, image=self.c3_image,bg = '#424242',cursor = "hand2")
        self.cake3_image.grid(row =2,column = 0,pady = 20,padx = 20)
        
        self.c4_image = Utils.resize_image((30,30),'images/google/cake5.png')
        self.cake4_image = tk.Label(self.left_nav, image=self.c4_image,bg = '#424242',cursor = "hand2")
        self.cake4_image.grid(row =3,column = 0,pady = 20,padx = 20)

        self.c5_image = Utils.resize_image((30,30),'images/google/cake6.png')
        self.cake5_image = tk.Label(self.left_nav, image=self.c5_image,bg = '#424242',cursor = "hand2")
        self.cake5_image.grid(row =4,column = 0,pady = 20,padx = 20)


        self.c6_image = Utils.resize_image((30,30),'images/google/oven.png')
        self.cake6_image = tk.Label(self.left_nav, image=self.c6_image,bg = '#424242',cursor = "hand2")
        self.cake6_image.grid(row =5,column = 0,pady = 20,padx = 20)


        self.c7_image = Utils.resize_image((30,10),'images/google/flatbread.png')
        self.cake7_image = tk.Label(self.left_nav, image=self.c7_image,bg = '#424242',cursor = "hand2")
        self.cake7_image.grid(row =6,column = 0,pady = 20,padx = 20)

       
       
        text = "Welcome to PyBake Pro"
        tk.Label(self.welcome_title,text = text,font = ("Arial",60),fg = '#006064',wraplength=1200,bg = "white").grid(row = 0, column = 0)
        text = """With PyBake Pro, you can seamlessly manage customers,products, orders, and employees. You can keep your inventory in check,optimize production, delight your customers,\and gain valuable insights into your bakery's performance. From the moment an order is  placed to the sweet smiles on your customers' faces, we've got every aspect covered. """
       
        tk.Label(self.welcome_title,text = text,font = ("Arial",15),wraplength=550,fg = '#424242',bg = "white").grid(row = 1, column = 0,pady = 20)






        tk.Label(self.login_as_title,text = "Who are you?",font = Style.page_heading,bg="white",fg = Style.page_heading_color).grid(row =0,column = 0,sticky='W',pady=(40,15), padx = 40)

        separator = ttk.Separator(self.login_as_title,orient = 'horizontal')
        separator.grid(row = 1, column = 0)
        separator.grid(row = 2, column = 0)

        self.admin_login= Utils.resize_image((100,100),'images/home/admin.png')
        # Create a Label widget with the resized image
        self.admin_login_image = tk.Label(self.login_as_section, image=self.admin_login,cursor = "hand2",bg='white')
        self.admin_login_image.grid(row = 0, column =0)

        self.admin_login_label = tk.Label(self.login_as_section, text="Administrator", fg = '#424242', font = Style.subheading,cursor = "hand2",bg='white')
        self.admin_login_label.grid(row = 1, column =0,pady=(0,200))
        self.admin_login_label.bind("<Button-1>",self.on_admin_login_click)
        self.admin_login_image.bind("<Button-1>",self.on_admin_login_click)

         # EDIT EXISTING ORDER
        self.ord_edit_image = Utils.resize_image((120,120),'images/home/manager.png')
        # Create a Label widget with the resized image
        self.order_edit_image = tk.Label(self.login_as_section, image=self.ord_edit_image,bg='white')
        self.order_edit_image.grid(row = 0, column =1)

        self.order_edit_label = tk.Label(self.login_as_section, text="Manager",fg = '#424242', font = Style.subheading,cursor = "hand2",bg='white')
        self.order_edit_label.grid(row = 1, column =1,pady=(0,200))
        self.order_edit_label.bind("<Button-1>",self.on_order_edit_click)
        self.order_edit_image.bind("<Button-1>",self.on_order_edit_click)

        # UPDATE ORDER
        self.ord_update_image = Utils.resize_image((120,120),'images//home/sales_assoc.png')
        # Create a Label widget with the resized image
        self.order_update_status_image = tk.Label(self.login_as_section, image=self.ord_update_image,bg='white')
        self.order_update_status_image.grid(row = 0, column =2)

        self.order_update_status_label = tk.Label(self.login_as_section, text="Sales Associate", fg = '#424242',font = Style.subheading,cursor = "hand2",bg='white')
        self.order_update_status_label.grid(row = 1, column =2,pady=(0,200))
        self.order_update_status_label.bind("<Button-1>",self.on_order_update_click)
        self.order_update_status_image.bind("<Button-1>",self.on_order_update_click)


        for column in range(3):  # Assuming you have 8 columns in the grid
            self.login_as_section.grid_columnconfigure(column, weight=1)


    def on_admin_login_click(self,event):
        root = tk.Tk()
        auth_screen = AuthenticationScreen(root)
        auth_screen.mainloop()

    def on_order_edit_click(self,event):
        pass

    def on_order_update_click(self,event):
        pass

  



# def Utils.resize_image(size,image_url):
#         # Load the original image
#         original_image = Image.open(f'{image_url}')
#         resized_image = original_image.resize((size[0], size[1]))   
#         tk_image = ImageTk.PhotoImage(resized_image)
#         return tk_image





if __name__ == '__main__':
<<<<<<< HEAD
    home_window = Home(tk.Tk())
=======
    home_window = Report(tk.Tk())
>>>>>>> a7ab2ee8e45a4919a62e40497ec9ffedcc06a44a
    home_window.root.mainloop()

