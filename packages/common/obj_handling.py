class Record:
    
    @staticmethod   
    def find_value(obj,key):
    #Finds the value of certain key/value pair passed in
        value = []
        for fields in obj:
            value.append(fields[key]) 
        return value
    
    @staticmethod
    def update_kv(obj,key,value):
        #Updates a key value pair with new value
        obj[key] = value
        return obj
    
    @staticmethod
    def return_list(obj):
    #Returns list of items in collection
        records = []
        for record in obj:
            records += [record]
        return records
    
    @staticmethod
    def create_course_record(obj):
    #Creates a dictionary from the form fields
        data = {
        'course_name':obj.get('course_name'),
        'address_line_1':obj.get('address_line_1'),
        'address_line_2': obj.get('address_line_2'),
        'address_line_3': obj.get('address_line_3'),
        'region': obj.get('region'),
        'postcode': obj.get('postcode'),
        'course_img': obj.get('course_img'),
        'affiliate_link': obj.get('affiliate_link'),
        'avg_rating': 0,
        'par': int(obj.get('par')),
        'description': obj.get('description')
        }
        return data

        
