from packages.common.obj_handling import Record
import math

class Pagination:
    """
    Calculates all necessary parameters for controlling pagination
    """
    def __init__(self,limit, count, session_skips):
        self.limit = limit
        self.results = None
        self.session_skips = session_skips
        self.skips = None
        self.count = count
        self.pagination_amount= None

        self.paginiation()
        self.calculate_skips()

        self.nextUrl = self.has_next_url()
        self.prevUrl = self.has_prev_url()

        
        

    def paginiation(self):
        self.pagination_amount = math.ceil(self.count / self.limit)

    def calculate_skips(self):
        self.skips = round(int(self.session_skips) * self.limit)

    def has_next_url(self):
        if self.pagination_amount -1 != int(self.session_skips) and self.count != 0:
            return True
        else:
            return False
    def has_prev_url(self):
        if int(self.session_skips) != 0:
            return True
        else:
            return False

class Search:

    @staticmethod
    #determines the search term that will be used in db search
    def search_term(region,course_name,min_rating):
        if region != None and course_name != "" and min_rating != 0:
            search = {"region": region, "course_name":{"$regex" : course_name, "$options":'i'} , 'avg_rating':{"$gte": min_rating}}
        elif region != None and course_name != "" :
            search = {"region": region, "course_name": {"$regex" : course_name, "$options":'i'}}
        elif region != None and min_rating != 0 :
            search = {"region": region, "avg_rating":{"$gte": min_rating}}
        elif course_name != "" and min_rating != 0 :
            search = {"course_name": {"$regex" : course_name, "$options":'i'}, "avg_rating":{"$gte": min_rating}}
        elif course_name != "" and min_rating != 0 :
            search = {"course_name": {"$regex" : course_name, "$options":'i'}, "avg_rating":{"$gte": min_rating}}
        elif  region != None:
            search = {"region": region}
        elif  min_rating != 0:
            search = {"avg_rating":{"$gte": min_rating}}
        elif  course_name != "":
            search = {"course_name": {"$regex" : course_name, "$options":'i'}}
        else: 
            search = ""

        return search