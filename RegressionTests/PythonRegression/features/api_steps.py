'''
Created on Jun 26, 2018

@author: d
'''
# -*- coding: utf-8 -*-


from lettuce import step
from util import api_bridge

# Define generic API Bridge
host = "https://localhost"
port = 14265
api = api_bridge.API(host,port)


@step('Given The host is https://node.iotanode.host')
def the_host_is_https_node_iotanode_host(step):
    api.setHost("https://node.iotanode.host")
    # assert True, "Set Host Failed"

@step('And The port is 443')
def the_port_is(step):
    api.setPort(443)
    # assert True, "Set Port Failed"
        
@step('Then GetNodeInfo will return type dict')
def getnodeinfo_returns_dict(step):
    info = api.getNodeInfo();
    assert type(info) is dict
    
    
    

