from aloe import *
from yaml import load,dump, Loader, Dumper
import io
from iota import Iota
from pip._vendor.pyparsing import empty

config = {}
responses = {'getNodeInfo':{},'getNeighbors':{}}

#Configuration

def configuration(step,yamlPath):
    stream = io.open(yamlPath,'r')
    machine1 = load(stream,Loader=Loader)
    config['seeds'] = machine1.get('seeds')
    
    nodes = {}
    keys = machine1.keys()    
    for i in keys:
        if i != 'seeds':
            name = i
            host = machine1[i]['host']
            nodes[name] = host
            
                
    config['nodes'] = nodes
    

def set_up_global(step):
    world.machines = config['nodes']
    world.seeds = config['seeds']
    
    
    
#GetNodeInfo tests

def getNodeInfo_is_called(step,nodeName):
    api = prepare_api_call(nodeName)    
    response = api.get_node_info()
    assert type(response) is dict, "Get Node Info returned wrong type: {}".format(type(response))
    
    responses['getNodeInfo'][nodeName] = response
    

def compare_getNodeInfo_response(step,nodeId,keys):
    response = responses['getNodeInfo'][nodeId]
    responseKeys = list(response.keys())
    responseKeys.sort()
    
    for i in range(len(response)):
        assert str(responseKeys[i]) == str(keys[i]['keys']), "There was an error with the response" 
    

#GetNeighbors tests

def getNeighbors_is_called(step,nodeName):
    api = prepare_api_call(nodeName)
    response = api.get_neighbors()
    assert type(response) is dict, "Get Neighbors returned wrong type: {}".format(type(response))
    
    responses['getNeighbors'][nodeName] = response
    
def compare_getNeighbors_response(step,nodeId,keys):
    response = responses['getNeighbors'][nodeId]
    responseKeys = list(response.keys)
    
    for x in range(len(response)):
        for i in range(len(response[x])):
            assert str(responseKeys[i]) == str(keys[i])
        
    
    
    
    
    
def prepare_api_call(nodeName):
    host = world.machines[nodeName]
    address ="http://"+ host + ":14265"
    api = Iota(address)
    return api
    
    