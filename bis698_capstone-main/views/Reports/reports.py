import tkinter as tk
# from database import DB_Connection
from tkinter import messagebox,ttk
from controllers.customers import Customer
from controllers.users import User
from controllers.utils import Utils
from controllers.products import Product
from controllers.orders import Order
from .user_report import UserReport
from .customer_report import CustomerReport
from .user_login_report import UserLoginReport
from .product_report import ProductReport
from .top_products import TopProductReport
from .top_customers import TopCustomerReport
from views.user_password_change import PasswordChange
from .customer_order_report import CustomerOrderReport
from views.styles import Style

class Report():
    
    def __init__(self,parent,user_obj,dashboard):

        self.parent = parent
        self.user = user_obj
        self.dashboard = dashboard
        self.utils = Utils()
        self.customer = Customer()
        self.users = User()
        self.product = Product()
        self.order = Order()
        


        self.wrapper = tk.Frame(master = self.parent, bg = "#EEEEEE")
        self.wrapper.pack(fill = "both", expand = True)
        #REPORT FRAMES
        self.report_title = tk.Frame(self.wrapper,height = 70)
        # self.report_title.grid(column = 0, row = 0, padx = 20,pady = 20 ,sticky = "ew")
        self.report_title.pack(fill = "both",expand = True,side = "left",padx = 20,pady = 20)

        self.report_reports = tk.Frame(self.wrapper,height = 100)
        self.report_reports.pack(fill = "x",side = "top",anchor = 'ne',padx = 20, pady = 10)
        # self.report_reports.grid_rowconfigure(0, weight=1)
        # self.report_reports.grid_columnconfigure(1, weight=1)
        # self.report_subsection1= tk.Frame(self.wrapper,height = 100)
        # self.report_subsection1.pack(fill = "both",expand = True,padx = 20, pady = 10)
        # #USER FRAMES
        # self.user_reports = tk.Frame(self.report_subsection1,width = 40, relief=tk.FLAT,bg= "red")
        # self.user_reports.pack(fill = "y",expand = True,side = 'top',anchor = "w")
        # # #CUSTOMER FRAMES
        # self.customer_reports = tk.Frame(self.report_subsection1,width = 200,relief=tk.FLAT,bg = "green")
        # self.customer_reports.pack(fill = 'y',expand = True ,side = 'top',anchor = 'center')
        # # PRODUCT FRAMES
        # self.product_reports = tk.Frame(self.report_subsection1, width = 200,relief=tk.FLAT,bg = "yellow")
        # self.product_reports.pack(fill = "y",expand = True, side = 'top',anchor= 'w')

        # ORDER FRAME
        # self.order_reports = tk.LabelFrame(self.wrapper,text = "Summary Report",height = 100, borderwidth = 1,bg="red")
        # self.order_reports.grid(row = 2, column = 0, columnspan = 3, padx = 20, pady = 20,sticky = "news")
        
        # frame1 = tk.Frame(self.order_reports,height = 20,width = 100,bg='white').grid(row = 0, column = 0,sticky = 'news')

        # frame2= tk.Frame(self.order_reports,height = 20,width = 100,bg='green').grid(row = 0, column = 1,sticky = 'news')
        # frame3= tk.Frame(self.order_reports,height = 20,width = 100,bg='yellow').grid(row = 0, column = 2,sticky = 'news')
       
       #REPORT TITLE
        self.report_text = tk.Label(master = self.report_title,text = "Reports",font = Style.page_heading,fg=Style.page_heading_color)
        self.report_text.grid(row = 0, column = 1,padx = 10,sticky ="W")


        # self.order_report_section1 = tk.Frame(master = self.parent,bg='#EEEEEE')
        # self.order_report_section1.pack(fill = 'both', expand = True,side = 'top')


       
        #REPORT TITLE IMAGE
        self.report_img = Utils.resize_image((70,70),'images/report/system_report.png')
        # Create a Label widget with the resized image
        self.report_image = tk.Label(self.report_title, image=self.report_img,bg = "#EEEEEE")
        self.report_image.grid(row = 0, column =0, padx = 10,sticky="E")
        

        #REPORT SUMMARY TOP
        tk.Label(master = self.report_reports,text = "Report Summary", font = Style.level_one_subheading,fg = Style.level_one_subheading_color).grid(row =0,column = 1,sticky = "w")
        tk.Label(master = self.report_reports,text = "Customers:").grid(row =1,column = 0,sticky='E')
        tk.Label(master = self.report_reports,text = self.customer.customer_count(),font = ("Poppins",15),fg = Style.page_heading_color).grid(row =1,column = 1,sticky='W') 

        tk.Label(master = self.report_reports,text = "Users:").grid(row =1,column = 2,sticky="E")
        tk.Label(master = self.report_reports,text = self.users.user_count(),font = ("Poppins",15),fg = Style.page_heading_color).grid(row =1,column = 3,sticky='W') 

        tk.Label(master = self.report_reports,text = "Products:").grid(row =1,column = 4,sticky="E")
        tk.Label(master = self.report_reports,text = self.product.product_count(),font = ("Poppins",15),fg = Style.page_heading_color).grid(row =1,column = 5,sticky='W')
     
        tk.Label(master = self.report_reports,text = "Orders:").grid(row =2,column = 0,sticky='E')
        tk.Label(master = self.report_reports,text = self.order.order_count(),font = ("Poppins",15),fg = Style.page_heading_color).grid(row =2,column = 1,sticky='W') 

        tk.Label(master = self.report_reports,text = "Sale:").grid(row =2,column = 2,sticky="E")
        tk.Label(master = self.report_reports,text = f"${self.order.total_sale()}",font = ("Poppins",15,'bold'),fg = Style.page_heading_color).grid(row =2,column = 3,sticky='W') 

        tk.Label(master = self.report_reports,text = "Top Selling Product:").grid(row =3,column = 0,sticky='E')
        tk.Label(master = self.report_reports,text = f"{self.product.top_selling_product()[1]}",font = ("Poppins",15),fg = Style.page_heading_color).grid(row =3,column = 1,sticky="W") 

        tk.Label(master = self.report_reports,text = "Quantity Sold:").grid(row =3,column = 2,sticky="E")
        tk.Label(master = self.report_reports,text = f"{self.product.top_selling_product()[2]}",font = ("Poppins",15),fg = Style.page_heading_color).grid(row =3,column = 3,sticky="W") 
     

        

        ###################USERS REPORT##################################

        # ALL USERS REPORT
        # tk.Label(master = self.user_reports,text = "User Report").grid(row = 0, column = 0)
        # tk.Label(master = self.customer_reports,text = "Customer Report").grid(row = 0, column = 0)
        # tk.Label(master = self.product_reports,text = "Product Report").grid(row = 0, column = 0)


        # self.user_img = Utils.resize_image((30,30),'images/report/group_users.png')
        # # Create a Label widget with the resized image
        # self.user_report_image = tk.Label(self.user_reports, image=self.user_img)
        # self.user_report_image.grid(row = 0, column =0,pady = 10, padx = 10,sticky="E")

        # self.user_report_label = tk.Label(self.user_reports, text="User Report",font = ('Poppins', 10),cursor = "hand2")
        # self.user_report_label.grid(row = 0, column =1,padx = 10,sticky='W')
        # self.user_report_label.bind("<Button-1>",self.on_generate_user_report_click)
        
        
         #USER LOGIN REPORT
        # self.login_img = Utils.resize_image((30,30),'images/clock.png')
        # # Create a Label widget with the resized image
        # self.user_login_image = tk.Label(self.user_reports, image=self.login_img)
        # self.user_login_image.grid(row = 1, column =0, padx = 10,sticky="E")

        # self.user_login_label = tk.Label(self.user_reports, text="User Login Report",font = ('Poppins', 10),cursor = "hand2")
        # self.user_login_label.grid(row = 1, column =1,padx = 10, pady=10,sticky='E')
        # self.user_login_label.bind("<Button-1>",self.on_generate_user_login_report_click)
     



        ###############CUSTOMER REPORTS##################################

        #ALL CUSTOMER REPORT
        # self.customer_img = Utils.resize_image((30,30),'images/report/customers.png')
        # # Create a Label widget with the resized image
        # self.customer_report_image = tk.Label(self.customer_reports, image=self.customer_img)
        # self.customer_report_image.grid(row = 0, column =0, pady= 10,padx = 10,sticky="E")

        # self.customer_report_label = tk.Label(self.customer_reports, text="All Customer Report",font = ('Poppins', 10),cursor = "hand2")
        # self.customer_report_label.grid(row = 0, column =1,padx = 10,sticky='W')
        # self.customer_report_label.bind("<Button-1>",self.on_generate_all_customer_report_click)
        
        
        # #TOP BUYING CUSTOMER
        # self.best_cust_image = Utils.resize_image((30,30),'images/report/top_customers.png')
        # # Create a Label widget with the resized image
        # self.customer_top_image = tk.Label(self.customer_reports, image=self.best_cust_image)
        # self.customer_top_image.grid(row = 1, column =0, padx = 10,sticky="E")

        # self.customer_top_label = tk.Label(self.customer_reports, text="Top Buying Customer",font = ('Poppins', 10),cursor = "hand2")
        # self.customer_top_label.grid(row = 1, column =1, pady = 10, padx = 10,sticky='W')
        # self.customer_top_label.bind("<Button-1>",self.on_generate_top_customer_report_click)
     

        

    

         ###############PRODUCTS REPORTS##################################

        #ALL PRODUCTS REPORT
        # self.product_img = Utils.resize_image((30,30),'images/report/products.png')
        # # Create a Label widget with the resized image
        # self.product_report_image = tk.Label(self.product_reports, image=self.product_img)
        # self.product_report_image.grid(row = 0, column =0, pady = 10, padx = 10,sticky="E")

        # self.product_report_label = tk.Label(self.product_reports, text="All Products Report",font = ('Poppins', 10),cursor = "hand2")
        # self.product_report_label.grid(row = 0, column =1,padx = 10,sticky='E')
        # self.product_report_label.bind("<Button-1>",self.on_generate_all_product_report_click)
        
        
        # #TOP SELLING PRODUCTS
        # self.top_prod_image = Utils.resize_image((30,30),'images/clock.png')
        # # Create a Label widget with the resized image
        # self.top_prouct_image = tk.Label(self.product_reports, image=self.top_prod_image)
        # self.top_prouct_image.grid(row = 1, column =0, padx = 10,sticky="E")

        # self.top_prouct_label = tk.Label(self.product_reports, text="Top Selling Products",font = ('Poppins', 10))
        # self.top_prouct_label.grid(row = 1, column =1, pady = 10, padx = 10,sticky='E')
        # self.top_prouct_label.bind("<Button-1>",self.on_generate_top_product_report_click)

        # #CUSTOMER ORDERS REPORT
        # self.customer_order_label = tk.Label(self.wrapper, text="Customer Order Report",font = ('Poppins', 10))
        # self.customer_order_label.grid(row = 2, column =1, pady = 10, padx = 10,sticky='E')
        # self.customer_order_label.bind("<Button-1>",self.on_generate_customer_orders_report_click)
       

        self.report_section_1 = tk.Frame(master = self.parent,bg='#EEEEEE')
        self.report_section_1.pack(fill = 'both', expand = True,side = 'top')

        self.report_section_2 = tk.Frame(master = self.parent,bg='#EEEEEE')
        self.report_section_2.pack(fill = 'both', expand = True,side = 'top')





        
        # USER REPORT

        self.user_report_label = tk.Label(self.report_section_1, text="Users",font = Style.level_one_subheading,fg = Style.page_heading_color,cursor = "hand2")
        self.user_report_label.grid(row = 0, column =0,pady=(0,20),sticky = 'news')
        self.a_user_image = Utils.resize_image((50,50),'images/report/user-check.png')
        # Create a Label widget with the resized image
        self.all_user_image = tk.Label(self.report_section_1, image=self.a_user_image,cursor = "hand2")
        self.all_user_image.grid(row = 1, column =0)

        self.all_user_label = tk.Label(self.report_section_1, text="All Users Report", font = Style.level_three_subheading,cursor = "hand2")
        self.all_user_label.grid(row = 2, column =0,pady=(0,40))
        self.all_user_label.bind("<Button-1>",self.on_all_user_click)
        self.all_user_image.bind("<Button-1>",self.on_all_user_click)

         # ALL CUSTOMER REPORT
        self.customer_label = tk.Label(self.report_section_1, text="Customers" ,font = Style.level_one_subheading,fg = Style.page_heading_color,cursor = "hand2")
        self.customer_label.grid(row = 0, column =1,pady=(0,20),sticky ='news')

        self.all_cust_img= Utils.resize_image((50,50),'images/report/user-crown.png')
        self.all_customer_image = tk.Label(self.report_section_1, image=self.all_cust_img)
        self.all_customer_image.grid(row = 1, column =1)

        self.all_customer_label = tk.Label(self.report_section_1, text="All Customers Report", font = Style.level_three_subheading,cursor = "hand2")
        self.all_customer_label.grid(row = 2, column =1,pady=(0,40))
        self.all_customer_label.bind("<Button-1>",self.on_all_customer_report_click)
        self.all_customer_image.bind("<Button-1>",self.on_all_customer_report_click)

        # PRODUCT REPORT
        self.product_label = tk.Label(self.report_section_1, text="Products", font = Style.level_one_subheading,fg = Style.page_heading_color,cursor = "hand2")
        self.product_label.grid(row = 0, column =2,pady=(0,20),sticky = 'news')

        self.prod_image = Utils.resize_image((50,50),'images/report/box-open-full.png')
        # Create a Label widget with the resized image
        self.product_report_image = tk.Label(self.report_section_1, image=self.prod_image)
        self.product_report_image.grid(row = 1, column =2)

        self.product_label = tk.Label(self.report_section_1, text="All Products Report", font = Style.level_three_subheading,cursor = "hand2")
        self.product_label.grid(row = 2, column =2,pady=(0,40))
        self.product_label.bind("<Button-1>",self.on_all_product_report_click)
        self.product_report_image.bind("<Button-1>",self.on_all_product_report_click)



        #ORDER REPORT
        self.order_label = tk.Label(self.report_section_1, text="Orders" ,font = Style.level_one_subheading,fg = Style.page_heading_color,cursor = "hand2")
        self.order_label.grid(row = 0, column =3,pady=(0,20),sticky = 'news')
        self.ord_image = Utils.resize_image((50,50),'images/report/cart.png')
        # Create a Label widget with the resized image
        self.order_report_image = tk.Label(self.report_section_1, image=self.ord_image)
        self.order_report_image.grid(row = 1, column =3)

        self.order_report_label = tk.Label(self.report_section_1, text="All Orders Report", font = Style.level_three_subheading,cursor = "hand2")
        self.order_report_label.grid(row = 2, column =3,pady=(0,40))
        self.order_report_label.bind("<Button-1>",self.on_order_report_click)
        self.order_report_image.bind("<Button-1>",self.on_order_report_click)


        for column in range(4):  # Assuming you have 8 columns in the grid
            self.report_section_1.grid_columnconfigure(column, weight=1)




        # USERS LOGIN REPORT
        self.userlogin_img = Utils.resize_image((50,50),'images/report/user-time.png')
        # Create a Label widget with the resized image
        self.user_login_report_image = tk.Label(self.report_section_2, image=self.userlogin_img,cursor = "hand2")
        self.user_login_report_image.grid(row = 0, column =0)

        self.user_login_report_label = tk.Label(self.report_section_2, text="User Login Report", font = Style.level_three_subheading,cursor = "hand2")
        self.user_login_report_label.grid(row = 1, column =0,pady=(0,40))
        self.user_login_report_label.bind("<Button-1>",self.on_user_login_report_click)
        self.user_login_report_image.bind("<Button-1>",self.on_user_login_report_click)

         # TOP CUSTOMER REPORT
        self.top_cust_img = Utils.resize_image((50,50),'images/report/trophy-star.png')
        # Create a Label widget with the resized image
        self.top_customers_image = tk.Label(self.report_section_2, image=self.top_cust_img)
        self.top_customers_image.grid(row = 0, column =1)

        self.top_customers_label = tk.Label(self.report_section_2, text="Top Customers Report", font = Style.level_three_subheading,cursor = "hand2")
        self.top_customers_label.grid(row = 1, column =1,pady=(0,40))
        self.top_customers_label.bind("<Button-1>",self.on_top_customers_click)
        self.top_customers_image.bind("<Button-1>",self.on_top_customers_click)

        # TOP PRODUCT REPORT
        self.top_prod_img = Utils.resize_image((50,50),'images/report/boxes.png')
        # Create a Label widget with the resized image
        self.top_products_image = tk.Label(self.report_section_2, image=self.top_prod_img)
        self.top_products_image.grid(row = 0, column =2)

        self.top_products_label = tk.Label(self.report_section_2, text="Top Products Report", font = Style.level_three_subheading,cursor = "hand2")
        self.top_products_label.grid(row = 1, column =2,pady=(0,40))
        self.top_products_label.bind("<Button-1>",self.on_top_products_click)
        self.top_products_image.bind("<Button-1>",self.on_top_products_click)

        #SALES REPORT
        self.sales_reprt_image = Utils.resize_image((50,50),'images/report/arrow-trend-up.png')
        # Create a Label widget with the resized image
        self.sales_report_image = tk.Label(self.report_section_2, image=self.sales_reprt_image)
        self.sales_report_image.grid(row = 0, column =3)

        self.sales_report_label = tk.Label(self.report_section_2, text="Detailed Sales Report", font = Style.level_three_subheading,cursor = "hand2")
        self.sales_report_label.grid(row = 1, column =3,pady=(0,40))
        self.sales_report_label.bind("<Button-1>",self.on_sales_report_click)
        self.sales_report_image.bind("<Button-1>",self.on_sales_report_click)


        for column in range(4):  # Assuming you have 8 columns in the grid
            self.report_section_2.grid_columnconfigure(column, weight=1)






       
    def on_logout_label_click(self,event):
        result = messagebox.askyesno("Question","Are you sure you want to log out?")
        if result:
            #call the logout function in the user_dashboard
            self.user.logout()


    def on_change_password_click(self,event):
        change_password_window = tk.Toplevel(self.parent)
        PasswordChange(change_password_window,self.user)

    #USER REPORT CLICKS#

    def on_all_user_click(self,event):
        report_window = tk.Toplevel(self.parent)
        UserReport(report_window,self.user)

    def on_user_login_report_click(self,event):
        login_report_window = tk.Toplevel(self.parent)
        UserLoginReport(login_report_window,self.user)
       

    #CUSTOMER REPORT CLICKS#
    def on_all_customer_report_click(self,event):
        report_window = tk.Toplevel(self.parent)
        CustomerReport(report_window,self.user)

    def on_top_customers_click(self,event):
        report_window = tk.Toplevel(self.parent)
        TopCustomerReport(report_window,self.user)
        



    #PRODUCT REPORT CLICKS

    def on_all_product_report_click(self,event):
        report_window = tk.Toplevel(self.parent)
        ProductReport(report_window,self.user)

    def on_top_products_click(self,event):
        report_window = tk.Toplevel(self.parent)
        TopProductReport(report_window,self.user)



    #ORDER REPORT CLICKS
    def on_order_report_click(self,event):
        report_window = tk.Toplevel(self.parent)
        CustomerOrderReport(report_window,self.user)

    def on_sales_report_click(self,event):
        pass




    def logout(self):
        self.user.logout()
       
        
# if __name__ == "__main__":
#     root = tk.Tk()
#     create_customer_window = tk.Toplevel(root)
#     CreateCustomer(create_customer_window)
#     root.mainloop()
