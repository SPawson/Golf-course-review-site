class Record:
    """Finds the value of certain
    key/value pair passed in"""
    @staticmethod
    def find_value(obj,key):
        value = ""
        for fields in obj:
            value = fields[key]
        return str(value)
    
    @staticmethod
    def update_kv(obj,key,value):
        obj[key] = value
        return obj
        
