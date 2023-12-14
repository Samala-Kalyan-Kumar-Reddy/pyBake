import tkinter as tk
# from database import DB_Connection
from tkinter import messagebox,ttk
from controllers.products import Product
from controllers.utils import Utils
from views.styles import Style
from controllers.exception import ProductCodeError,PriceError

class ManageProduct(tk.Toplevel):
    def __init__(self, parent,user_obj,admin_dashboard):
        self.parent = parent
        self.user = user_obj
        self.admin_dashboard = admin_dashboard
        

        self.product_wrapper = tk.Frame(master = self.parent)
        self.product_wrapper.pack(fill = "both",expand = True)
        
        self.title_frame = tk.Frame(master = self.product_wrapper)
        self.title_frame.pack(fill = 'x',expand = True,side = 'top')

        self.form_message_frame = tk.Frame(master = self.product_wrapper)
        self.form_message_frame.pack(anchor='center',pady = 15)

        self.product_frame = tk.Frame(master = self.product_wrapper)
        self.product_frame.pack(fill = "both",expand = True,padx = 100)


        # self.tk_image = Utils.resize_image((50,50),'images/products.png')
        # # Create a Label widget with the resized image
        # self.product_image = tk.Label(self.title_frame, image=self.tk_image)
        # self.product_image.grid(row = 0, column =4,pady = 20, padx = 20,sticky="E")

        # self.product_label = tk.Label(self.title_frame, text="Create Product",font= Style.page_heading,foreground =Style.page_heading_color)
        # self.product_label.grid(row = 0, column = 0, padx=(20,420), pady=10,sticky = "w")



        self.tk_image = Utils.resize_image((50,50),'images/products.png')
        # Create a Label widget with the resized image
        self.title_image = tk.Label(self.title_frame, image=self.tk_image)
        self.title_image.pack(side = "right", padx=(0,40),pady =(20,0))
        tk.Label(self.title_frame, text = "Create Product",font = Style.page_heading,fg = Style.page_heading_color).pack(side = 'left',padx = (40,0), pady =(20,0))

        





        

        tk.Label(self.product_frame, text="Product Code:").grid(row = 1, column =0,sticky='E')
        self.product_code_entry = tk.Entry(self.product_frame,width = 20,font = ('helvetica', 11))
        self.product_code_entry.grid(row = 1, column = 1,padx=20,pady=20,sticky='W')


        tk.Label(self.product_frame, text="Product Name:").grid(row = 2, column = 0,sticky='E')
        self.product_name_entry = tk.Entry(self.product_frame,font = ('helvetica', 11))
        self.product_name_entry.grid(row = 2, column = 1,padx=20,pady=20,sticky='W')


        tk.Label(self.product_frame, text="Price:").grid(row = 3, column = 0,sticky='E')
        self.product_unit_price_entry = tk.Entry(self.product_frame,font = ('helvetica', 11))
        self.product_unit_price_entry.grid(row = 3, column = 1, padx=20,pady=20,sticky='W')


        tk.Label(self.product_frame, text="Description:").grid(row = 4, column = 0,sticky='E')
        self.product_description_entry = tk.Text(self.product_frame,font = ('helvetica', 11),height=3,width = 40)
        self.product_description_entry.grid(row=4, column=1,columnspan = 4,pady = 20, padx=20,sticky='W')
       

        self.form_message = tk.Label(self.form_message_frame,text = "",fg='red',bg = "#FFEBEE")
        self.form_message.grid(row = 0,column=1, columnspan = 3,sticky = "news")


        self.save_button = tk.Button(self.product_frame, text="Save Product",background="#08A04B",fg="black",width= 10, command=self.save_product)
        self.save_button.grid(row = 1, column = 4, sticky='E',padx = (170,0),pady = 20)

        self.clear_button = tk.Button(self.product_frame, text="Clear Form",background="#008FD3",fg="black",width= 10,command=self.clear_product_create_form)
        self.clear_button.grid(row = 2, column = 4, padx=(170,0), sticky='E',pady = 10)



    def save_product(self):
        try:
            if float(self.product_unit_price_entry.get()) <= 0.0:
                raise PriceError("Product price must be greater than 0")
            if len(self.product_code_entry.get()) != 2:
                raise ProductCodeError("Product code must be two characters only")
            product_info = {
                'product_code' :self.product_code_entry.get(),
                'product_name':self.product_name_entry.get(),
                'unit_price':float(self.product_unit_price_entry.get()),
                'product_description':self.product_description_entry.get('1.0', 'end-1c')
                            }
        
        except (PriceError ,ValueError,ProductCodeError) as e:
                self.form_message.config(text = str(e))
        else:
                # new_product = products.Product()
            new_product = Product(
                product_info['product_code'],
                product_info['product_name'],
                product_info['unit_price'],
                product_info['product_description'])
            save_operation = new_product.add_product()
                
            if not save_operation:
                messagebox.showerror("Error", "Product with thesame product code already exist")
            else: 
                messagebox.showinfo("Product Creation","Product added successfully!")  
                self.clear_product_create_form()  


    def clear_product_create_form(self):
        self.product_code_entry.delete(0, tk.END)
        self.product_name_entry.delete(0, tk.END)
        self.product_unit_price_entry.delete(0, tk.END)
        self.product_description_entry.delete("1.0", tk.END)
        self.form_message.config(text = " ")

