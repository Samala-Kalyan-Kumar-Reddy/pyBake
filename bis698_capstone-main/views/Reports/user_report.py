# This is a sample Report Program. It fetches data from my user_details table to display
from tkinter import ttk
import tkinter as tk
import datetime as dt
from controllers.users import User
from controllers.utils import Utils
from views.styles import Style

class UserReport():
    def __init__(self,root,admin_dashboard):
        self.root =root
        self.root.title("User Report")
        self.user = User()
        # self.utils = Utils()

        self.report_frame = tk.Frame(self.root,bg = "#EEEEEE")
        self.report_frame.pack()

        self.user_info_frame = tk.Frame(self.report_frame, background= "#EEEEEE")
        self.user_info_frame.grid(row=0, column=0, sticky="news", padx=20, pady=10)

        self.report_label = tk.Label(self.user_info_frame, text="Report of the Users in the System", bg = "#EEEEEE",font='Poppins, 15', fg = Style.page_heading_color,anchor="c")
        self.report_label.grid(row=0, column=0)
        date = dt.datetime.now()

        self.date_label = tk.Label(self.user_info_frame, text=f"{date:%A, %B %d, %Y}", background =  "#EEEEEE",font="Poppins, 12", anchor='e',fg = Style.page_heading_color)
        self.date_label.grid(row=1, column=0)  # r=1, column = 0

        self.report_body_frame = tk.Frame(self.report_frame, background="white")
        self.report_body_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

        self.button_frame = tk.Frame(self.report_frame,background='#EEEEEE')
        self.button_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)



        self.style = ttk.Style()
        # self.style.theme_use('clam')
        report_font = ['Helvetica', 12, 'bold']
        # Configure the style of Heading in Treeview widget
        self.style.configure('Treeview.Heading', background='#B2EBF2', font=report_font)



        self.tree = ttk.Treeview(self.report_body_frame,column=("1", "2", "3", "4", "5","6","7"), show='headings')


        self.tree.tag_configure('gray', background='#E1F5FE')
        self.tree.tag_configure('normal', background='white')

        cell_width = 100
        self.tree.column("#1", anchor = tk.W,width = cell_width)
        self.tree.heading("#1", text="First Name")
        self.tree.column("#2", anchor = tk.CENTER,width = cell_width)
        self.tree.heading("#2", text="Middle I.")
        self.tree.column("#3", anchor = tk.W,width = cell_width)
        self.tree.heading("#3", text="Last Name")
        self.tree.column("#4", anchor = tk.W,width = 150)
        self.tree.heading("#4", text="Email")
        self.tree.column("#5", anchor = tk.CENTER,width = cell_width)
        self.tree.heading("#5", text="Role")
        self.tree.column("#6", anchor = tk.CENTER,width = cell_width)
        self.tree.heading("#6", text="Status")
        self.tree.column("#7", anchor = tk.W,width = cell_width)
        self.tree.heading("#7", text="Date Hired")
      

        #self.tree.grid(row=3, column=0)
        self.tree.pack()

        

        self.btnDisplay = tk.Button(self.button_frame, text="Refresh", width=10,command = self.refresh)
        self.btnExportPDF = tk.Button(self.button_frame, text="Export to PDF", width=10,command = self.export_to_pdf)
        self.btnExportWord = tk.Button(self.button_frame, text="Export to Word", width=10,command = self.export_to_word)
        self.btnExit = tk.Button(self.button_frame, text="Exit", width=10,command = self.exit)

        self.btnDisplay.grid(row=0, column=0)
        self.btnExportPDF.grid(row=0, column=1)
        self.btnExportWord.grid(row=0, column=2)
        self.btnExit.grid(row=0, column=3)

 
        for widget in self.button_frame.winfo_children():
            widget.grid_configure(padx=30, pady=10)

        self.display()



    def display(self):
        data = self.user.get_users()

        formatted_data = []

        for item in data :
            formatted_date = item[6].strftime("%b. %d, %Y")
            
            formatted_item = (
                item[0].capitalize(),
                item[1][:1].capitalize(),
                item[2].capitalize(),
                item[3],
                item[4].capitalize(),
                item[5].capitalize(),
                formatted_date)
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


    def export_to_word(self):
        pass

    def exit(self):  # Exits the program
        self.root.destroy() 



    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    report = UserReport(root)
    report.run()