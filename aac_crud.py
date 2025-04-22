from pymongo import MongoClient

class AnimalShelterCRUD():
    def __init__(self, username, password, host, port, database, collection):
        # Connection Variables
        USER = username
        PASS = password
        HOST = host
        PORT = port
        DB = database
        COL = collection
        
        # Initialize Connection
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
        self.database = self.client[DB]
        self.collection = self.database[COL]
        
    # Method to implement Create
    def create(self, data):
        try:
            result = self.collection.insert_one(data)
            return True if result.inserted_id else False
        except Exception as e:
            print(f"Error inserting document: {e}")
            return False
                
    # Method to implement Read
    def read(self, query):
        try:
            cursor = self.collection.find(query)
            return list(cursor)
        except Exception as e:
            print(f"Error querying documents: {e}")
            return []
          
    # Method to implement Update
    def update(self, query, new_data):
        try:
            result = self.collection.update_many(query, {"$set": new_data})
            return result.modified_count
        except Exception as e:
            print(f"An error occured: {e}")
            return 0
          
    # Method to implement Delete
    def delete(self, query):
        try: 
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as e: 
            print(f"An error occured: {e}")
            return 0
      
    
