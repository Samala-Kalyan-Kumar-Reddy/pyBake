from database import DB_Connection
from . utils import Utils
from datetime import datetime
import logging

class User():
    def __init__(self,firstname="",middlename="",lastname="",email = "",password = "",role=""):
    # def __init__(self):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.email = email
        self.password = password
        self.role = role


        self.util_obj = Utils()
        self.db_connection = DB_Connection()
        self.login_attempt_count = 0


        # self.user_info = {"firstname":self.firstname,
        #                   'middlename':self.middlename,
        #                   'lastname':self.lastname}

    def set_user_email(self):
        self.email = self.util_obj.generate_email_address(self.firstname,self.middlename,self.lastname)


    def get_user_email(self):
        return self.email
    

    def set_role(self):
        role_mapping = {'admin':1,'manager':2,'sales associate':3} 
        if self.role not in role_mapping.keys():
             raise ValueError("Invalid Role")
        else:
            self.role = role_mapping.get(self.role)
        

    def get_role(self):
        return self.role


    def set_user_password(self):
        self.password = self.util_obj.generate_default_password()
        
    
    def get_user_password(self):
        return self.password

  
    def authenticate_user(self):
        
        auth_status = ""
        #check if email matches email pattern
        if self.util_obj.check_email_pattern(self.email):
            #check if the password length is valid
            if self.util_obj.check_password_length(self.password):
                #get the user object from the database
                query = "SELECT * FROM user join role on user.role = role.role_id WHERE email = %s AND password = %s "
                self.db_connection.cursor.execute(query,(self.email,self.password))
                user = self.db_connection.cursor.fetchone()
                if user:
                    user = {'user_id':user[0],
                            'firstname':user[1],
                            'middlename':user[2],
                            'lastname':user[3],
                            'password':user[5],
                            'email':user[4],
                            'status':user[7],
                            'role':user[12]
                            }
                    #check if user is active
                    if not self.is_active():
                        auth_status = "change_password"
                        message = "password change is required"
                        return(auth_status,message,user)
                    
                    auth_status = 'authenticated'
                    message = "authenticated successfully"
                    #create a log of this
                    #save the log in timestamp in the database
                    self.util_obj.track_login_logout('login',user['email'],datetime.now())
                    return(auth_status,message,user)
            auth_status = 'invalid_password'    
            message = "email or password is incorrect"
            return (auth_status,message)
        
        auth_status = "invalid_email"
        message = "email must be a valid email"
        return (auth_status,message)
        

        # query = "SELECT * FROM user join role on user.role = role.role_id WHERE email = %s AND password = %s "
        # self.db_connection.cursor.execute(query,(self.get_user_email,self.get_user_password))
        # result = self.db_connection.cursor.fetchone()
       
        # if result:
        #     column_names = self.db_connection.cursor.column_names # type: ignore
        #     user = {column_names[i]:result[i] for i in range(len(column_names))}
        #     return (user)
        # return False


    def get_roles(self):
        query = 'SELECT role_name FROM role'
        self.db_connection.cursor.execute(query)
        result = self.db_connection.cursor.fetchall()
        result_list = [item[0] for item in result]
        return result_list

      
    

    def get_locked_users(self):
        query = 'SELECT firstname,lastname,email from user where status =%s'
        self.db_connection.cursor.execute(query,('locked',))
        locked_users = self.db_connection.cursor.fetchall()
        # locked_users = [item[2] for item in locked_users]
        locked_users = [item[2] for item in locked_users]
        return locked_users
        

    def is_active(self):
        query = 'SELECT status from user where email = %s'
        self.db_connection.cursor.execute(query,(self.get_user_email(),))
        status = self.db_connection.cursor.fetchone()
        if status[0] != 'active':
            return False
        return True



    def save_user(self):
        try:
            self.set_role()

            self.set_user_email()
            self.set_user_password()
    #RUN THE EMAIL ALGORITHM. CHECK IF USER ALREADY EXIST. DO THE NEEDFUL
        #check if user already exist
        
            select_query = "SELECT * FROM user WHERE email = %s"
            self.db_connection.cursor.execute(select_query,(self.get_user_email(),))
            self.user = self.db_connection.cursor.fetchone()
            if self.user: # this means the user does exist
                return (False, f"User with email {self.get_user_email()} already exist")
                        
           
            insert_query = "INSERT INTO user (firstname, middlename, lastname, email,password,role) VALUES (%s, %s, %s, %s, %s,%s)"
            # password = 'WRDXFTEW'
            # user_email ='ertyuiop@eriity.tyu'
            user_info = (
            self.firstname.lower(),
            self.middlename.lower(),
            self.lastname.lower(),
            self.get_user_email(),
            self.get_user_password(),
            self.get_role())

            self.db_connection.cursor.execute(insert_query, user_info)
        
            self.db_connection.connection.commit()
            self.db_connection.close_connection()
        except ValueError as e:
            status = 'ERROR'
            message= str(e)
            return (status,message)
        
        else:
            status = 'SUCCESS'
            message = f"user with email {self.get_user_email()} added to the database"
            return (status,message)

        #SEND EMAIL TO THE USER THAT HIS ACCOUNT HAS BEEN CREATED


        
    def get_users(self):
        select_query = '''SELECT 
        u.firstname,
        u.middlename,
        u.lastname,
        u.email,
        r.role_name,
        u.status,
        u.date_created
        FROM user u JOIN role r ON u.role = r.role_id'''
        self.db_connection.cursor.execute(select_query)
        users = self.db_connection.cursor.fetchall()
        if users:
            return users




    def user_count(self):
        query = "SELECT COUNT(*) AS user_count FROM user"
        self.db_connection.cursor.execute(query)
        user_count = self.db_connection.cursor.fetchone()
        return user_count[0]
    def change_password(self,new_password,confirm_password):
            
            select_query = 'SELECT user_id from user WHERE email = %s AND password = %s'
            self.db_connection.cursor.execute(select_query,(self.get_user_email(),self.get_user_password()))
            user = self.db_connection.cursor.fetchone()
            #if the user is a valid user based on the supplied email and old password
            if user:
                #check the new password lenght
                if self.util_obj.check_password_length(new_password):
                    #check if the new password matches the confirm password
                    if self.util_obj.check_new_confirm_password(new_password,confirm_password):
                        updated_new_password = new_password
                        user_id = user[0]
                        status = 'active'
                        update_query = 'UPDATE user set password = %s,status = %s WHERE user_id = %s'
                        self.db_connection.cursor.execute(update_query,(updated_new_password,status,user_id))

                        self.db_connection.connection.commit()
                        self.db_connection.close_connection()
                        
                        # logging.info(f"Password changed for {self.user.get('email')} at {datetime.now()}")
                        return "Password changed successfully!"
                    return "new password and confirm password must be thesame"
                return "new password must be at least 8 characters"
            return 'Unable validate your old password!'
            


    def reset_password(self):
        select_query = 'SELECT user_id from user WHERE email = %s'
        self.db_connection.cursor.execute(select_query,(self.get_user_email(),))
        user = self.db_connection.cursor.fetchone()
        #if the user is a valid user based on the supplied email and old password
        if user:
            user_id = user[0]
            status = 'inactive'
            password = self.util_obj.generate_default_password()
            update_query = 'UPDATE user set password = %s,status = %s WHERE user_id = %s'
            self.db_connection.cursor.execute(update_query,(password,status,user_id))
            self.db_connection.connection.commit()
            self.db_connection.close_connection()
            logging.info(f"Password was reset for {self.get_user_email()} at {datetime.now()}")
            status = 'success'
            message = "Password reset was successfully!"
            return (status,message)
        status = 'failure'
        message = 'Unable to retrieve the user!'
        return (status,message)
    

    def lock_user_account(self):
        #check if the login attempt is unsuccessful
        if not self.authenticate():
        #increment the unsuccessful login attempt count
            while self.lock_user_account != 3:
                self.login_attempt_count += 1
            #set the user status to locked
            update_query = 'UPDATE user set status = %s WHERE user_id = %s'
            self.db_connection.cursor(update_query,(self.get_user_email()))
        
        return True
        #set the login attempt count to 0 on successful login

        


    def unlock_user_account(self,email):
        select_query = 'SELECT user_id from user WHERE email = %s'
        self.db_connection.cursor.execute(select_query,(email,))
        user = self.db_connection.cursor.fetchone()
        #if the user is a valid user based on the supplied email and old password
        if user:
            user_id = user[0]
            status = 'inactive'
            password = self.util_obj.generate_default_password()
            update_query = 'UPDATE user set password = %s,status = %s WHERE user_id = %s'
            self.db_connection.cursor.execute(update_query,(password,status,user_id))
            self.db_connection.connection.commit()
            self.db_connection.close_connection()
            logging.info(f"Account unlocked for {email} at {datetime.now()}")
            status = 'success'
            message = "User account was successfully unlocked!"
            return (status,message)
        logging.info(f"Could not unlock account for {email} at {datetime.now()}")
        status = 'failure'
        message = 'Unable to retrieve the user!'
        return (status,message)


    def get_users_login_info(self):
        query = '''SELECT 
        u.firstname,
        u.lastname,
        u.email,
        lh.login_time AS last_login_time
        FROM user u
        LEFT JOIN (
                    SELECT user_id, MAX(login_time) AS login_time
                    FROM login_history 
                    GROUP BY user_id
                    )
        lh ON u.user_id = lh.user_id WHERE lh.login_time is not NULL
        ORDER BY last_login_time DESC'''
        self.db_connection.cursor.execute(query)
        users_login_info = self.db_connection.cursor.fetchall()
        return users_login_info



        
