from database import DB_Connection
from .utils import Utils

class Product():
    util_obj = Utils()
   
    def __init__(self,product_code = "",product_name = "",product_price =0,product_description = ""):
        self.product_code = product_code
        self.product_name = product_name
        self.product_price = product_price
        self.product_description = product_description
        

        self.db_connection = DB_Connection()


                         
        
    def add_product(self):
        #check if the customer does not already exist
        query = 'SELECT * FROM products WHERE product_code = %s'
        self.db_connection.cursor.execute(query,(self.product_code,))
        result = self.db_connection.cursor.fetchone()

        if not result:
            insert_query = "INSERT INTO products (product_code,product_name,product_price,product_description) VALUES (%s, %s, %s, %s)"
            insert_data = (self.product_code.upper(),self.product_name.lower(),self.product_price,self.product_description)
            self.db_connection.cursor.execute(insert_query, insert_data)
            self.db_connection.connection.commit()
            self.db_connection.close_connection()
            # Product.product_count += 1 # increment the number of products
            #SEND AN EMAIL TO THE CUSTOMER
            return True
 
        else:
            return False
        

    def get_products(self):
        query = '''SELECT 
        product_code,
        product_name,
        product_price, 
        product_description
        FROM products '''
        self.db_connection.cursor.execute(query)
        products_info = self.db_connection.cursor.fetchall()
        return products_info



    def get_product_id(self,product_code):
        query = 'SELECT product_id FROM products WHERE product_code = %s'
        self.db_connection.cursor.execute(query,(product_code,))
        result = self.db_connection.cursor.fetchone()
        if result:
            return result[0]
        return False
    
    def product_count(self):
        query = "SELECT COUNT(*) AS product_count FROM products"
        self.db_connection.cursor.execute(query)
        product_count = self.db_connection.cursor.fetchone()
        return product_count[0]
    

    def top_selling_product(self):
        query = """SELECT
            p.product_code,
            p.product_name,
            SUM(ol.quantity) AS total_quantity_sold
            FROM
            products p
            JOIN
            orderline ol ON p.product_id = ol.product_id
            GROUP BY
            p.product_id, p.product_name
            ORDER BY
            total_quantity_sold DESC
            LIMIT 1"""
        self.db_connection.cursor.execute(query)
        top_selling_product = self.db_connection.cursor.fetchone()
        return top_selling_product
        
   

    def top_ten_products(self):
        query = """SELECT
                        p.product_name,
                        SUM(ol.quantity) AS total_quantity_sold,
                        SUM(ol.quantity * p.product_price) AS total_revenue
                        FROM
                        products p
                        JOIN
                        orderline ol ON p.product_id = ol.product_id
                        GROUP BY
                        p.product_name
                        ORDER BY
                        total_quantity_sold DESC
                        LIMIT 10"""
        self.db_connection.cursor.execute(query)
        top_ten_product = self.db_connection.cursor.fetchall()
        return top_ten_product
    
    

    

            
    








        

    
 
        
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
            


        
