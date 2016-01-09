from threading import Thread
from threading import Event
from model import EliteModel
import simplejson
import sys

class FileUpdater(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.interval = 10
        self.model = EliteModel()
        self.stopEvent = Event()

    def run(self):
        print ("Running FileUpdater")
        while not self.stopEvent.wait(self.interval):
            #break # temporary disabled

            self.checkUpdate()
            pass




    def checkUpdate(self):
        try:
            print "checking if file exists"    
            self.update_system_from_file()        

        except Exception as e:
            print "error "+str(e)


    def update_system_from_file(self):

        #parse data from the file
        data = []
        with open("/tmp/systems.json") as data_file:    
            data = simplejson.load(data_file)

        
        
        
        print str(len(data))+" systems to import"

        outputEvery=10
        count =0
        countOut = 0
        for system in data:
            #print system
            system_id = self.model.get_system(system["name"]);
            
            self.model.update_system(system_id,system)
            
           
            count=count +1
            countOut= countOut+1
            if countOut >= outputEvery:
                countOut=0
                print "imported "+str(count)+" systems"
                sys.stdout.flush()    
                self.model.commit()
                if self.stopEvent.is_set():
                    return

              
        self.model.commit()
        data = None


class StationUpdater(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.interval = 10
        self.model = EliteModel()
        self.stopEvent = Event()

    def run(self):
        print ("Running StationUpdater")
        while not self.stopEvent.wait(self.interval):
            #break # temporary disabled

            self.checkUpdate()
            pass




    def checkUpdate(self):
        try:
            print "checking if file exists"    
            self.update_system_from_file()        

        except Exception as e:
            print "error "+str(e)


    def update_system_from_file(self):

        #parse data from the file
        data = []
        with open("/tmp/stations.json") as data_file:    
            data = simplejson.load(data_file)

        
        
        
        print str(len(data))+" stations to import"

        outputEvery=10
        count =0
        countOut = 0
        for station in data:
            #print station["system_id"]
            system_id = self.model.get_system_by_imported_id(station["system_id"]);
            #print system_id
            if system_id != 0:
                #print station["system_id"]
                station_id = self.model.get_station(station["name"],system_id)
                #print station["system_id"]
                self.model.update_station(station_id,station)
                
               
            count=count +1
            countOut= countOut+1
            if countOut >= outputEvery:
                countOut=0
                print "imported "+str(count)+" stations"
                sys.stdout.flush()    
                self.model.commit()
                if self.stopEvent.is_set():
                    return

              
        self.model.commit()
        data = None


