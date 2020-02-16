from packages.common.obj_handling import Record
import math

class Search_Results:
    def __init__(self,limit):
        self.limit = None
        self.items = None
        self.amount = None
        self.pagination_amount= None

    def paginiation(self):
        self.pagination_amount = math.ceil(self.amount / self.limit)
        
