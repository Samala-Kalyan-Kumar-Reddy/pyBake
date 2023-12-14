import tkinter as tk
from tkinter import ttk
from controllers.users import User
from controllers.customers import Customer
from controllers.products import Product
from controllers.orders import Order
from tkinter import messagebox
from werkzeug.security import generate_password_hash,check_password_hash
from controllers.utils import MyCalendar
from controllers.utils import Utils
from controllers.exception import DateEmptyError,ProductEmptyError
from controllers.utils import ReportExporter
from views.styles import Style


class CreateOrder(tk.Toplevel):
    def __init__(self, root,user_obj,dashboard):
        self.root = root
        self.user = user_obj
        self.dashboard = dashboard
        self.root.title("Create Order")
        self.utils = Utils()
        self.product = Product()
        self.customer = Customer()
        self.root.resizable(False,False)
        self.report_exporter = ReportExporter()
        self.order_invoice_template = ReportExporter.get_invoice_template()
        # self.root.geometry("500x400")


        # self.title_frame = tk.Frame(master = self.root,bg = "#EEEEEE",borderwidth = 1)
        # self.title_frame.pack(padx = 20, pady = (20,0))

     



        self.title_frame = tk.Frame(master = self.root,bg = "#EEEEEE")
        self.title_frame.pack(side="top", fill="x", expand=True)

        self.customer_frame = tk.Frame(master = self.root,bg = "#EEEEEE")
        self.customer_frame.pack(padx = 20, pady = (20,0),expand =True,fill = "x")

        self.order_error_frame = tk.Frame(master = self.root,bg = "#EEEEEE")
        self.order_error_frame.pack(padx = 20)

        self.product_frame = tk.Frame(master = self.root,bg = "#EEEEEE")
        self.product_frame.pack(padx = 20)

        self.notes_frame = tk.Frame(master = self.root,bg = "#EEEEEE")
        self.notes_frame.pack(padx = 20, pady = (5,0) ,expand =True,fill = "x")


        self.button_frame = tk.Frame(self.root, bg = "#EEEEEE")
        self.button_frame.pack(padx = 20)

        self.total_amount = 0.0
        self.selected_date = tk.StringVar()

        self.selected_delivery_option = tk.StringVar()
        self.selected_delivery_option.set("pickup") 

        # self.selected.config(text=f"Selected Date: {selected_date}")

        
        # Create form elements for creating a customer

       

        # #this will be a drop down menu containing all customers
        self.selected_customer_value = tk.StringVar()
        self.selected_product_value = tk.StringVar()



        #ERROR MESSAGE
        self.order_error_message = tk.Label(self.order_error_frame, text = "",bg = "#FFEBEE",fg = 'red')
        self.order_error_message.grid(row = 0, column =0,columnspan = 4,sticky = 'news')

        #FOR CUSTOMER

        self.tk_image = Utils.resize_image((50,50),'images/order/checklist.png')
        # Create a Label widget with the resized image
        self.product_image = tk.Label(self.title_frame, image=self.tk_image)
        self.product_image.pack(side = "right", padx=(0,40),pady =(20,0))
        tk.Label(self.title_frame, text = "Create Orders",font = Style.page_heading,fg =Style.page_heading_color).pack(side = 'left',padx = (40,0), pady =(20,0))

        tk.Label(self.customer_frame, text="Select Customer:").grid(row = 0, column =0,sticky = "W")
        self.search_customer_combobox = ttk.Combobox(self.customer_frame,width = 30, values=self.get_customers())
        self.search_customer_combobox.grid(row = 0, column =1)
        self.search_customer_combobox.bind("<<ComboboxSelected>>", self.on_customer_combobox_select)        
        # self.first_name_entry.grid(row = 1, column = 1,padx=10,pady=5)


        self.fulfilment_date_label = tk.Label(self.customer_frame,text = "Pickup/Delivery Date: ",font = ("helvetica",12,'bold'))
        self.fulfilment_date_label.grid(row = 1,column = 0,pady = 20, sticky = 'w')
        self.fulfilment_date_entry = tk.Entry(self.customer_frame, width = 15, textvariable = self.selected_date)
        self.fulfilment_date_entry.grid(row = 1 ,column = 1, padx = 0 ,pady = 20, sticky = 'E')
        self.fulfilment_date_button = tk.Button(self.customer_frame,text = "select Date",command =self.select_date)
        self.fulfilment_date_button.grid(row = 1, column = 2, padx = 0, pady = 20, sticky = 'w')


        self.delivery_method_label = tk.Label(self.customer_frame,text = "Delivery Method: ",font = ("helvetica",12,'bold'))
        self.delivery_method_label.grid(row = 2,column = 0, sticky = 'W')


        self.delivery_method_radio_1 = tk.Radiobutton(self.customer_frame, text="Pickup", variable=self.selected_delivery_option, value='pickup',command=lambda: self.show_selected_option('pickup'))
        self.delivery_method_radio_2 = tk.Radiobutton(self.customer_frame, text="Delivery", variable=self.selected_delivery_option, value='delivery',command=lambda: self.show_selected_option('delivery'))

        self.delivery_method_radio_1.grid(row=3,column = 0,sticky="W")
        self.delivery_method_radio_2.grid(row=4,column = 0,sticky="W")

        


        #DISPLAY CUSTOMER INFORMATION
        #customer name
        tk.Label(self.customer_frame, text = "Customer Name:",font = ("helvetica",12,'bold')).grid(row = 2, column = 1,sticky = "E")
        self.customer_name = tk.Label(self.customer_frame,text = "")
        self.customer_name.grid(row = 2, column = 2,sticky = "W")

        #customer Address:
        tk.Label(self.customer_frame,text = "Customer Address:", font = ("helvetica",12,'bold')).grid(row = 3, column = 1,sticky = "E")
        self.customer_address = tk.Label(self.customer_frame,text = "")
        self.customer_address.grid(row = 3, column = 2,sticky = "W")




        #FOR PRODUCTS

        tk.Label(self.product_frame, text="Select Product:").grid(row = 0, column =0,pady = (20,0))
       
        self.search_product_combobox = ttk.Combobox(self.product_frame,values=self.get_products())
        self.search_product_combobox.grid(row = 1, column =0,pady = (0.10))
        self.search_product_combobox.bind("<<ComboboxSelected>>", self.on_product_combobox_select) 

        #QUANTITY
        self.qty_label = tk.Label(self.product_frame, text = "Qty")
        self.qty_label.grid(row = 0, column = 1,pady = (20,0))

        self.qty_spinbox = tk.Spinbox(self.product_frame,width = 3 ,fr= 1, to = 100)
        self.qty_spinbox.grid(row = 1, column = 1, pady =(0,10))

        self.item_add_button = tk.Button(self.product_frame,text = "Add Item",command = self.add_item)
        self.item_add_button.grid(row = 1, column = 2,pady = 10)


        # self.product_name_entry = tk.Entry(self.product_frame, textvariable=self.selected_product_value)
        # self.search_customer_entry.grid(row=1,column=2)

        # self.search_customer_entry = tk.Entry(self.customer_frame, textvariable=self.selected_customer_value)
        # self.search_customer_entry.grid(row=1,column=2)

        
        #PRODUCT DISPLAY TABLE

        self.style = ttk.Style()
        # self.style.theme_use('clam')
        report_font = ['Helvetica', 12, 'bold']
        # Configure the style of Heading in Treeview widget
        self.style.configure('Treeview.Heading', background="lightgray", font=report_font)

        self.product_display_table = ttk.Treeview(self.product_frame,column=("1", "2", "3", "4", "5","6"), show='headings')


        self.product_display_table.tag_configure('gray', background='lightgray')
        self.product_display_table.tag_configure('normal', background='white')

        cell_width = 100
        self.product_display_table.column("#1", anchor=tk.CENTER,width = cell_width)
        self.product_display_table.heading("#1", text="S/N")
        self.product_display_table.column("#2", anchor=tk.CENTER,width = cell_width)
        self.product_display_table.heading("#2", text="Product Code")
        self.product_display_table.column("#3", anchor=tk.CENTER,width = 150)
        self.product_display_table.heading("#3", text="Product Name")
        self.product_display_table.column("#4", anchor=tk.CENTER,width = cell_width)
        self.product_display_table.heading("#4", text="Quantity")
        self.product_display_table.column("#5", anchor=tk.CENTER,width = cell_width)
        self.product_display_table.heading("#5", text="Unit Price")
        self.product_display_table.column("#6", anchor=tk.CENTER,width = cell_width)
        self.product_display_table.heading("#6", text="Amount")

        #self.product_display_table.grid(row=3, column=0)
        self.product_display_table.grid(row = 2, column = 0, columnspan = 3)
        self.total_amount_widget = tk.Label(self.product_frame, text=f"Total Amount:  ${self.total_amount:,.2f}",font = ('helvetica', 15,'bold'))
        self.total_amount_widget.grid(row = 3, column = 2,sticky='E')
        


       


       #NOTES
        tk.Label(self.notes_frame, text="Notes:",font = ('helvetica', 12)).grid(row = 0, column = 0,sticky='W')
        self.note_entry = tk.Text(self.notes_frame,font = ('helvetica', 11),height=2)
        self.note_entry.grid(row=1, column=0,columnspan = 3,sticky='E')


        #BUTTONS

        self.btnSaveOrder = tk.Button(self.button_frame, text="Save Order", width=10,command = self.save_order)
        self.btnGenerateInvoice = tk.Button(self.button_frame, text="Generate Invoice", width=10,command = self.generate_invoice)
        self.btnReset = tk.Button(self.button_frame, text="Reset", width=10,command = self.reset_order)
        self.btnExit = tk.Button(self.button_frame, text="Exit",fg="black" ,width=10,command = self.exit)


        for widget in self.button_frame.winfo_children():
            widget.grid_configure(pady = 10,padx = 2)

        self.btnSaveOrder.grid(row=0, column=0)
        self.btnGenerateInvoice.grid(row=0, column=1)
        self.btnReset.grid(row = 0,column = 2)
        self.btnExit.grid(row=0, column=3)


    def on_customer_combobox_select(self,event):
        self.selected_customer_value.set(self.search_customer_combobox.get())
        result = self.search_customer_combobox.get()
        email = (result.split("|")[1]).strip()
        customer = self.utils.get_customer_from_email(email)
        
        self.customer_name.configure(text = f"{customer[1].capitalize()} {customer[2].capitalize()}")
        self.customer_address.configure(text = "{}, {}, {}".format(customer[4],customer[5],customer[6]))



    def show_selected_option(self,option):
        pass
        # print(f"Selected Option: {option}")

    def select_date(self):
        date_window = tk.Toplevel(self.root)
        MyCalendar(date_window,calling_window =self)

    def update_selected_date(self,selected_date,date_type = ""):
        self.selected_date.set(selected_date)
       
        
       
  
    def on_product_combobox_select(self,event):
        self.selected_product_value.set(self.search_product_combobox.get())
    


    def get_customers(self):
        customer_data = []
        customers =self.customer.get_customers()
        for customer_info in customers:
            
            customer_data.append("{} {} | {}".format(customer_info[0],customer_info[1],customer_info[2]))
        return customer_data


    def get_products(self):
        product = []
        
        products =self.product.get_products()
        for product_info in products:
            product.append("{} | {} | {}".format(product_info[0],product_info[1],product_info[2]))
        return product


    def get_items(self):
        product_id_quantity = []
        for item in self.product_display_table.get_children():
            values = self.product_display_table.item(item, 'values')
            product_id = self.product.get_product_id(values[1])
            product_quantity = int(values[3])
            product_id_quantity.append((product_id,product_quantity))
        return(product_id_quantity)
            

    def get_product(self):
        products = []
        for item in self.product_display_table.get_children():
            values = self.product_display_table.item(item, 'values')
            
            products.append((values[1],values[2],values[3],values[4],values[5]))
        return products


    def add_item(self):
        quantity  = int(self.qty_spinbox.get())
        product = self.search_product_combobox.get()
        item = [item.strip() for item in product.split('|')]
        product_code = item[0]
        product_name = item[1]
        product_price = "$" + f"{float(item[2]):.2f}"
        line_total = "$" + f'{quantity * float(item[2]):.2f}'

        invoice_item = [product_code,product_name,quantity,product_price,line_total]

        #insert into the tree table
        self.my_tag = 'gray' if len(self.product_display_table.get_children()) % 2 == 0 else 'normal'

        index = len(self.product_display_table.get_children()) + 1
        self.product_display_table.insert("","end",values =[index] + invoice_item,tags = self.my_tag)
        
    
        self.total_amount += (quantity * float(item[2]))
        self.total_amount_widget.configure(text=f"Total Amount: ${self.total_amount:,.2f}")
        # Update the row displaying the total amount
        # self.update_total_amount_row()

        self.clear_item()

   

    def clear_item(self):
        self.qty_spinbox.delete(0,"end")
        self.search_product_combobox.set("")


    def reset_order(self):
        self.qty_spinbox.delete(0,"end") #reset quantity to 0
        self.search_product_combobox.set("")#clear selected product
        self.search_customer_combobox.set("")#clear selected customer
        self.selected_date.set("")
        self.order_error_message.config(text="")
        self.customer_name.configure(text ="")
        self.customer_address.configure(text ="")
        self.selected_delivery_option.set("pickup") 
        self.total_amount = 0.0
        self.total_amount_widget.configure(text=f"Total Amount: ${self.total_amount:,.2f}")
        for item in self.product_display_table.get_children():
            self.product_display_table.delete(item)#clear the line items



    def save_order(self):

        self.order = Order()
        try: 
            customer_info = self.selected_customer_value.get()
            if customer_info == "":
                raise ValueError("Error: Please select a customer")
            
            if self.product_display_table.get_children() == ():
                raise ProductEmptyError("Please enter at least one product")

            self.customer_email = [item.strip() for item in customer_info.split('|')]

      
            order_info = {'fulfilment_date': self.utils.date_formatter(self.selected_date.get()),
                        'delivery_method':self.selected_delivery_option.get(),
                        'customer':self.customer_email[1],
                        'salesperson': self.user['user_id'],
                        'notes':self.note_entry.get('1.0', 'end-1c'),
                        'products':self.get_items()
                        }
        
        except ValueError as e:
            self.order_error_message.config(text=str(e))
        except DateEmptyError as e:
            self.order_error_message.config(text=str(e))
        except ProductEmptyError as e:
            self.order_error_message.config(text=str(e))

        else:

            status,message = self.order.save_order(order_info)
            if status == "Error":
                self.order_error_message.config(text = message)
            else:
                messagebox.showinfo('Order Creation',message)
                result = messagebox.askyesno("Question","""
                                         Do you want to Generate Invoice for this order?""")
                if result:
                        self.generate_invoice()
                        self.reset_order()
                else:
                        self.reset_order()


 

    def generate_invoice(self):
            cust = self.selected_customer_value.get().split("|")
            cust_email = cust[1].strip()
            customer_data = self.customer.get_customer(cust_email)
            other_info  = [self.fulfilment_date_entry.get(),self.total_amount,self.selected_delivery_option.get()]
            self.report_exporter.export_order_invoice_to_docx(self.order_invoice_template,product_data = self.get_product(),customer_data =customer_data, user_data = self.user,other_info = other_info)
            messagebox.showinfo('Invoice Generation',"Invoice was generated successfully!")
          
          
            
        # except Exception as e:
        #     print('Error occurred while trying to create a report',e)
        # else:
        #     messagebox.showinfo("Success","Report Exported Successfully!")



    def exit(self):
        self.root.destroy()
         

if __name__ == "__main__":
    root = tk.Tk()
    create_order_window = tk.Toplevel(root)
    CreateOrder(create_order_window)
    root.mainloop()