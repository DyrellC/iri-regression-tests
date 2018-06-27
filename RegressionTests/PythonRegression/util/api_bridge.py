from iota import Iota 

'''
Created on Jun 26, 2018

@author: d
'''

class API(object):
    '''
    classdocs
    '''
    
    def __init__(self,host,port):
        self.host = host
        self.port = port
    
    
    def setHost(self,host):
        self.host = host
    
    def setPort(self, port):
        self.port = str(port)
       
    def getHost(self):
        return self.host

    def getPort(self):
        return self.port
    
    
    
    def getNodeInfo(self):
        try:
            address = self.host + ":" + self.port
            api = Iota(address)
            response = api.get_node_info()
        
            return response
        except: 
            return "Error: getNodeInfo did not succeed" 
        