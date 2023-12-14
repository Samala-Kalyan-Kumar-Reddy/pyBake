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

class CustomerOrderDetailsReport():
    def __init__(self,root,user,order):
        self.root =root
        self.user = user
        self.order = order
        self.root.title("Customer Order History Report")
        # self.order = Order()
        self.utils = Utils()

        
           
        
        

        self.report_frame = tk.Frame(self.root,background = "#EEEEEE")
        self.report_frame.pack()

        self.customer_info_frame = tk.Frame(self.report_frame, background='#EEEEEE')
        self.customer_info_frame.grid(row=0, column=0, sticky="news", padx=20, pady=10)

        self.report_filter_frame = tk.LabelFrame(self.report_frame, background='#EEEEEE')
        self.report_filter_frame.grid(row=1, column=0, sticky="news", padx=10, pady=10)

        
        self.report_body_frame = tk.Frame(self.report_frame, background='white')
        self.report_body_frame.grid(row=2, column=0, sticky="news", padx=10, pady=10)


        self.button_frame = tk.Frame(self.report_frame, background='#EEEEEE')
        self.button_frame.grid(row=3, column=0, sticky="news", padx=20, pady=10)


        self.report_label = tk.Label(self.customer_info_frame, text="Customer Order History Report", font='Poppins, 15', anchor="c")
        self.report_label.grid(row=0, column=0)
        date = dt.datetime.now()

        self.date_label = tk.Label(self.customer_info_frame, text=f"{date:%A, %B %d, %Y}", font="Poppins, 12", anchor='e')
        self.date_label.grid(row=1, column=0)  # r=1, column = 0



        # self.start_date_entry = tk.Entry(self.report_filter_frame, width = 15, textvariable = self.selected_start_date)
        # self.start_date_entry.grid(row = 1 ,column = 0, padx = 0, sticky = 'w')
        # self.start_date_button = tk.Button(self.report_filter_frame,text = "select Start Date",command =self.select_start_date)
        # self.start_date_button.grid(row = 0, column = 0, padx = 0, sticky = 'w')

        # tk.Label(self.report_filter_frame,text = "to").grid(row =1, column =1)
        # self.end_date_entry = tk.Entry(self.report_filter_frame, width = 15, textvariable = self.selected_end_date)
        # self.end_date_entry.grid(row = 1 ,column = 2, padx = 0, sticky = 'E')
        # self.end_date_button = tk.Button(self.report_filter_frame,text = "select End Date",command =self.select_end_date)
        # self.end_date_button.grid(row = 0, column = 2, padx = 0, sticky = 'e')

       

        # tk.Label(self.report_filter_frame, text="Order Status:").grid(row = 0, column =3,sticky = "W")
        # self.select_order_status_combobox = ttk.Combobox(self.report_filter_frame,width = 30, values=self.get_order_status())
        # self.select_order_status_combobox.grid(row = 1, column =3)
        # # self.select_order_status_combobox.bind("<<ComboboxSelected>>", self.on_customer_combobox_select)

        # self.go_button = tk.Button(self.report_filter_frame,text = "Go",command =self.go)
        # self.go_button.grid(row = 0, column = 4, padx = 0, sticky = 'e')

        # self.clear_filter_button = tk.Button(self.report_filter_frame,text = "Clear Filter",command =self.clear_filter)
        # self.clear_filter_button.grid(row = 1, column = 4, padx = 0, sticky = 'e')




        

        self.style = ttk.Style()
        # self.style.theme_use('clam')
        report_font = ['Helvetica', 12, 'bold']
        # Configure the style of Heading in Treeview widget
        self.style.configure('Treeview.Heading', background="lightgray", font=report_font)


        
        self.order_display = ttk.Treeview(self.report_body_frame,column=("1", "2", "3", "4", "5","6"), show='headings')


        self.order_display.tag_configure('gray', background='#EEEEEE')
        self.order_display.tag_configure('normal', background='white')

        cell_width = 120
        self.order_display.column("#1", anchor=tk.CENTER,width = cell_width)
        self.order_display.heading("#1", text="Order ID")
        self.order_display.column("#2", anchor=tk.CENTER,width = 200)
        self.order_display.heading("#2", text="Order Status")
        self.order_display.column("#3", anchor=tk.CENTER,width = cell_width)
        self.order_display.heading("#3", text="Date Updated")
        self.order_display.column("#4", anchor=tk.CENTER,width = 100)
        self.order_display.heading("#4", text="Time Updated")
        self.order_display.column("#5", anchor=tk.CENTER,width = cell_width)
        self.order_display.heading("#5", text="Updated By")
        self.order_display.column("#6", anchor=tk.CENTER,width = 200)
        self.order_display.heading("#6", text="Update Note")
        
   
      

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

        self.display()



       
    def display(self):
        order_id = self.order[0]
        history_data = self.utils.get_order_history(order_id)
        formatted_data = []

        for item in history_data :
            status = item[2].capitalize()
            user = [item.capitalize() for item in  item[1].split(" ")]
            # date_object = datetime.strptime(item[4], '%m/%d/%y')
            date_updated = item[3].strftime("%b. %d, %Y")
            time_updated = item[3].strftime("%H:%M")
            
            formatted_item = (
                item[0],
                status,
                date_updated,
                time_updated,
                user,
                item[4])
            formatted_data.append(formatted_item)

    
        my_tag = 'normal'
        for order_history in formatted_data:
            if my_tag == 'normal':
                my_tag = 'gray'
            else:
                my_tag = 'normal'
            self.order_display.insert("", tk.END, values=order_history,tags = my_tag)
   

   

    def refresh(self):
        self.order_display.delete(*self.order_display.get_children())
        self.display()
    

    def export_to_pdf(self):
        pass
        # self.utils.export_to_pdf()


    def exit(self):  # Exits the program
        self.root.destroy() 


    def refresh(self):
        self.display()


    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    report = CustomerOrderDetailsReport(root)
    report.run()