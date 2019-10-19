import os

class App_Connection:
    """Defining app connection method parameters"""
    def __init__(self):
        self.host_val = os.environ.get('IP')
        self.port_val = int(os.environ.get('PORT'))
        self.m_uri = os.environ.get('MONGO_URI')
        self.db_name = 'golf_course'