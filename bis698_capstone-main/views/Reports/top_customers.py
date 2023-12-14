# This is a sample Report Program. It fetches data from my user_details table to display
from tkinter import ttk
import tkinter as tk
import datetime as dt
from controllers.users import User
from controllers.customers import Customer
from controllers.utils import Utils

class TopCustomerReport():
    def __init__(self,root,user):
        self.root =root
        self.user = user
        self.root.title("Top Customer Report")
        self.customer = Customer()
        # self.utils = Utils()

        self.report_frame = tk.Frame(self.root,background = "#EEEEEE")
        self.report_frame.pack()

        self.customer_info_frame = tk.Frame(self.report_frame, background='#EEEEEE')
        self.customer_info_frame.grid(row=0, column=0, sticky="news", padx=20, pady=10)

        self.report_label = tk.Label(self.customer_info_frame, text="Report on Top Customers", font='Poppins, 15', anchor="c")
        self.report_label.grid(row=0, column=0)
        date = dt.datetime.now()

        self.date_label = tk.Label(self.customer_info_frame, text=f"{date:%A, %B %d, %Y}", font="Poppins, 12", anchor='e')
        self.date_label.grid(row=1, column=0)  # r=1, column = 0

        self.report_body_frame = tk.Frame(self.report_frame, background='white')
        self.report_body_frame.grid(row=1, column=0, sticky="news", padx=10, pady=10)


        self.button_frame = tk.Frame(self.report_frame, background='#EEEEEE')
        self.button_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)


        self.style = ttk.Style()
        # self.style.theme_use('clam')
        report_font = ['Helvetica', 12, 'bold']
        # Configure the style of Heading in Treeview widget
        self.style.configure('Treeview.Heading', background="lightgray", font=report_font)


        
        self.tree = ttk.Treeview(self.report_body_frame,column=("1", "2", "3", "4", "5","6"), show='headings')


        self.tree.tag_configure('gray', background='#EEEEEE')
        self.tree.tag_configure('normal', background='white')

        cell_width = 100
        self.tree.column("#1", anchor=tk.CENTER,width = cell_width)
        self.tree.heading("#1", text="Customer Name")
        self.tree.column("#2", anchor=tk.CENTER,width = cell_width)
        self.tree.heading("#2", text="Email")
        self.tree.column("#3", anchor=tk.CENTER,width = cell_width)
        self.tree.heading("#3", text="City")
        self.tree.column("#4", anchor=tk.CENTER,width = 150)
        self.tree.heading("#4", text="State")
        self.tree.column("#5", anchor=tk.CENTER,width = cell_width)
        self.tree.heading("#5", text="Total Orders")
        self.tree.column("#6", anchor=tk.CENTER,width = cell_width)
        self.tree.heading("#6", text="Total Purchase Amount")
   
      

        #self.tree.grid(row=3, column=0)
        self.tree.pack()

        

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
        print(self.customer)
        data = self.customer.top_customers()

        formatted_data = []

        for item in data :
            formatted_amount = f"${item[5]}"
            name = item[0].split(" ")
            formatted_name = [item.capitalize() for item in name]
            formatted_item = (
                formatted_name,
                item[1],
                item[2],
                item[3],
                item[4],
                formatted_amount)
            formatted_data.append(formatted_item)

    

    
        my_tag = 'normal'
        for user in formatted_data:
            if my_tag == 'normal':
                my_tag = 'gray'
            else:
                my_tag = 'normal'
            # #print(row)
            self.tree.insert("", tk.END, values=user,tags = my_tag)

    def refresh(self):
        self.tree.delete(*self.tree.get_children())
        self.display()

    def export_to_pdf(self):
        pass
        # self.utils.export_to_pdf()


    def exit(self):  # Exits the program
        self.root.destroy() 



    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    report = TopCustomerReport(root)
    report.run()