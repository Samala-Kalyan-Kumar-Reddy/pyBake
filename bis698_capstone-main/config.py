

class Config():
    domain = 'pybake.com'
    smtp_username="kalyanreddy434@gmail.com"
    smtp_password="ahme lnlz sypn mqxo"
    def __init__(self):
        self.db_host = 'pybake.cpbm3wmseaoj.us-east-2.rds.amazonaws.com'#new database
        self.user='admin'
        self.password='Admin123$'
        # self.db_host = 'pybakedb.cvdpwt9dypjw.us-east-1.rds.amazonaws.com'#old database
    # database ='pyBake_db'
        self.database ='py_Bake_testDB'



    @classmethod
    def get_domain(cls):
        return cls.domain
    


   
        
   