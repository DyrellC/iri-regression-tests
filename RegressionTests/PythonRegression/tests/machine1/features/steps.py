from aloe import *
from aloe import steps
from tests.steps import machine_test_steps


steps = machine_test_steps
node = {}

@step(r'node configuration "([^"]*)"')
def configure(step,configPath):
    steps.configuration(step,configPath)
    
    
@step(r'set up global environment')
def set_up_global_env(step):
    steps.set_up_global(step)
    
@step(r'getNodeInfo is called on Node "([^"]*)"')
def call_getNodeInfo(step,nodeName):
    node['nodeId'] = nodeName
    node['currentAPI'] = 'getNodeInfo'
    steps.getNodeInfo_is_called(step, nodeName)
 
    
@step(r'a response with the following is returned:')
def response_comparison(step):
    keys = step.hashes
    try:
        if node['currentAPI'] == 'getNodeInfo':
            steps.compare_getNodeInfo_response(step,node['nodeId'],keys)
        elif node['currentAPI'] == 'getNeighbors':
            steps.compare_getNeighbors_response(step,node['nodeId'],keys)
    except:
        print('Current API is not recognized: {}'.format(node['currentAPI'])) 
        
        
        
  
@step(r'getNeighbors is called on Node "([^"]*)"')
def call_getNeighbors(step,nodeName):
    node['nodeId'] = nodeName
    node['currentAPI'] = 'getNeighbors'
    steps.getNeighbors_is_called(step, nodeName)
    
