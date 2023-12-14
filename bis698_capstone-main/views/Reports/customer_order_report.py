# This is a sample Report Program. It fetches data from my user_details table to display
from tkinter import ttk
import tkinter as tk
import datetime as dt
from controllers.users import User
from controllers.customers import Customer
from controllers.orders import Order
from controllers.utils import Utils
from datetime import datetime
from controllers.utils import MyCalendar
from .customer_order_detail_report import CustomerOrderDetailsReport

class CustomerOrderReport():
    def __init__(self,root,user):
        self.root =root
        self.user = user
        self.root.title("Customer Order Report")
        self.order = Order()
        self.utils = Utils()

        self.selected_start_date = tk.StringVar()
        self.selected_end_date = tk.StringVar()
        self.selected_order_status = tk.StringVar()
    
        
        # self.utils = Utils()

        self.report_frame = tk.Frame(self.root,background = "#EEEEEE")
        self.report_frame.pack()

        custom_style = ttk.Style()
        custom_style.configure("Custom.TSeparator", background="red", thickness=3)

# Create a separator using the custom style
        separator = ttk.Separator(self.report_frame, orient="horizontal", style="Custom.TSeparator")
        separator.grid(row = 0 , column = 0, columnspan = 4)

        self.customer_info_frame = tk.Frame(self.report_frame, background='#EEEEEE')
        self.customer_info_frame.grid(row=0, column=0, sticky="news", padx=20, pady=10)

        self.report_filter_frame = tk.LabelFrame(self.report_frame, background='#EEEEEE')
        self.report_filter_frame.grid(row=1, column=0, sticky="news", padx=10, pady=10)

        
        self.report_body_frame = tk.Frame(self.report_frame, background='white')
        self.report_body_frame.grid(row=2, column=0, sticky="news", padx=10, pady=10)


        self.button_frame = tk.Frame(self.report_frame, background='#EEEEEE')
        self.button_frame.grid(row=3, column=0, sticky="news", padx=20, pady=10)


        self.report_label = tk.Label(self.customer_info_frame, text="Report on Customer Orders", font='Poppins, 15', anchor="c")
        self.report_label.grid(row=0, column=0)
        date = dt.datetime.now()

        self.date_label = tk.Label(self.customer_info_frame, text=f"{date:%A, %B %d, %Y}", font="Poppins, 12", anchor='e')
        self.date_label.grid(row=1, column=0)  # r=1, column = 0



        self.start_date_entry = tk.Entry(self.report_filter_frame, width = 15, textvariable = self.selected_start_date)
        self.start_date_entry.grid(row = 1 ,column = 0, padx = 0, sticky = 'w')
        self.start_date_button = tk.Button(self.report_filter_frame,text = "select Start Date",command =self.select_start_date)
        self.start_date_button.grid(row = 0, column = 0, padx = 0, sticky = 'w')

        tk.Label(self.report_filter_frame,text = "to").grid(row =1, column =1)
        self.end_date_entry = tk.Entry(self.report_filter_frame, width = 15, textvariable = self.selected_end_date)
        self.end_date_entry.grid(row = 1 ,column = 2, padx = 0, sticky = 'E')
        self.end_date_button = tk.Button(self.report_filter_frame,text = "select End Date",command =self.select_end_date)
        self.end_date_button.grid(row = 0, column = 2, padx = 0, sticky = 'e')

       

        tk.Label(self.report_filter_frame, text="Order Status:").grid(row = 0, column =3,sticky = "W")
        self.select_order_status_combobox = ttk.Combobox(self.report_filter_frame,width = 30, values=self.get_order_status())
        self.select_order_status_combobox.grid(row = 1, column =3)
        # self.select_order_status_combobox.bind("<<ComboboxSelected>>", self.on_customer_combobox_select)

        self.go_button = tk.Button(self.report_filter_frame,text = "Go",command =self.go)
        self.go_button.grid(row = 0, column = 4, padx = 0, sticky = 'e')

        self.clear_filter_button = tk.Button(self.report_filter_frame,text = "Clear Filter",command =self.clear_filter)
        self.clear_filter_button.grid(row = 1, column = 4, padx = 0, sticky = 'e')




        

        self.style = ttk.Style()
        # self.style.theme_use('clam')
        report_font = ['Helvetica', 12, 'bold']
        # Configure the style of Heading in Treeview widget
        self.style.configure('Treeview.Heading', background="lightgray", font=report_font)


        
        self.order_display = ttk.Treeview(self.report_body_frame,column=("1", "2", "3", "4", "5","6","7"), show='headings')


        self.order_display.tag_configure('gray', background='#EEEEEE')
        self.order_display.tag_configure('normal', background='white')

        cell_width = 120
        self.order_display.column("#1", anchor=tk.CENTER,width = cell_width)
        self.order_display.heading("#1", text="Order ID")
        self.order_display.column("#2", anchor=tk.CENTER,width = cell_width)
        self.order_display.heading("#2", text="Order Date")
        self.order_display.column("#3", anchor=tk.CENTER,width = cell_width)
        self.order_display.heading("#3", text="Customer")
        self.order_display.column("#4", anchor=tk.CENTER,width = 150)
        self.order_display.heading("#4", text="Sales Person")
        self.order_display.column("#5", anchor=tk.CENTER,width = cell_width)
        self.order_display.heading("#5", text="Order Fulfillment Date")
        self.order_display.column("#6", anchor=tk.CENTER,width = cell_width)
        self.order_display.heading("#6", text="Delivery Method")
        self.order_display.column("#7", anchor=tk.CENTER,width = cell_width)
        self.order_display.heading("#7", text="Status")
   
      

        #self.order_display.grid(row=3, column=0)
        self.order_display.pack()

        

        self.btnDisplay = tk.Button(self.button_frame, text="Refresh", width=10,command = self.refresh)
        self.btnExportPDF = tk.Button(self.button_frame, text="Export to PDF", width=10,command = self.export_to_pdf)
        self.btnExit = tk.Button(self.button_frame, text="Exit", width=10,command = self.exit)

        self.btnDisplay.grid(row=0, column=0, pady=10)
        self.btnExportPDF.grid(row=0, column=1,pady=10)
        self.btnExit.grid(row=0, column=2,pady=10)


        for widget in self.button_frame.winfo_children():
            widget.grid_configure(padx=10, pady=10)

        self.display(start_date = '1900-01-01',end_date = '9999-12-31',status = None)



       


    def display(self,start_date,end_date,status):
        data = self.order.get_customer_order(start_date,end_date,status)

        formatted_data = []

        for item in data :
            formatted_order_date = item[1].strftime("%b. %d, %Y")
            customer = [item.capitalize() for item in  item[2].split(" ")]
            salesperson = [item.capitalize() for item in  item[3].split(" ")]
            # date_object = datetime.strptime(item[4], '%m/%d/%y')
            formatted_order_fulfilment_date = item[4].strftime("%b. %d, %Y")
            formatted_item = (
                item[0],
                formatted_order_date,
                customer,
                salesperson,
                formatted_order_fulfilment_date,
                item[5],
                item[6])
            formatted_data.append(formatted_item)

    
        my_tag = 'normal'
        for user in formatted_data:
            if my_tag == 'normal':
                my_tag = 'gray'
            else:
                my_tag = 'normal'
            # #print(row)
            self.order_display.insert("", tk.END, values=user,tags = my_tag)
            self.order_display.bind("<ButtonRelease-1>", self.show_order_details)

    #showing details of order_displayview items
    def show_order_details(self,event): 
        self.selected_item = self.order_display.focus()
        item_data = self.order_display.item(self.selected_item)
       
        self.order = item_data
        self.order = self.order['values']
        detail_window = tk.Toplevel(self.root)
        CustomerOrderDetailsReport(detail_window,self.user,self.order)


    def select_start_date(self):
        start_date_window = tk.Toplevel(self.root)
        MyCalendar(start_date_window,calling_window =self,date_type = 'start')

    def update_selected_date(self,selected_date,date_type):
        if date_type == 'start':
            self.selected_start_date.set(selected_date)
        elif date_type == 'end':
            self.selected_end_date.set(selected_date)
       


    def select_end_date(self):
        end_date_window = tk.Toplevel(self.root)
        MyCalendar(end_date_window,calling_window =self,date_type = 'end')

    def on_order_status_combobox_select(self,event):
        self.selected_order_status.set(self.select_order_status_combobox.get())


    def get_order_status(self):
        all_status = self.utils.get_order_status()
        # print('original:', all_status)
       
        status = [status[0] for status in all_status]
        # print('list comprehended: ',status)
        return status



    def refresh(self):
        for item in self.order_display.get_children():
            self.order_display.delete(item)
       
        start_date = '1900-01-01'      
        end_date = '9999-12-31'
        status = None

        self.display(start_date,end_date,status)



    def go(self):
        for item in self.order_display.get_children():
            self.order_display.delete(item)
        start_date = self.selected_start_date.get()
        if start_date == "":
            start_date = '1900-01-01'
        else:
            start_date = self.utils.date_formatter(start_date)      
          
        end_date = self.selected_end_date.get() 
        if end_date == "":
            end_date = '9999-12-31'
        else:
            end_date = self.utils.date_formatter(end_date)
        order_status = self.select_order_status_combobox.get()
        self.display(start_date,end_date,order_status)
       
      
    def clear_filter(self):
        self.selected_start_date.set("")
        self.selected_end_date.set("")
        self.select_order_status_combobox.set("")

    def export_to_pdf(self):
        pass
        # self.utils.export_to_pdf()


    def exit(self):  # Exits the program
        self.root.destroy() 



    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    report = CustomerOrderReport(root)
    report.run()