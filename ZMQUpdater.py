from threading import Thread
from threading import Event
from model import EliteModel
import simplejson
import sys
import zlib
import zmq
import simplejson
import sys
import time
"""
 "  Configuration
"""
relayEDDN             = 'tcp://eddn-relay.elite-markets.net:9500'
#__timeoutEDDN           = 600000 # 10 minuts
timeoutEDDN           = 60000 # 1 minut
context     = zmq.Context()
subscriber  = context.socket(zmq.SUB)

subscriber.setsockopt(zmq.SUBSCRIBE, "")

class ZMQUpdater(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.interval = 10
        self.model = EliteModel()
        self.stopEvent = Event()

    def run(self):
        print ("Running ZMQUpdater")
        model = self.model
        while True:
            try:
                subscriber.connect(relayEDDN)
                print 'Connect to EDDN'
                sys.stdout.flush()
                
                poller = zmq.Poller()
                poller.register(subscriber, zmq.POLLIN)
                

               



                while True:
                    socks = dict(poller.poll(timeoutEDDN))
                    if socks:
                        if socks.get(subscriber) == zmq.POLLIN:
                            __message   = subscriber.recv(zmq.NOBLOCK)
                            __message   = zlib.decompress(__message)
                            __json      = simplejson.loads(__message)
             
                            print "new message:"
                            print __json["$schemaRef"]
                          #  print __json["message"]
                            if __json["$schemaRef"] == "http://schemas.elite-markets.net/eddn/commodity/2":
                                message = __json["message"]

                                systemName = message["systemName"];
                                stationName = message["stationName"];
                                system_id = model.get_system(systemName)
                                station_id = model.get_station(stationName,system_id)
                               
                                for comm in message["commodities"]:
                                    print comm
                                    commodity_id = model.get_commodity(comm["name"])
                                    #print "updating market info"
                                    model.update_market((station_id,commodity_id,comm["buyPrice"],comm["sellPrice"],comm["demand"],comm["supply"]))
                               
                                model.commit()
                               


                            message = None
                            sys.stdout.flush()
                    else:
                        print 'Disconnect from EDDN (After timeout)'
                        sys.stdout.flush()
                        
                        subscriber.disconnect(__relayEDDN)
                        break
                    if self.stopEvent.is_set():
                        return
                    
            except zmq.ZMQError, e:
                print 'Disconnect from EDDN (After receiving ZMQError)'
                print 'ZMQSocketException: ' + str(e)
                sys.stdout.flush()
                
                subscriber.disconnect(__relayEDDN)
                time.sleep(10)

            if self.stopEvent.is_set():
                return
                
            


