class Record:
    
    @staticmethod   
    def find_value(obj,key):
    #Finds the value of certain key/value pair passed in
        value = ""
        for fields in obj:
            value = fields[key]
        return str(value)
    
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

        
