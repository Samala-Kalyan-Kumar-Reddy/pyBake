import tkinter as tk
from tkinter import ttk
from controllers.users import User
from tkinter import messagebox
from controllers.utils import Utils
from views.styles import Style
from werkzeug.security import generate_password_hash,check_password_hash




class AddUser(tk.Toplevel):
    def __init__(self, root):
        self.root = root
        self.root.title("Add User")
        self.utils = Utils()
        # self.root.geometry("400x300")
        self.role_var = tk.StringVar()
        available_roles = self.fetch_available_roles()
        #create title frame
        self.title_frame = tk.Frame(master = self.root)
        self.title_frame.pack(fill = 'x',expand = True)

        self.form_msg_frame = tk.Frame(master = self.root)
        self.form_msg_frame.pack(fill = 'x',expand= True)

        self.create_form_frame = tk.Frame(master = self.root)
        self.create_form_frame.pack(fill = 'x',expand= True)

        self.create_form_button_frame = tk.Frame(master = self.root,)
        self.create_form_button_frame.pack(fill = 'x',expand= True,padx = 20,pady = (20,30))
       

        
        #add user form title
        self.tk_image = Utils.resize_image((50,50),'images/google/add-user.png')
        # Create a Label widget with the resized image
        self.product_image = tk.Label(self.title_frame, image=self.tk_image,)
        self.product_image.pack(side = "right", padx=(0,40),pady =(20,0))
        tk.Label(self.title_frame, text = "Add User",font = Style.page_heading,fg = Style.page_heading_color).pack(side = 'left',padx = (40,0), pady =(20,0))


        self.form_message = tk.Label(self.form_msg_frame, text="",fg = 'red')
        self.form_message.pack()

        tk.Label(self.create_form_frame, text="First Name:").grid(row = 1, column =0,sticky='E')
        self.first_name_entry = tk.Entry(self.create_form_frame)
        self.first_name_entry.grid(row = 1, column = 1, sticky = 'W')

        tk.Label(self.create_form_frame, text="Middle Name:").grid(row = 2, column = 0,sticky='E')
        self.middle_name_entry = tk.Entry(self.create_form_frame)
        self.middle_name_entry.grid(row = 2, column = 1,sticky='W')

        tk.Label(self.create_form_frame, text="Last Name:").grid(row = 3, column = 0,sticky='E')
        self.last_name_entry = tk.Entry(self.create_form_frame)
        self.last_name_entry.grid(row = 3, column = 1,sticky='W')


        # tk.Label(root, text="Date of Birth").grid(row = 4, column = 0)
        # self.dob_entry = customtkinter.CTkEntry(root)
        # self.dob_entry.grid(row = 4, column = 1, padx=20,pady=5)

        # tk.Label(root, text="Phone Number:").grid(row = 5, column = 0)
        # self.phone_entry = customtkinter.CTkEntry(root)
        # self.phone_entry.grid(row = 5, column = 1, padx=20,pady=5)
        # For example, you can add Entry widgets for customer information
        
        
       

        tk.Label(self.create_form_frame, text="Roles:").grid(row = 4, column = 0,sticky='E')
        
        self.role_var.set(available_roles[0])
        self.role_dropdown = ttk.Combobox(self.create_form_frame, width = 10,values = available_roles)
        self.role_dropdown.grid(row = 4, column = 1,sticky='W')



        self.save_button = tk.Button(self.create_form_frame, text="Save User",command=self.save_user)
        self.save_button.grid(row = 5, column = 1,sticky='W')

        self.reset_button = tk.Button(self.create_form_frame, text="Reset", command=self.reset_form)
        self.reset_button.grid(row = 5, column = 1,padx = (0,20),sticky = 'E')


        for widget in self.create_form_frame.winfo_children():
            widget.grid_configure(pady = (0,20),padx = 20)


        for widget in self.create_form_button_frame.winfo_children():
            widget.grid_configure(pady = 10,padx = 10)

    

    def fetch_available_roles(self):
        self.user_roles = User()
        return self.user_roles.get_roles()
      
    
    # def on_customer_combobox_select(self,event):
    #     self.role_var.set(self.search_customer_combobox.get())
        
    def save_user(self):
        firstname = self.first_name_entry.get()
        middlename = self.middle_name_entry.get()
        lastname = self.last_name_entry.get()
        role = self.role_dropdown.get()
        
        user = User(firstname = firstname,lastname = lastname,middlename=middlename,role=role)
       
       
        status,message =  user.save_user()
        if status == 'ERROR':

            # messagebox.showerror("Error", message)
            self.form_message.config(text = message)
        else:
            messagebox.showinfo("User Creation",message)
            self.root.destroy()

    def reset_form(self):
        self.first_name_entry.delete(0,"end")
        self.last_name_entry.delete(0,"end")
        self.middle_name_entry.delete(0,"end")
        self.role_var.set("")

            # toast = ToastNotification(
            #     title="Success Message", message=f"User with email {customer_info['email']} has been added successfully!",
            #     duration=7000,
            #     alert=True,
            #     position=(250,30,'sw'),)
            # toast.show_toast()
            



if __name__ == "__main__":
    root = tk.Tk()
    add_user_window = tk.Toplevel(root)
    AddUser(add_user_window)
    root.mainloop()