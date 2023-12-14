from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random,string
import smtplib
import re
from database import DB_Connection
from config import Config as config
import datetime as dt

from tkinter import PhotoImage
from PIL import Image, ImageTk

from docxtpl import DocxTemplate
from docx2pdf import convert
from datetime import datetime
from tkcalendar import Calendar
import tkinter as tk
from . exception import DateEmptyError


# db_connection = DB_Connection()


class Utils():

    def __init__(self):
        self.db_connection = DB_Connection()
        

    #generate email address
    def generate_email_address(self,firstname,middlename,lastname):
        firstname_init = firstname[:1].lower()
        middlename_init = middlename[:1].lower()
        if len(lastname ) > 5:
            word_prefix = lastname[0:5].lower()
        else:
            word_prefix = lastname
        num = self.count_lastname(word_prefix)
        # return "{a}{b}{c}{d}@{e}".format(a = word_prefix,b = num,c = firstname_init,d = middlename_init,e = config.domain)
        return "{a}{b}{c}{d}@{e}".format(a = word_prefix,b = num,c = firstname_init,d = middlename_init,e = config.get_domain())



    #SEND EMAIL
    def send_email(email,subject,body):
        pass



        
    #GENERATE DEFAULT PASSWORD
    @staticmethod
    def generate_default_password():
        ref_data_set = string.ascii_uppercase + \
        string.ascii_lowercase + string.punctuation[0:5] +string.digits
        selection = random.choices(ref_data_set, k=8)
        password = "".join(map(str, selection))
        return "passinit"
    



    #CHECK IF EMAIL IS VALID
    def check_email_pattern(self,email):
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(email_pattern, email):
            return True
        return False

    
    


    def count_lastname(self,word_prefix):
        self.lastname_count = 0
        query = 'SELECT count(*) from user where lastname like %s'
        self.db_connection.cursor.execute(query,(word_prefix,))
        result = self.db_connection.cursor.fetchone()
        self.db_connection.close_connection()

        if result is not None and isinstance(result[0], int):
            return result[0] + 1
        else:
            return 0 + 1

    def get_userid_from_email(self,email):
        #get the user's id from the users table
        select_query ='SELECT user_id FROM user WHERE email = %s'
        self.db_connection.cursor.execute(select_query,(email,))
        user_id = self.db_connection.cursor.fetchone()[0]
        return user_id
    
    def get_customer_from_email(self,email):
         #get the user's id from the users table
        select_query ='SELECT * FROM customer WHERE email = %s'
        self.db_connection.cursor.execute(select_query,(email,))
        customer = self.db_connection.cursor.fetchone()
        return customer


    def get_order_status(self):
         #get the user's id from the users table
        select_query ='SELECT order_status_name FROM orderstatus'
        self.db_connection.cursor.execute(select_query)
        all_status = self.db_connection.cursor.fetchall()
        return all_status
    

    def get_order_history(self,order_id):
        query ="""select
                    oh.order_id,
                    CONCAT(u.firstname, ' ', u.lastname) AS 'Updated By',
                    os.order_status_name,
                    date_updated,
                    oh.notes
                    FROM orderhistory oh
                    JOIN orderstatus os ON oh.order_status = os.orderstatus_id
                    JOIN user u ON u.user_id = oh.user_id
                    WHERE oh.order_id = %s"""
        self.db_connection.cursor.execute(query,(order_id,))
        order_history = self.db_connection.cursor.fetchall()
        return order_history




    def get_order_from_orderid(self,order_id):
        query = """
            select orders.order_id,
            order_date,
            delivery_method,
            order_fulfilment_date,
            user.firstname,
            user.lastname,
            order_status,
            sum(orderline.quantity) as total_quantity,
            sum(orderline.quantity * products.product_price) as amount,
            orders.notes
            from orders 
            join user on user.user_id = orders.salesperson
            join orderline on orders.order_id = orderline.order_id 
            join products on products.product_id = orderline.product_id
            where orders.order_id = %s
            group by orders.order_id;
        """
        # select_query ='SELECT * FROM orders WHERE order_id = %s'
        self.db_connection.cursor.execute(query,(order_id,))
        order = self.db_connection.cursor.fetchone()
        return order



        

    #TRACK USER LOGIN AND LOGOUT TIMES
    def track_login_logout(self,type,email,timestamp):
        user_id = self.get_userid_from_email(email)
      
        #insert the login datetime in the database if user logs in
        if type == 'login':
            query = 'INSERT INTO login_history (user_id,login_time) VALUES (%s,%s)'
            self.db_connection.cursor.execute(query,(user_id,timestamp))
            self.db_connection.connection.commit()

        #insert the logout datetime in the database when user logs out   
        else:
            query = 'UPDATE login_history SET logout_time = %s WHERE user_id = %s'
            self.db_connection.cursor.execute(query,(timestamp,user_id))
            self.db_connection.connection.commit()
        self.db_connection.connection.close()
          

    def get_last_logged_in_time(self,email):
        user_id = self.get_userid_from_email(email)
        query = 'SELECT MAX(login_time) AS last_login_time FROM login_history WHERE user_id = %s'
        self.db_connection.cursor.execute(query,(user_id,))
        last_login_time = self.db_connection.cursor.fetchone()[0]
        return last_login_time
    

    def get_date_joined(self,email):
        user_id = self.get_userid_from_email(email)
        query = 'SELECT date_created FROM user WHERE user_id = %s'
        self.db_connection.cursor.execute(query,(user_id,))
        date_joined = self.db_connection.cursor.fetchone()[0]
        return date_joined
    
    
        



    def resize_image(size,image_url):
        # Load the original image
        original_image = Image.open(f'{image_url}')
        resized_image = original_image.resize((size[0], size[1]))   
        # tk_image = tkinter.PhotoImage(resized_image)
        tk_image = ImageTk.PhotoImage(resized_image)
        return tk_image

    #CHECK IF PASSWORD IS 8 CHARACTERS OR MORE

    def check_password_length(self,password):
        if len(password) >= 8 or password == 'q':
            return True
        return False

    
    def check_new_confirm_password(self,new_password,confirm_password):
        if new_password == confirm_password:
            return True
        return False


    def date_formatter(self,input_date):
        if input_date == "":
            raise DateEmptyError("Error, Please enter a date")
        date_object = datetime.strptime(input_date, '%m/%d/%y')
        formatted_date = date_object.strftime('%Y-%m-%d')
        return formatted_date
    
    def date_object(self,input_date):
        if input_date == "":
            raise DateEmptyError("Error, Please enter a date")
        date_object = datetime.strptime(input_date, '%m/%d/%y')
        return date_object
    


    def get_time_of_day_greeting(self):
        current_time = datetime.now()
        current_hour = current_time.hour

        if 5 <= current_hour < 12:
            return "Good morning"
        elif 12 <= current_hour < 17:
            return "Good afternoon"
        else:
            return "Good evening"
    
    


