from aloe import *
from iota import Iota

config = {}
responses = {'getNodeInfo':{},'getNeighbors':{}}   
    
#GetNodeInfo tests
@step(r'getNodeInfo is called on "([^"]*)"')
def getNodeInfo_is_called(step,nodeName):
    config['apiCall'] = 'getNodeInfo'
    config['nodeId'] = nodeName
     
    api = prepare_api_call(nodeName)    
    response = api.get_node_info()
    assert type(response) is dict, "Get Node Info returned wrong type: {}".format(type(response))
    
    responses['getNodeInfo'][nodeName] = response
    
@step(r'a response with the following is returned:')
def compare_getNodeInfo_response(step):
    keys = step.hashes
    nodeId = config['nodeId']
    print(nodeId)
    print(config['apiCall'])
    print(responses)
    if config['apiCall'] == 'getNodeInfo':
        response = responses['getNodeInfo'][nodeId]
        responseKeys = list(response.keys())
        responseKeys.sort()
        for i in range(len(response)):
            assert str(responseKeys[i]) == str(keys[i]['keys']), "There was an error with the response" 
    
    elif config['apiCall'] == 'getNeighbors':
        response = responses['getNeighbors'][nodeId] 
        responseKeys = list(response.keys())
        for x in range(len(response)):
            try:
                for i in range(len(response[x])):
                    assert str(responseKeys[i]) == str(keys[i])
            except:
                print("No neighbors to verify response with")        
                    
#GetNeighbors tests
@step(r'getNeighbors is called on "([^"]*)"')
def getNeighbors_is_called(step,nodeName):
    config['apiCall'] = 'getNeighbors'
    config['nodeId'] = nodeName
    
    api = prepare_api_call(nodeName)
    response = api.get_neighbors()
    assert type(response) is dict, "Get Neighbors returned wrong type: {}".format(type(response))
    
    responses['getNeighbors'][nodeName] = response
    
    
    
    
    
def prepare_api_call(nodeName):
    host = world.machines[nodeName]
    address ="http://"+ host + ":14265"
    api = Iota(address)
    return api

def check_responses_for_call(apiCall):
    if len(responses[apiCall]) > 0:
        return True
    else:
        return False
    
def fetch_response(apiCall):
    return responses[apiCall]