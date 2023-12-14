import tkinter as tk
# from database import DB_Connection
from tkinter import messagebox,ttk
from controllers.customers import Customer
from controllers.utils import Utils

class ManageCustomer(tk.Toplevel):
    def __init__(self, parent):
        self.parent = parent
        
        
        self.tk_image = Utils.resize_image((50,50),'images/user.png')
        # Create a Label widget with the resized image
        self.customer_image = tk.Label(self.parent, image=self.tk_image)
        self.customer_image.grid(row = 0, column =3,pady = 20, padx = 20,sticky="E")

        self.customer_label = tk.Label(self.parent, text="Create Customer",font= ('Helvetica',18),foreground ='#008fd3')
        self.customer_label.grid(row = 0, column = 0, padx=20, pady=10)

        tk.Label(parent, text="First Name:",font = ('helvetica', 11)).grid(row = 1, column =0,sticky='E')
        self.first_name_entry = tk.Entry(self.parent,width = 20,font = ('helvetica', 11))
        self.first_name_entry.grid(row = 1, column = 1,padx=20,pady=20,sticky='W')

        tk.Label(parent, text="Last Name:",font = ('helvetica', 11)).grid(row = 1, column = 2,sticky='E')
        self.last_name_entry = tk.Entry(self.parent,width = 20,font = ('helvetica', 11))
        self.last_name_entry.grid(row = 1, column = 3,padx = 20,pady=20,sticky='W')

        tk.Label(parent, text="Email:",font = ('helvetica', 12)).grid(row = 2, column = 0,sticky='E')
        self.email_entry = tk.Entry(self.parent,font = ('helvetica', 11))
        self.email_entry.grid(row = 2, column = 1,padx=20,pady=20,sticky='W')

        tk.Label(parent, text="Address:",font = ('helvetica', 12)).grid(row = 2, column = 2,sticky='E')
        self.address_entry = tk.Entry(self.parent,font = ('helvetica', 11))
        self.address_entry.grid(row = 2, column = 3, padx = 20,pady=20)

        tk.Label(parent, text="City:",font = ('helvetica', 12)).grid(row = 3, column = 0,sticky='E')
        self.city_entry = tk.Entry(self.parent,font = ('helvetica', 11))
        self.city_entry.grid(row = 3, column = 1, padx=20,pady=20,sticky='W')

        tk.Label(parent, text="State:",font = ('helvetica', 12)).grid(row = 3, column = 2,sticky='E')
        self.state_entry = tk.Entry(self.parent,width=10,font = ('helvetica', 11))
        self.state_entry.grid(row =3, column = 3,padx = 20, pady=(0,10),sticky='W')

        self.form_state_message = tk.Label(self.parent,text = "",fg='red',font = ('helvetica',9))
        self.form_state_message.grid(row=4,column=3)

        tk.Label(parent, text="Note:",font = ('helvetica', 12)).grid(row = 5, column = 0,sticky='E')
        self.note_entry = tk.Text(self.parent,font = ('helvetica', 11),height=3,width = 40)
        self.note_entry.grid(row=5, column=1,columnspan = 3, padx=20,sticky='W')
       

        self.save_button = tk.Button(self.parent, text="Save Customer",background="#08A04B",font = ('helvetica', 10),fg="white",width= 15, command=self.save_customer)
        self.save_button.grid(row = 6, column = 2, sticky='E',padx = 20,pady = 80,)

        self.clear_button = tk.Button(self.parent, text="Clear Form",background="#008FD3",font = ('helvetica', 10),fg="white",width= 15,command=self.clear_customer_create_form)
        self.clear_button.grid(row = 6, column = 3, padx=20, sticky='E',pady = 80)



        

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
                city = customer_info['address'],
                state = customer_info['state'],
                notes = customer_info['notes'] )
            save_operation = new_customer.add_customer()
            
        if not save_operation:
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
