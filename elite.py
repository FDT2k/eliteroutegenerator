import zlib
import zmq
import simplejson
import sys
import time

import os
import urllib2,urllib
from FileUpdater import FileUpdater
from FileUpdater import StationUpdater

from model import EliteModel
import signal

from ZMQUpdater import ZMQUpdater



#db = mysql.connector.connect()


def download_file_to(url,_file):

    download_path = _file+"_tmp"
    final_path = _file
    if not os.path.isfile(final_path):  # downloading the file if it doesn't exists

        try:
            u = urllib2.urlopen(url,None,30)

            meta = u.info()

            if len(meta.getheaders("Content-Length")) > 0:

                f = open(download_path , 'wb')
                file_size = int(meta.getheaders("Content-Length")[0])
                print("Downloading: %s Bytes: %s" % (url, file_size))
                file_size_dl = 0
                block_sz = 8192
                while file_size_dl < file_size:# and not self.stopEvent.isSet():
                    buff = u.read(block_sz)
                    if not buff:  # eof or error ?
                        break

                    file_size_dl += len(buff)
                    f.write(buff)
                    #self.status = "%d/%d %3.0f%%" % (i + 1, len(theFiles), file_size_dl * 100. / file_size)
                    print "dl"
                    #self.status = self.status + chr(8)*(len(self.status)+1)
                    #print self.status,
                    #logger.info(self.status)
                    sys.stdout.flush()
                f.close()
                
                #print(self.status)
                #if self.stopEvent.isSet():
                #    break
                # move the file to final folder
                os.rename(download_path, final_path )

            else:
                print ("file " + url + " not found on the server")
        except Exception as e:
            print ("Cannot get url "+url+" error:"+str(e))


def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    fileupdater.stopEvent.set();
    zmqupdater.stopEvent.set();
    sys.exit(0)



fileupdater = FileUpdater()

stationupdater = StationUpdater()
zmqupdater = ZMQUpdater()

"""
 "  Start
"""    
def main():
    signal.signal(signal.SIGINT, signal_handler)

    download_file_to("https://eddb.io/archive/v4/systems.json","/tmp/systems.json")
    download_file_to("https://eddb.io/archive/v4/stations.json","/tmp/stations.json")

   # update_system_from_file();
    
    fileupdater.start()
    stationupdater.start()
    zmqupdater.start()
        
    while True:
        pass
        

if __name__ == '__main__':
    main()