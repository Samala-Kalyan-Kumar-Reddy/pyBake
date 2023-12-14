# This is a sample Report Program. It fetches data from my user_details table to display
from tkinter import ttk
import tkinter as tk
import datetime as dt
from tkinter import messagebox
from controllers.users import User
from controllers.utils import ReportExporter
# from config import ReportTemplate
from ..styles import Style

class UserLoginReport():
    def __init__(self,root,user,report_template = ""):
        self.root =root
        self.login_user = user
        self.root.title("Users Login Report")
        self.all_user = User()
        self.user_login_report_template = ReportExporter.get_users_login_report_template()
        self.report_exporter = ReportExporter()
        

        self.report_frame = tk.Frame(self.root,bg = '#EEEEEE')
        self.report_frame.grid(row=0,column=0)

        

        self.user_info_frame = tk.Frame(self.report_frame, background='#EEEEEE')
        self.user_info_frame.grid(row=0, column=0, sticky="news", padx=20, pady=10)

        self.report_label = tk.Label(self.user_info_frame,bg = '#EEEEEE', text="Report on the Last Login Time of Users", fg = Style.page_heading_color,font='Poppins, 15', anchor="c")
        self.report_label.grid(row=0, column=0)
        date = dt.datetime.now()

        self.date_label = tk.Label(self.user_info_frame, text=f"{date:%A, %B %d, %Y}", font="Poppins, 12", anchor='e')
        self.date_label.grid(row=1, column=0)  # r=1, column = 0

        self.report_body_frame = tk.Frame(self.report_frame, background='white')
        self.report_body_frame.grid(row=1, column=0, padx=10, pady=10)



        self.style = ttk.Style()
        # self.style.theme_use('clam')
        report_font = ['Helvetica', 12, 'bold']
        # Configure the style of Heading in Treeview widget
        self.style.configure('Treeview.Heading', background="lightgray", font=report_font)



        self.tree = ttk.Treeview(self.report_body_frame,column=("1", "2", "3", "4","5"), show='headings')


        self.tree.tag_configure('gray',background='#E0F7FA')
        self.tree.tag_configure('normal', background='white')
        cell_width = 100
        self.tree.column("#1", anchor=tk.CENTER, width = cell_width)
        self.tree.heading("#1", text="FirstName")
        self.tree.column("#2", anchor=tk.CENTER, width = cell_width)
        self.tree.heading("#2", text="LastName")
        self.tree.column("#3", anchor=tk.CENTER, width = 150)
        self.tree.heading("#3", text="Email")
        self.tree.column("#4", anchor=tk.CENTER, width = cell_width)
        self.tree.heading("#4", text="LastLoginDate")
        self.tree.column("#5", anchor=tk.CENTER, width = cell_width)
        self.tree.heading("#5", text="LastLoginTime")
        
      

        #self.tree.grid(row=3, column=0)
        self.tree.pack()

        self.button_frame = tk.Frame(self.report_frame, background="#EEEEEE")
        self.button_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

        self.btnDisplay = tk.Button(self.button_frame, text="Refresh", bg = "#EEEEEE",width=10,command = self.refresh)
        self.btn_export_report_docx = tk.Button(self.button_frame, bg = "#EEEEEE", text="ExportToDoc", width=10,command = self.export_report_doc)
        self.btn_export_report_pdf = tk.Button(self.button_frame,  bg = "#EEEEEE",text="ExportToPDF", width=10,command = self.export_report_pdf)
        self.btnExit = tk.Button(self.button_frame, text="Exit", bg = "#EEEEEE", width=10,command = self.exit)

        self.btnDisplay.grid(row=0, column=0, pady=10)
        self.btn_export_report_docx.grid(row = 0, column = 1, pady = 10)
        self.btn_export_report_pdf.grid(row = 0, column = 2, pady = 10)
        self.btnExit.grid(row=0, column=3,pady=10)


        for widget in self.button_frame.winfo_children():
            widget.grid_configure(padx=10, pady=10)

        self.display()



    def display(self):
        data = self.all_user.get_users_login_info()
        
        #format the date to look better
        self.formatted_data = []

        for item in data :
            formatted_date = item[3].strftime("%b. %d, %Y")
            formatted_time = item[3].strftime("%H:%M:%S")
            formatted_item = [item[0].capitalize(), item[1].capitalize(), item[2], formatted_date,formatted_time]
            self.formatted_data.append(formatted_item)

    
        my_tag = 'normal'
        for user in self.formatted_data:
            if my_tag == 'normal':
                my_tag = 'gray'
            else:
                my_tag = 'normal'
            # #print(row)
            self.tree.insert("", tk.END, values=user,tags = my_tag)

    def export_report_doc(self):
        try:
            self.report_exporter.export_user_login_report_to_docx(self.user_login_report_template,self.formatted_data,other_info = self.login_user)
        except Exception as e:
            print('Error occurred while trying to create a report',e)
        else:
            messagebox.showinfo("Success","Report Exported Successfully!")
    def export_report_pdf(self):
        # self.report_exporter.export_to_pdf(self.user_login_report_template,self.formatted_data,other_info = self.login_user)
        pass

    def refresh(self):
        self.tree.delete(*self.tree.get_children())
        self.display()



    def exit(self):  # Exits the program
        self.root.destroy()



    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    report = UserLoginReport(root)
    report.run()