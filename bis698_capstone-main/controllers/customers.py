from database import DB_Connection
from .utils import Utils

class Customer():
    
    
    
    # customer_count = 0
   
    def __init__(self,firstname = "",lastname = "",email ="",address ="",city = "",state ="",notes = ""):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.address = address
        self.city = city
        self.state = state
        self.notes = notes

        self.db_connection = DB_Connection()
        self.util_obj = Utils()
        


                         
        
    def add_customer(self):
        #check if the customer does not already exist
        query = 'SELECT * FROM customer WHERE email = %s'
        self.db_connection.cursor.execute(query,(self.email,))
        result = self.db_connection.cursor.fetchone()

        if not result: #if customer do not already exist
            insert_query = "INSERT INTO customer (firstname,lastname,email,address,city,state,notes) VALUES (%s, %s, %s, %s, %s,%s,%s)"
            insert_data = (self.firstname.lower(),self.lastname.lower(),self.email,self.address,self.city,self.state,self.notes)
            self.db_connection.cursor.execute(insert_query, insert_data)
            self.db_connection.connection.commit()
            #SEND AN EMAIL TO THE CUSTOMER

            # self.util_obj.send_email(self.email,"Test Email","Customer created successfully!")
            
            return True
 
        else:
            return False
        
    def get_customers(self):
        query = '''SELECT 
        firstname,
        lastname,
        email,
        city,
        state
        FROM customer '''
        self.db_connection.cursor.execute(query)
        customer_info = self.db_connection.cursor.fetchall()
        return customer_info
    
    def get_customer(self,email):
        query = '''SELECT 
        firstname,
        lastname,
        email,
        address,
        city,
        state
        FROM customer WHERE email = %s'''
        self.db_connection.cursor.execute(query,(email,))
        customer_info = self.db_connection.cursor.fetchall()
        return customer_info[0]
    

    def top_customers(self):
        query = """SELECT
    CONCAT(c.firstname, ' ', c.lastname) AS customer_name,
    c.email,
    c.city,
	c.state,
    COUNT(DISTINCT o.order_id) AS total_orders,
    SUM(ol.quantity * p.product_price) AS total_purchase_amount
    FROM
    customer c
    JOIN
    orders o ON c.customer_id = o.customer
    JOIN
    orderline ol ON o.order_id = ol.order_id
    JOIN
    products p ON ol.product_id = p.product_id
    GROUP BY
    c.customer_id, customer_name
    ORDER BY
    total_purchase_amount DESC
    LIMIT 10"""
        self.db_connection.cursor.execute(query)
        top_customers= self.db_connection.cursor.fetchall()
        return top_customers



    def customer_count(self):
        query = "SELECT COUNT(*) AS customer_count FROM customer"
        self.db_connection.cursor.execute(query)
        customer_count = self.db_connection.cursor.fetchone()
        return customer_count[0]

    
    def get_customer_id(self,customer_email):
        query = 'SELECT customer_id FROM customer WHERE email = %s'
        self.db_connection.cursor.execute(query,(customer_email,))
        result = self.db_connection.cursor.fetchone()
        if result:
            return result[0]
        return False
        

            
    








        

    
 
        
    # def authenticate(self, email,password):
    #     query = "SELECT * FROM user join role on user.role = role.role_id WHERE email = %s AND password = %s "
    #     self.db_connection.cursor.execute(query,(email,password))
    #     result = self.db_connection.cursor.fetchone()
       
    #     if result:

    #         column_names = self.db_connection.cursor.column_names # type: ignore
    #         user = {column_names[i]:result[i] for i in range(len(column_names))}
    #         return (user)
    #     return False


    # def get_roles(self):
    #     query = 'SELECT role_name FROM role'
    #     self.db_connection.cursor.execute(query)
    #     result = self.db_connection.cursor.fetchall()
    #     result_list = [item[0] for item in result]
    #     return result_list

    # def is_active(self,email):
    #     query = 'SELECT status from user where email = %s'
    #     self.db_connection.cursor.execute(query,(email,))
    #     status = self.db_connection.cursor.fetchone()
    #     if status[0] == 'inactive':
    #         return False
    #     return True



    # def save_user(self,**user_info):

    # #RUN THE EMAIL ALGORITHM. CHECK IF USER ALREADY EXIST. DO THE NEEDFUL
    #     user_email = self.util_obj.generate_email_address(**user_info)
    #     # user_email = 'tfredrtgd@derf.gtf'
    #     select_query = "SELECT * FROM user WHERE email = %s"
    #     self.db_connection.cursor.execute(select_query,(user_email,))
    #     user = self.db_connection.cursor.fetchone()
    #     if user: # this means the user does exist
    #         print(f"customer with email {user_info['email']} already exsit")
    #         return False
                
    #     else:
            
    #         role_maping = {'admin':1,'manager':2,'standard':3}
    #         role = role_maping.get(user_info['role'],3)
    #         insert_query = "INSERT INTO user (firstname, middlename, lastname, email,role,password) VALUES (%s, %s, %s, %s, %s,%s)"
    #         # password = 'WRDXFTEW'
    #         # user_email ='ertyuiop@eriity.tyu'
    #         insert_data = (
    #             user_info['firstname'].lower(),
    #                 user_info['middlename'].lower(),
    #                 user_info['lastname'].lower(),
    #                 user_email,
    #                     role,
    #         # generate_password_hash(self.generate_password()))
    #                 Utils.generate_default_password())
    #         self.db_connection.cursor.execute(insert_query, insert_data)
            
    #         self.db_connection.connection.commit()
    #         self.db_connection.close_connection()
    #         print(f"user with email {user_email} added to the database")
    #     #     return True
        
        

    # def change_password(self,username,old_password,new_password):
    #         select_query = 'SELECT user_id from user WHERE email = %s AND password = %s'
    #         self.db_connection.cursor.execute(select_query,(username,old_password))
    #         user = self.cursor.fetchone()
    #         if user:
    #             user_id = user[0]
    #             status = 'active'
    #             update_query = 'UPDATE user set password = %s,status = %s WHERE user_id = %s'
    #             self.db_connection.cursor.execute(update_query,(new_password,status,user_id))

    #             self.connection.commit()
    #             return f"Password changed successfully to {new_password}"
    #             #send an email to the user
    #         else:
    #             return 'Unable to change your password. Make sure your old password is correct!'
            


        
