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
from views.styles import Style


class UpdateOrder(tk.Toplevel):
    def __init__(self, root,user_obj,dashboard):
        self.root = root
        self.user = user_obj
        self.dashboard = dashboard
        self.root.title("Update Order Status")
        self.root.resizable(False,False)
        self.utils = Utils()
        self.order = Order()
        # self.root.geometry("500x400")x


        # self.title_frame = tk.Frame(master = self.root,bg = "#EEEEEE",borderwidth = 1)
        # self.title_frame.pack(padx = 20, pady = (20,0))

     



        self.title_frame = tk.Frame(master = self.root,bg = "#EEEEEE")
        self.title_frame.pack(side="top", fill="x", expand=True)

        self.combo_frame = tk.Frame(master = self.root,bg = "#EEEEEE")
        self.combo_frame.pack(padx = 20, pady = (20,0),expand =True,fill = "x")

        self.order_info_frame = tk.Frame(master = self.root,bg = "#EEEEEE")
        self.order_info_frame.pack(padx = 20, pady = (20,0),expand =True,fill = "x")

        self.order_info_frame_section_1 = tk.Frame(master = self.order_info_frame,width = 150)
        self.order_info_frame_section_1.grid(row = 0, column = 0 ,sticky = 'w')

        self.order_info_frame_section_2 = tk.Frame(master = self.order_info_frame,width = 150)
        self.order_info_frame_section_2.grid(row = 0, column = 1,sticky = 'e')

        self.old_order_note_frame = tk.Frame(master = self.root,bg = "#EEEEEE")
        self.old_order_note_frame.pack(padx = 20,pady=(5,5),anchor='w')


        self.order_status_frame = tk.Frame(master = self.root,bg = "#EEEEEE")
        self.order_status_frame.pack(padx = 20,pady = 20)

        self.order_error_frame = tk.Frame(master = self.root,bg = "#EEEEEE")
        self.order_error_frame.pack(padx = 20)

        self.product_frame = tk.Frame(master = self.root,bg = "#EEEEEE")
        self.product_frame.pack(padx = 20)

        self.notes_frame = tk.Frame(master = self.root,bg = "#EEEEEE")
        self.notes_frame.pack(padx = 20, pady = (0,20) ,expand =True,fill = "x")


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
        self.selected_order_value = tk.StringVar()
        self.selected_order_status = tk.StringVar()
        self.selected_customer_id = 0
        self.initial_order_status = ""



        #ERROR MESSAGE
        # self.order_error_message = tk.Label(self.order_error_frame, text = "",bg = "#FFEBEE")
        # self.order_error_message.grid(row = 0, column =0,columnspan = 4,sticky = 'news')

        #FOR CUSTOMER

        self.tk_image = Utils.resize_image((50,50),'images/order/checklist.png')
        # Create a Label widget with the resized image
        self.title_image = tk.Label(self.title_frame, image=self.tk_image)
        self.title_image.pack(side = "right", padx=(0,40),pady =(20,0))
        tk.Label(self.title_frame, text = "Update Order Status",font = Style.page_heading,fg = Style.page_heading_color).pack(side = 'left',padx = (40,0), pady =(20,0))

        



        tk.Label(self.combo_frame, text="Select Customer:").grid(row = 0, column =0,sticky = "W")
        self.search_customer_combobox = ttk.Combobox(self.combo_frame,width = 30, values=self.get_customers())
        self.search_customer_combobox.grid(row = 1, column =0)
        self.search_customer_combobox.bind("<<ComboboxSelected>>", self.on_customer_combobox_select)        
        # self.first_name_entry.grid(row = 1, column = 1,padx=10,pady=5)


        #FOR ORDERS

        tk.Label(self.combo_frame, text="Select Customer Order:").grid(row = 0, column =1,padx = 20,sticky = "W")
       
        self.search_order_combobox = ttk.Combobox(self.combo_frame,width = 30, values=[])
        self.search_order_combobox.grid(row = 1, column =1,padx = 20,sticky='W')
        self.search_order_combobox.bind("<<ComboboxSelected>>", self.on_order_combobox_select) 

        


        #display order information
        tk.Label(self.order_info_frame_section_1,text = "Order Status:", font = ("helvetica",12,'bold')).grid(row = 0, column = 0,sticky = "E")
        self.order_status = tk.Label(self.order_info_frame_section_1,text = "")
        self.order_status.grid(row = 0, column = 1,sticky = "W")


        tk.Label(self.order_info_frame_section_1,text = "Order Date:", font = ("helvetica",12,'bold')).grid(row = 1, column = 0,sticky = "E")
        self.order_date = tk.Label(self.order_info_frame_section_1,text = "")
        self.order_date.grid(row = 1,column =1,sticky = "W")

        tk.Label(self.order_info_frame_section_1,text = "Order Amount:", font = ("helvetica",12,'bold')).grid(row = 2, column = 0,sticky = "E")
        self.order_amount = tk.Label(self.order_info_frame_section_1,text = "")
        self.order_amount.grid(row = 2, column = 1,sticky = "W")
        
        
        tk.Label(self.order_info_frame_section_1,text = "Total Quantity:", font = ("helvetica",12,'bold')).grid(row = 3, column = 0,sticky = "E")
        self.total_quantity = tk.Label(self.order_info_frame_section_1,text = "")
        self.total_quantity.grid(row = 3, column = 1,sticky = "W")



        #display customer information
        tk.Label(self.order_info_frame_section_2, text = "Customer Name:",font = ("helvetica",12,'bold')).grid(row = 0, column = 0,sticky = "E")
        self.customer_name = tk.Label(self.order_info_frame_section_2,text = "")
        self.customer_name.grid(row = 0, column = 1,sticky = "W")

        tk.Label(self.order_info_frame_section_2,text = "Customer Address:", font = ("helvetica",12,'bold')).grid(row = 1, column = 0,sticky = "E")
        self.customer_address = tk.Label(self.order_info_frame_section_2,text = "")
        self.customer_address.grid(row = 1, column = 1,sticky = "W")
        

        tk.Label(self.order_info_frame_section_2,text = "Sales Person:", font = ("helvetica",12,'bold')).grid(row = 2, column = 0,sticky = "E")
        self.sales_person = tk.Label(self.order_info_frame_section_2,text = "")
        self.sales_person.grid(row = 2, column = 1,sticky = "W")

        tk.Label(self.order_info_frame_section_2,text = "Delivery Method:", font = ("helvetica",12,'bold')).grid(row = 3, column = 0,sticky = "E")
        self.delivery_method = tk.Label(self.order_info_frame_section_2,text = "")
        self.delivery_method.grid(row = 3, column = 1,sticky = "W")



        tk.Label(self.old_order_note_frame,text = "Order Notes:", font = ("helvetica",12,'bold')).grid(row = 0, column = 0,sticky = "W")
        self.order_notes = tk.Label(self.old_order_note_frame,text = "")
        self.order_notes.grid(row = 0, column = 1, columnspan = 3,sticky = "E")
        


        #select status
        tk.Label(self.order_status_frame, text="Select Order Status:").grid(row = 0, column =0,sticky = "W")
        self.select_order_status_combobox = ttk.Combobox(self.order_status_frame,width = 30, values=self.get_order_status())
        self.select_order_status_combobox.grid(row = 1, column =0)
        self.select_order_status_combobox.bind("<<ComboboxSelected>>", self.on_customer_combobox_select)

        tk.Button(master = self.order_status_frame,text = "Update Status",command = self.update_status).grid(row = 1,column = 1)        
        # self.first_name_entry.grid(row = 1, column = 1,padx=10,pady=5)



       #NOTES
        tk.Label(self.notes_frame, text="Notes:",font = ('helvetica', 12)).grid(row = 1, column = 0,sticky='W')
        self.note_entry = tk.Text(self.notes_frame,font = ('helvetica', 11),height=2)
        self.note_entry.grid(row=1, column=1,columnspan = 3,sticky='E')


        #BUTTONS

        # self.btnSaveOrder = tk.Button(self.button_frame, text="Save Order", width=10,command = self.save_order)
        # self.btnGenerateInvoice = tk.Button(self.button_frame, text="Generate Invoice", width=10,command = self.generate_invoice)
        # self.btnReset = tk.Button(self.button_frame, text="Reset", width=10,command = self.reset_order)
        self.btnExit = tk.Button(self.button_frame, text="Exit",fg="black" ,width=10,command = self.exit)


        # for widget in self.button_frame.winfo_children():
        #     widget.grid_configure(pady = 10,padx = 2)

        # self.btnSaveOrder.grid(row=0, column=0)
        # self.btnGenerateInvoice.grid(row=0, column=1)
        # self.btnReset.grid(row = 0,column = 2)
        self.btnExit.grid(row=0, column=3,pady = 20)


    def on_customer_combobox_select(self,event):
        self.selected_customer_value.set(self.search_customer_combobox.get())
        result = self.search_customer_combobox.get()
        email = (result.split("|")[1]).strip()
        customer = self.utils.get_customer_from_email(email)
        
        self.customer_name.configure(text = f"{customer[1].capitalize()} {customer[2].capitalize()}")
        self.customer_address.configure(text = "{}, {}, {}".format(customer[4],customer[5],customer[6]))
        self.selected_customer_id = customer[0]
        orders = self.get_customer_orders(self.selected_customer_id)
        self.search_order_combobox['values'] = orders
        # self.search_order_combobox.set('')
        



    #open the datepicker to select date
    def select_date(self):
        date_window = tk.Toplevel(self.root)
        MyCalendar(date_window,calling_window =self)

    def update_selected_date(self,selected_date):
        self.selected_date.set(selected_date)
       
        
       
  
    def on_order_combobox_select(self,event):
        self.selected_order_value.set(self.search_order_combobox.get())
        order_id = self.search_order_combobox.get().split(" ")
        self.initial_order_status = (self.search_order_combobox.get().split('|')[2]).strip()
        print(self.initial_order_status)
        order_id = int(order_id[0])
        

        #get the entire order object
        order = self.utils.get_order_from_orderid(order_id)

        #display order information
       
        self.order_date.configure(text = order[1].strftime("%b. %d, %Y %H:%M"))
        self.order_amount.configure(text = f"${order[8]}")
        self.total_quantity.configure(text = order[7])
        if order[6] in ['created','paid','completed']:
            self.order_status.configure(text = order[6].capitalize(),fg = "green",font = ('helvetica',14,'bold'))
        elif order[6] in ['in progress','on hold','pending payment']:
            self.order_status.configure(text = order[6].capitalize(),fg = "orange",font = ('helvetica',14,'bold'))
        elif order[6]  == 'cancelled':
            self.order_status.configure(text = order[6].capitalize(),fg = "red",font = ('helvetica',14,'bold'))
        else:
            self.order_status.configure(text = order[6].capitalize(),fg = 'blue',font = ('helvetica',14,'bold'))

        self.delivery_method.configure(text = order[2].capitalize())
        self.sales_person.configure(text = f"{order[4].capitalize()} {order[5].capitalize()}")
        self.order_notes.configure(text = order[9])
        




    def on_order_status_combobox_select(self,event):
        self.selected_order_status.set(self.selected_order_status_combobox.get())


    def get_order_status(self):
        all_status = self.utils.get_order_status()
        # print('original:', all_status)
       
        status = [status[0] for status in all_status]
        # print('list comprehended: ',status)
        return status

    
    def get_customers(self):
        customer_email = []
        customer = Customer()
        customers =customer.get_customers()
        for customer_info in customers:
            
            customer_email.append("{} {} | {}".format(customer_info[0],customer_info[1],customer_info[2]))
        return customer_email

    
    # def get_customer_orders(self):
    #     print("The selected customer id is in the order section is:",self.selected_customer_id)
    #     print('The type of the selected value is:',type(self.selected_customer_id))
    #     customer = self.selected_customer_id
    #     if customer == 0:
    #         print("Do nothing")
    #     else:
    #         orders =self.order.get_orders(customer)
    #         print("The orders are",orders)
    #     return orders
   
        
    def get_customer_orders(self,customer):
        order_info = []
        customer = self.selected_customer_id
        if customer == 0:
            print("Do nothing")
        else:
            orders =self.order.get_orders(customer)
            for order in orders:
                order_info.append("{} | {} | {}".format(order[0],order[1],order[2]))

            return order_info




    def update_status(self):
        #get the selected value


        status_update_info = {'status':self.select_order_status_combobox.get(),
        'order':self.search_order_combobox.get().split(" ")[0],
        'user':self.user['user_id'],
        'notes':self.note_entry.get('1.0', 'end-1c')
        }
        print(status_update_info['status'])
        print(self.initial_order_status)
        if status_update_info['status'] == self.initial_order_status:
            messagebox.showerror("Error","Please select a new status from the list!")
        else:
            status,message = self.order.update_order_status(status_update_info)
            if status == "Error":
                self.error_messsage.configure(text = message)
            elif status == "success":
                messagebox.showinfo("Success",message)
                self.root.destroy()

    # def get_items(self):
    #     product_id_quantity = []
    #     for item in self.product_display_table.get_children():
    #         values = self.product_display_table.item(item, 'values')
    #         product_id = self.product.get_product_id(values[1])
    #         product_quantity = int(values[3])
    #         product_id_quantity.append((product_id,product_quantity))
    #     return(product_id_quantity)
            


    # def add_item(self):
    #     quantity  = int(self.qty_spinbox.get())
    #     product = self.search_product_combobox.get()
    #     item = [item.strip() for item in product.split('|')]
    #     product_code = item[0]
    #     product_name = item[1]
    #     product_price = "$" + f"{float(item[2]):.2f}"
    #     line_total = "$" + f'{quantity * float(item[2]):.2f}'

    #     invoice_item = [product_code,product_name,quantity,product_price,line_total]

    #     #insert into the tree table
    #     self.my_tag = 'gray' if len(self.product_display_table.get_children()) % 2 == 0 else 'normal'

    #     index = len(self.product_display_table.get_children()) + 1
    #     self.product_display_table.insert("","end",values =[index] + invoice_item,tags = self.my_tag)
        
    
    #     self.total_amount += (quantity * float(item[2]))
    #     self.total_amount_widget.configure(text=f"Total Amount: ${self.total_amount:,.2f}")
    #     # Update the row displaying the total amount
    #     # self.update_total_amount_row()

    #     self.clear_item()

   

    # def clear_item(self):
    #     self.qty_spinbox.delete(0,"end")
    #     self.search_product_combobox.set("")


    # def reset_order(self):
    #     self.qty_spinbox.delete(0,"end") #reset quantity to 0
    #     self.search_product_combobox.set("")#clear selected product
    #     self.search_customer_combobox.set("")#clear selected customer
    #     self.selected_date.set("")
    #     self.order_error_message.config(text="")
    #     self.customer_name.configure(text ="")
    #     self.customer_address.configure(text ="")
    #     self.selected_delivery_option.set("pickup") 
    #     self.total_amount = 0.0
    #     self.total_amount_widget.configure(text=f"Total Amount: ${self.total_amount:,.2f}")
    #     for item in self.product_display_table.get_children():
    #         self.product_display_table.delete(item)#clear the line items



    # def save_order(self):

    #     self.order = Order()
    #     customer_info = self.selected_customer_value.get()
       
        
    #     self.customer_email = [item.strip() for item in customer_info.split('|')]

    #     order_info = {'fulfilment_date': self.utils.date_formatter(self.selected_date.get()),
    #                 'delivery_method':self.selected_delivery_option.get(),
    #                 'customer':self.customer_email[1],
    #                 'salesperson': self.user['user_id'],
    #                 'notes':self.note_entry.get('1.0', 'end-1c'),
    #                 'products':self.get_items()
    #                 }

    #     status,message = self.order.save_order(order_info)
    #     if status == "Error":
    #         self.order_error_message.config(text = message)
    #     else:
    #         messagebox.showinfo('Order Creation',message)
    #         self.reset_order()


    # def generate_invoice(self):
    #     pass



    def exit(self):
        self.root.destroy()
         

if __name__ == "__main__":
    root = tk.Tk()
    update_order_window = tk.Toplevel(root)
    UpdateOrder(update_order_window)
    root.mainloop()