class ReportExporter():
    users_login_report_template = "Assets/users_login_report_tmpl.docx"
    order_invoice_template = "Assets/invoice_template.docx"

    def __init__(self):
        self.utils = Utils()
        pass

    
    def export_user_login_report_to_docx(self,template,data,other_info):
        self.doc = DocxTemplate(template)


      
        self.doc.render({"name":other_info['firstname'] + " " + other_info['lastname'],
                         "role":other_info['role'],
                         "total_users":len(data),
                         'users_list':data,
                         'date':dt.datetime.now().strftime("%b. %d, %Y"),
                         'time':dt.datetime.now().strftime("%H:%M:%S")
                         })
        return self.doc.save(f"Rprts/user_login_report-{dt.datetime.now()}.docx")
    

    def export_order_invoice_to_docx(self,template,product_data,customer_data,user_data,other_info):
        self.doc = DocxTemplate(template)
        self.doc.render({"user_name":user_data['firstname'].capitalize() + " " + user_data['lastname'].capitalize(),
                         "customer_name":customer_data[0].capitalize() + " " + customer_data[1].capitalize(),
                         "customer_email":customer_data[2],
                         "customer_address":customer_data[3],
                         "customer_city":customer_data[4],
                         'customer_state':customer_data[5],
                         'product_list':product_data,
                         'date':dt.datetime.now().strftime("%b. %d, %Y"),
                         'fulfillment_date':(self.utils.date_object(other_info[0])).strftime("%b. %d, %Y"),
                         'total_amount':f"${other_info[1]}",
                         'delivery_method': other_info[2]
                    })
        return self.doc.save(f"Rprts/invoice_{customer_data[2]}-{dt.datetime.now()}.docx")


    def export_to_pdf(self,template,data,other_info):
        self.doc = DocxTemplate(template)
        self.doc.render({"name":other_info['firstname'] + " " + other_info['lastname'],
                         "role":other_info['role'],
                         "total_users":len(data),
                         'users_list':data,
                         'date':dt.datetime.now().strftime("%b. %d, %Y"),
                         'time':dt.datetime.now().strftime("%H:%M:%S")
                         })
       
        docx_filename = f"Rprts/user_login_report-{dt.datetime.now()}.docx"
        self.doc.save(docx_filename)
        convert(docx_filename)
        # print(type(self.doc.save(f"Rprts/user_login_report-{dt.datetime.now()}.docx")))

    @classmethod
    def get_users_login_report_template(cls):
        return cls.users_login_report_template
    
    @classmethod
    def get_invoice_template(cls):
        return cls.order_invoice_template
      




class MyCalendar(tk.Toplevel):
    def __init__(self,root,calling_window,date_type = ""):
        self.root = root
        self.calling_window = calling_window
        self.root.title("Calendar")
        self.date_type = date_type


        self.cal = Calendar(self.root, selectmode='day', year=2023, month=11, day=8)
        self.cal.pack(padx=10, pady=10)

         #Button to get the selected date
        self.get_date_button = tk.Button(self.root, text="Get Date", command=self.get_selected_date)
        self.get_date_button.pack(pady=10)


    def get_selected_date(self):
        
        self.selected_date = self.cal.get_date()
        self.calling_window.update_selected_date(self.selected_date,self.date_type)
        self.root.destroy()
        # self.selected_date_label.config(text=f"Selected Date: {selected_date}")

   
class EmailService():

    def __init__(self):
        pass

    def send_email(self, to_email, subject, message):

        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        smtp_username = config.smtp_username
        smtp_password = config.smtp_password
        smtp_connection = smtplib.SMTP(smtp_server, smtp_port)

        try:
            smtp_connection.starttls()
            smtp_connection.login(smtp_username, smtp_password)
            msg = MIMEMultipart()
            msg['From'] = smtp_username
            msg['To'] = to_email
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))

            smtp_connection.sendmail(smtp_username, to_email, msg.as_string())
        except Exception as e:

            print(f"Email sending failed: {str(e)}")

        finally:
            smtp_connection.quit()







   

    


