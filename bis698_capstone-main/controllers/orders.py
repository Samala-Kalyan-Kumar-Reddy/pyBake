from database import DB_Connection
from controllers.customers import Customer
from datetime import datetime
from .exception import OrderValidationException,DateEmptyError
class Order():
    message = ""
    def __init__(self,order_fulfilment_date ="",delivery_method="",
        customer = 0,salesperson =0,payment_status="",notes=""):
        self.order_fulfilment_date = order_fulfilment_date
        self.delivery_method = delivery_method
        self.salesperson = salesperson
        self.customer = customer
        self.payment_status = payment_status
        self.notes = notes

        self.customer = Customer()
        self.db_connection = DB_Connection()




    def set_order_fulfilment_date(self,order_fulfil_date):
        order_fulfil_date = datetime.strptime(order_fulfil_date, '%Y-%m-%d')
        if order_fulfil_date < datetime.now():
            raise OrderValidationException("Error: The fulfilment date must be in the future")
        else:
            self.order_fulfilment_date = order_fulfil_date

    def get_order_fulfilment_date(self):
        return self.order_fulfilment_date

    

    def set_delivery_method(self,delivery_method):
        self.delivery_method = delivery_method


    def get_delivery_method(self):
        return self.delivery_method


    
    def set_salesperson(self,salesperson):
        self.salesperson = salesperson


    def get_salesperson(self):
        return self.salesperson
        


    # def get_orders(self,customer_id):
    #     query = '''SELECT 
    #     order_id,
    #     order_date,
    #     order_status
    #     FROM orders WHERE customer = %s'''
    #     self.db_connection.cursor.execute(query,(customer_id,))
    #     order_info = self.db_connection.cursor.fetchall()
    #     return order_info

    def get_orders(self,customer_id):
        query = '''SELECT 
        order_id,
        order_date,
        order_status
        FROM orders WHERE customer = %s'''
        self.db_connection.cursor.execute(query,(customer_id,))
        order = self.db_connection.cursor.fetchall()
        return order




    def save_order(self,order_info):
        try:
            self.set_order_fulfilment_date(order_info['fulfilment_date'])
            self.order_fulfilment_date = self.get_order_fulfilment_date()
            self.delivery_method = order_info['delivery_method']
            self.customer = self.customer.get_customer_id(order_info['customer'])
            self.salesperson =order_info['salesperson']
            self.notes = order_info['notes']
            self.products = order_info['products']

            
        #check if the customer does not already exist

        
            query = 'INSERT into orders (order_fulfilment_date,delivery_method,salesperson,customer,notes)VALUES(%s,%s,%s,%s,%s)'
            insert_data = (self.order_fulfilment_date,
            self.delivery_method, self.salesperson,
            self.customer,
            self.notes)
            self.db_connection.cursor.execute(query,insert_data)
            self.db_connection.cursor.execute("SELECT LAST_INSERT_ID()")#get the ID of the last inserted record
            self.order_id = self.db_connection.cursor.fetchone()[0]
            self.db_connection.connection.commit()


            for product_id,quantity in self.products:
                query = 'INSERT INTO orderline (order_id,product_id,quantity) VALUES (%s,%s,%s)'
                values = (self.order_id,product_id,quantity)
                self.db_connection.cursor.execute(query,values)
            self.db_connection.connection.commit()


            query = 'INSERT INTO orderhistory (order_id,user_id,order_status,notes) VALUES (%s,%s,%s,%s)'
            values = (self.order_id,self.salesperson,1,self.notes)
            self.db_connection.cursor.execute(query,values)
            self.db_connection.connection.commit()
            self.db_connection.connection.close()
           

        except OrderValidationException as e:
            status = "Error"
            message = str(e)
            return (status,message)
        
        except DateEmptyError as e:
            status = "Error"
            message = str(e)
            return (status,message)
        
        # except ValueError as e:
        #     status = "Error"
        #     message = str(e)
        #     return (status,message)
        else:

            #get the last inserted orderID
            # self.db_connection.cursor.execute("SELECT LAST_INSERT_ID()")    
            # print('order_id: ',self.order_id)
            # print('products: ', self.products)
            # print('inserted data:', insert_data)
            status = "success"
            message = "Customer order was successfully created!"
            return (status,message)

    def get_status_id(self,status):
        query = 'SELECT orderstatus_id FROM orderstatus WHERE order_status_name = %s'
        self.db_connection.cursor.execute(query,(status,))    
        result = self.db_connection.cursor.fetchone()
        return result[0]

    def update_order_status(self,order_update_info):
        try:
            status = order_update_info['status']
            order_id = int(order_update_info['order'])
            user_id = order_update_info['user']
            notes = order_update_info['notes']
  
            #update the order table
            query = 'UPDATE  orders SET order_status = %s WHERE order_id = %s'
            self.db_connection.cursor.execute(query,(status,order_id))
            # self.db_connection.cursor.execute("SELECT LAST_INSERT_ID()")#get the ID of the last inserted record
            # self.order_id = self.db_connection.cursor.fetchone()[0]
            self.db_connection.connection.commit()


            query = 'INSERT INTO orderhistory (order_id,user_id,order_status,notes) VALUES (%s,%s,%s,%s)'
            values = (order_id,user_id,self.get_status_id(status),notes)
            self.db_connection.cursor.execute(query,values)
            self.db_connection.connection.commit()
            self.db_connection.connection.close()
           

        except Exception as e:
            status = "Error"
            message = str(e)
            return (status,message)
        else:

            #get the last inserted orderID
            # self.db_connection.cursor.execute("SELECT LAST_INSERT_ID()")    
            # print('order_id: ',self.order_id)
            # print('products: ', self.products)
            # print('inserted data:', insert_data)
            status = "success"
            message = "Order status upated successfully!"
            return (status,message)



    def get_customer_order(self,start_date,end_date,order_status):
        query = """SELECT o.order_id,
                    o.order_date,
                    CONCAT(c.firstname, ' ' ,c.lastname) as customer,
                    CONCAT(u.firstname, ' ' ,u.lastname )as salesperson,
                    o.order_fulfilment_date,
                    o.delivery_method,
                    o.order_status as status
                    FROM orders o
                    JOIN customer c ON c.customer_id = o.customer
                    JOIN user u ON u.user_id = o.salesperson
                    WHERE DATE(o.order_date) BETWEEN %s AND %s """
                    # WHERE o.order_date BETWEEN COALESCE(%s, '1900-01-01') AND COALESCE(%s, '9999-12-31')"""
        # order_status = None  # Replace with the desired order status or None
        params = [start_date, end_date]  # Initial parameter list

        if order_status is not None and order_status != "":
            query += "AND o.order_status = %s"
            params.append(order_status)  
        
        
        self.db_connection.cursor.execute(query,params)
        customer_order = self.db_connection.cursor.fetchall()
        return customer_order


    def order_count(self):
            query = "SELECT COUNT(*) AS order_count FROM orders"
            self.db_connection.cursor.execute(query)
            order_count = self.db_connection.cursor.fetchone()
            return order_count[0]
    
    def total_sale(self):
        query = """SELECT
                        SUM(ol.quantity * p.product_price) AS total_sale_amount
                        FROM
                        orders o
                        JOIN
                        orderline ol ON o.order_id = ol.order_id
                        JOIN
                        products p ON ol.product_id = p.product_id"""
        self.db_connection.cursor.execute(query)
        total_sale = self.db_connection.cursor.fetchone()
        return total_sale[0]
