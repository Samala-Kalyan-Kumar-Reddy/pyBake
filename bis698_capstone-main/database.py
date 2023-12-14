
from turtle import update
import mysql.connector

import config
from config import Config
from werkzeug.security import generate_password_hash,check_password_hash


class DB_Connection():
   

    def __init__(self):
        self.config_instance = Config()
        self.connection = mysql.connector.connect(
             host = self.config_instance.db_host,
             user = self.config_instance.user,
             password = self.config_instance.password,
             database = self.config_instance.database)
        self.cursor = self.connection.cursor()


    def close_connection(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.connection.is_connected():
                self.connection.close()
        except Exception as e:
            # Handle any exceptions that occur during cleanup
            print(f"Error during connection cleanup: {e}")

        
        
        
       
    


    # def authenticate(self, email,password):
    #     query = "SELECT * FROM user join role on user.role = role.role_id WHERE email = %s AND password = %s "
    #     self.cursor.execute(query,(email,password))
    #     result = self.cursor.fetchone()
    #     if result:

    #         column_names = self.cursor.column_names # type: ignore
    #         user = {column_names[i]:result[i] for i in range(len(column_names))}
    #         return (user)
    #     return False


    # def get_roles(self):
    #     query = 'SELECT role_name FROM role'
    #     self.cursor.execute(query)
    #     result = self.cursor.fetchall()
    #     result_list = [item[0] for item in result]
    #     return result_list

    # def is_active(self,email):
    #     query = 'SELECT status from user where email = %s'
    #     self.cursor.execute(query,(email,))
    #     status = self.cursor.fetchone()
    #     if status[0] == 'inactive':
    #         return False
    #     return True
        



    
    # def save_user(self,**user_info):
    #     # print(f"""
    #     # {user_info['firstname'],
    #     # user_info['role'] }""")
    #     #RUN THE EMAIL ALGORITHM. CHECK IF USER ALREADY EXIST. DO THE NEEDFUL
    #     user_email = self.generate_email_address(**user_info)
    #     # user_email = 'tfredrtgd@derf.gtf'
    #     select_query = "SELECT * FROM user WHERE email = %s"
    #     self.cursor.execute(select_query,(user_email,))
    #     user = self.cursor.fetchone()
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
    #              user_info['middlename'].lower(),
    #               user_info['lastname'].lower(),
    #                 user_email,
    #                     role,
    #         # generate_password_hash(self.generate_password()))
    #                 self.generate_password())
    #         self.cursor.execute(insert_query, insert_data)
            
    #         self.connection.commit()
    #         print(f"user with email {user_email} added to the database")
    #     #     return True
        
    # def count_lastname(self,word_prefix):
    #     self.lastname_count = 0
    #     query = 'SELECT count(*) from user where lastname like %s'
    #     self.cursor.execute(query,(word_prefix,))
    #     result = self.cursor.fetchone()

    #     if result is not None and isinstance(result[0], int):
    #         return result[0] + 1
    #     else:
    #     # Return a default value or raise an exception if appropriate
    #         return 0 + 1
      

    



    # def generate_password(self):
    #     util = Utils()
    #     password = util.generate_default_password()
    #     return password


    # def change_password(self,username,old_password,new_password):
    #     select_query = 'SELECT user_id from user WHERE email = %s AND password = %s'
    #     self.cursor.execute(select_query,(username,old_password))
    #     user = self.cursor.fetchone()
    #     if user:
    #         user_id = user[0]
    #         status = 'active'
    #         update_query = 'UPDATE user set password = %s,status = %s WHERE user_id = %s'
    #         self.cursor.execute(update_query,(new_password,status,user_id))

    #         self.connection.commit()
    #         return f"Password changed successfully to {new_password}"
    #         #send an email to the user
    #     else:
    #         return 'Unable to change your password. Make sure your old password is correct!'





    # def save_customer(self,**customer_info):
    #     select_query = "SELECT * FROM customer WHERE email = %s"
    #     self.cursor.execute(select_query,(customer_info['email'],))
    #     result = self.cursor.fetchone()
    #     if result: # this means the user does not exist
    #         print(f"customer with email {customer_info['email']} already exsit")
    #         return False
          
    #     else:
    #         insert_query = "INSERT INTO customer (firstname, lastname, email, address, city,state) VALUES (%s, %s, %s, %s, %s,%s)"
    #         insert_data = (customer_info['firstname'],
    #                     customer_info['lastname'],
    #                     customer_info['email'],
    #                     customer_info['address'], 
    #                     customer_info['city'],
    #                     customer_info['state'])
    
    #         self.cursor.execute(insert_query, insert_data)
            
    #         self.connection.commit()
    #         print(f"Customer with email {customer_info['email']} added to the database")
    #         return True
           

    

        

if __name__ == '__main__':
    # db = DB_Connection()
    print('owobuwilfred@gmail.com','password')


# db_host = 'localhost'
# user='root'
# password='Admin123$'
# database ='pyBake_db'
# connection = mysql.connector.connect(
#     host = db_host,
#     user = user,
#     password = password,
#     database = database)

# email = 'owobuwilfred@gmail.com'
# password = 'password'

# cursor = connection.cursor()
# query = "SELECT * FROM users WHERE email = %s AND password = %s"
# cursor.execute(query,(email,password))
# result = cursor.fetchall()

# print(result[0])
# if result:
#     print("The user exists")
# else:
#     print("No user with that email exists")
