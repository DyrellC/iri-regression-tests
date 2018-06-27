'''
Created on Jun 26, 2018

@author: d
'''
# -*- coding: utf-8 -*-


from aloe import step,world
from iota import Iota



@step(r'The host is "([^"]*)"')
def the_host_is(step,host):
    world.host = host
    # assert True, "Set Host Failed"

@step(r'The port is (\d+)')
def the_port_is(step,port):
    world.port = port
    # assert True, "Set Port Failed"
        
@step(r'GetNodeInfo will return type dict')
def getnodeinfo_returns_dict(step):
    address = world.host + ":" + str(world.port)
    api = Iota(address)
    try:
        info = api.get_node_info();
    except:
        info = "Error: getNodeInfo did not succeed"
    
    assert type(info) is dict, "GetNodeInfo returned %r which means it did not succeed" % type(info)
    
    
    

