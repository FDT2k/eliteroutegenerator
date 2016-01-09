import mysql.connector

add_commodity = ("insert into commodity (name) VALUES(%s)")
add_system = ("insert into system (name) value(%s)")
add_station =("insert into station (name,system_id) value(%s,%s)")
add_market = ("insert into market (station_id,commodity_id,buyPrice,sellPrice,demand,supply,last_updated) VALUES (%s,%s,%s,%s,%s,%s,NOW())")
delete_market =("delete from market where station_id = %s and commodity_id =%s")

cnxpool = mysql.connector.pooling.MySQLConnectionPool(pool_name = "mypool",
                                                      pool_size = 32,
                                                      user='elite', password='qpTrtzLYJ4VXeMVX',
                              host='vps.ditore.ch',
                              database='elitedangerous')
print "pooool"
class EliteModel():

    def commit (self):
        self.db.commit()
        self.cursor.close()
        self.db.close()
        self.db = cnxpool.get_connection()
        self.cursor = self.db.cursor()

    def __init__(self):
        
        self.db = cnxpool.get_connection()
        self.cursor = self.db.cursor()


    def update_system(self,system_id,system):
        self.cursor.execute("update system set x=%s,y=%s,z=%s,imported_id=%s where system_id =%s",(system["x"],system["y"],system["z"],system["id"],system_id))


    def update_market(self,data):
        self.cursor.execute(delete_market,(data[0],data[1]))
        self.cursor.execute(add_market,data)
       

    def get_system(self,name):

       # cursor = db.cursor()

        query = ("select system_id,name from system where name=%s")
        self.cursor.execute(query, (name,))
        
        for (_id,name) in self.cursor:
                return _id
        
       # cursor.close() 
       # cursor = db.cursor()
        #print "adding system: "+name
        self.cursor.execute(add_system,(name,))

        _id = self.cursor.lastrowid
       # cursor.close()

        return _id
      
    def get_system_by_imported_id(self,name):

       # cursor = db.cursor()

        query = ("select system_id from system where imported_id=%s")
        self.cursor.execute(query, (name,))
        
        for (_id,) in self.cursor:
           return _id
        
        return 0

    def get_commodity(self,name):
     #   cursor = db.cursor()
        query = ("select * from commodity where name=%s")
        self.cursor.execute(query, (name,))

        for (_id,name) in self.cursor:
            return _id
        
       # cursor.close() 
       # cursor = db.cursor()
        print "adding commodity: "+name
        self.cursor.execute(add_commodity,(name,))
        
        _id = self.cursor.lastrowid
      #  cursor.close()

        return _id



    def get_station(self,name,system_id):
     #   cursor = db.cursor()
        query = ("select * from system where name=%s and system_id = %s")
        self.cursor.execute(query, (name,system_id))
        print "whut"
        for (_id,station_id,name) in self.cursor:
            return _id
        
    #    cursor.close() 
    #    cursor = db.cursor()
        print "adding station: "+name
        self.cursor.execute(add_station,(name,system_id))
        
        _id = self.cursor.lastrowid
    #    cursor.close()

        return _id

    def update_station(self,station_id,station):
        self.cursor.execute("update station set dist_from_star =%s where station_id =%s",(station["distance_to_star"],station_id))
