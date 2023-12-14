import tkinter as tk
# from database import DB_Connection
from tkinter import messagebox,ttk
from controllers.customers import Customer
from controllers.utils import Utils
from views.styles import Style
class CreateCustomer(tk.Toplevel):
    def __init__(self, parent):
        self.parent = parent


        self.customer_frame = tk.Frame(self.parent,bg = "#EEEEEE")
        self.customer_frame.grid(row = 0,column =0,padx = 40)
        

        
        self.tk_image = Utils.resize_image((50,50),'images/google/add-customer.png')
        # Create a Label widget with the resized image
        self.customer_image = tk.Label(self.customer_frame, image=self.tk_image)
        self.customer_image.grid(row = 0, column =3,pady = 20, padx = 20,sticky="E")

        self.customer_label = tk.Label(self.customer_frame, text="Create Customer",font= Style.page_heading,foreground =Style.page_heading_color)
        self.customer_label.grid(row = 0, column = 0, padx=20, pady=10)

        tk.Label(self.customer_frame, text="First Name:",fg="black").grid(row = 1, column =0,sticky='E')
        self.first_name_entry = tk.Entry(self.customer_frame,width = 20,fg="black")
        self.first_name_entry.grid(row = 1, column = 1,padx=20,pady=20,sticky='W')

        tk.Label(self.customer_frame, text="Last Name:",fg="black").grid(row = 1, column = 2,sticky='E')
        self.last_name_entry = tk.Entry(self.customer_frame,width = 20,font = ('helvetica', 11))
        self.last_name_entry.grid(row = 1, column = 3,padx = 20,pady=20,sticky='W')

        tk.Label(self.customer_frame, text="Email:",font = ('helvetica', 12)).grid(row = 2, column = 0,sticky='E')
        self.email_entry = tk.Entry(self.customer_frame,font = ('helvetica', 11))
        self.email_entry.grid(row = 2, column = 1,padx=20,pady=20,sticky='W')

        tk.Label(self.customer_frame, text="Address:",font = ('helvetica', 12)).grid(row = 2, column = 2,sticky='E')
        self.address_entry = tk.Entry(self.customer_frame,font = ('helvetica', 11))
        self.address_entry.grid(row = 2, column = 3, padx = 20,pady=20)

        tk.Label(self.customer_frame, text="City:",font = ('helvetica', 12)).grid(row = 3, column = 0,sticky='E')
        self.city_entry = tk.Entry(self.customer_frame,font = ('helvetica', 11))
        self.city_entry.grid(row = 3, column = 1, padx=20,pady=20,sticky='W')

        tk.Label(self.customer_frame, text="State:",font = ('helvetica', 12)).grid(row = 3, column = 2,sticky='E')
        self.state_entry = tk.Entry(self.customer_frame,width=10,font = ('helvetica', 11))
        self.state_entry.grid(row =3, column = 3,padx = 20, pady=20 ,sticky='W')

        self.form_state_message = tk.Label(self.customer_frame,text = "",fg='red',font = ('helvetica',9))
        self.form_state_message.grid(row=4,column=3)

        tk.Label(self.customer_frame, text="Note:",font = ('helvetica', 12)).grid(row = 5, column = 0,sticky='E')
        self.note_entry = tk.Text(self.customer_frame,height=3,width = 40)
        self.note_entry.grid(row=5, column=1,columnspan = 3, padx=20,sticky='W')
       

        self.save_button = tk.Button(self.customer_frame, text="Save Customer",background="#08A04B",font = ('helvetica', 12),fg="black",width= 15, command=self.save_customer)
        self.save_button.grid(row = 6, column = 2, sticky='E',padx = 20,pady = 40,)

        self.clear_button = tk.Button(self.customer_frame, text="Clear Form",background="#008FD3",font = ('helvetica', 12),fg="black",width= 15,command=self.clear_customer_create_form)
        self.clear_button.grid(row = 6, column = 3, padx=20, sticky='E',pady = 40)


     

    def save_customer(self):
        customer_info = {
            'firstname' :self.first_name_entry.get(),
            'lastname': self.last_name_entry.get(),
            'email':self.email_entry.get(),
            'address':self.address_entry.get(),
            'city':self.city_entry.get(),
            'state':self.state_entry.get(),
            'notes':self.note_entry.get('1.0', 'end-1c')

                         }
        

        #VALIDATE CITY FORM
        if len(customer_info['state']) != 2:
            self.form_state_message.config(text = "State must be two characters")
        else:
            new_customer = Customer(
                firstname =customer_info['firstname'],
                lastname = customer_info['lastname'],
                email = customer_info['email'],
                address = customer_info['address'],
                city = customer_info['city'],
                state = customer_info['state'],
                notes = customer_info['notes'] )
            save_operation = new_customer.add_customer()
            
        if save_operation == False:
            messagebox.showerror("Error", "Customer record was not created, customer already exist")
        else: 
            messagebox.showinfo("Customer Creation","Customer added successfully!")
            

    def clear_customer_create_form(self):

        self.first_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.city_entry.delete(0, tk.END)
        self.state_entry.delete(0, tk.END)
        self.note_entry.delete("1.0", tk.END)
        self.form_state_message.config(text = " ")



# if __name__ == "__main__":
#     root = tk.Tk()
#     create_customer_window = tk.Toplevel(root)
#     CreateCustomer(create_customer_window)
#     root.mainloop()
