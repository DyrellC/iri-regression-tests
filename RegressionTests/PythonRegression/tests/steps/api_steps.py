
# -*- coding: utf-8 -*-
from aloe import *
from iota import Iota
from util.logging import file_editing
from util.file_handling import directory_handling, file_handling

import os 
import time 
import json

dir = directory_handling.DirectoryHandling()
file = file_handling.FileHandling()
edit = file_editing.FileEditing()

testAddresses = {'host':[],'port':[]}
testVars = {}

#Scenario 1: GetNodeInfo call

@step(r'the host is "([^"]*)"')
def the_host_is(step,host):
    testAddresses['host'[0]] = host

@step(r'the port is (\d+)')
def the_port_is(step,port):
    testAddresses['port'[0]] = port
        
@step(r'getNodeInfo will return type dict')
def getnodeinfo_returns_dict(step):
    address = testAddresses['host'[0]] + ":" + str(testAddresses['port'[0]])
    api = Iota(address)
    info = api.get_node_info();
    
    assert type(info) is dict, "GetNodeInfo returned %r which means it did not succeed" % type(info)
    
    
## Scenario 2: Logging


@step(r'the node host is "([^"]*)" and the node port is (\d+)')
def set_address_for_calls(step, host,port):
    address = host + ":" + str(port)
    testVars['addresses'] = [] 
    testVars['addresses'[0]] = address
    
    
@step(r'getNodeInfo is called (\d+)')
def call_getNodeInfo_multiple_times(step,numTests):
    testVars['numTests'] = int(numTests)
    testVars['responses'] = []
    
    address = testVars['addresses'[0]]
    api = Iota(address)      
    responses = []    
   
    for i in range(testVars['numTests']):        
        response = api.get_node_info()     
        responses.append(response)
    
    testVars['responses'] = responses
         
        
@step(r'(\d+) test log directories will be created')
def test_log_dirs_created(step,numTests):
    logDir = "./API_testing_logs"
    dir.make_and_enter(logDir)  
    logDir = "./getNodeInfo_logs"
    dir.make_and_enter(logDir)
    
    testLogs = []
    logFiles = []
    
    for i in range(int(numTests)):
        testnum = i + 1
        
        logDir = "./Test%d/" % testnum
        dir.make_directory(logDir)      
        testLog =logDir + "Test%dGetNodeLog" % testnum
        testLogs.append(testLog)

        logFile = file.make_file(testLog)
        logFiles.append(logFile)
    
    testVars['logFiles'] = testLogs 
    testVars['logFilesId'] = logFiles
    
    
@step(r'each directory will have a log file containing the response')
def write_responses_to_files(step):
    assert len(testVars['logFiles']) > 0, "logFiles array empty {}".format(testVars['logFiles'])
    for i in range(len(testVars['logFiles'])):
        assert os.path.exists(testVars['logFiles'][i])
        for x in testVars['responses'][i]:
            contentWrite = str(x) + " : " + str(testVars['responses'][i][x])+"\n"
            edit.write_to_file(testVars['logFilesId'][i], contentWrite)
        
        file.close_file(testVars['logFilesId'][i])
        
    dir.change_directory("../../")
           


#Scenario 3: getNeighbors api test 
@step(r'getNeighbors will return type dict')
def getNeighbors_returns_type_dict(step):
    address = testAddresses['host'[0]] + ":" + str(testAddresses['port'[0]])
    api = Iota(address)
    info = api.get_neighbors();
    
    assert type(info) is dict, "GetNeighbors returned %r which means it did not succeed" % info
    
    
#Scenario 4: log neighbors
@step(r'getNeighbors is called (\d+) times')
def multiple_getNeighbors_called(step,numtests):
    testVars['numTests'] = int(numtests)
    
    address = testVars['addresses'[0]]
    api = Iota(address)      
    responses = []    
   
    for i in range(testVars['numTests']):        
        response = api.get_neighbors()     
        responses.append(response)
    
    testVars['responses'] = responses
         

@step(r'(\d+) neighbor log directories will be created')
def make_neighbor_log_dirs(step,numtests):
    logDir = "./API_testing_logs"
    exists = os.path.exists(logDir)
    if(exists):
        dir.change_directory(logDir)
    else:
        dir.make_and_enter(logDir)
        
    logDir = "./getNeighbors_logs"
    dir.make_and_enter(logDir)
    
    testLogs = []
    logFiles = []
    
    for i in range(int(numtests)):
        testnum = i + 1
        
        logDir = "./Test%d/" % testnum
        dir.make_directory(logDir)      
        testLog =logDir + "Test%dGetNeighbors" % testnum
        testLogs.append(testLog)

        logFile = file.make_file(testLog)
        logFiles.append(logFile)
    
    testVars['logFiles'] = testLogs 
    testVars['logFilesId'] = logFiles


@step(r'each directory will have a file listing the neighbors')
def log_neighbors(step):
    assert len(testVars['logFiles']) > 0, "logFiles array empty {}".format(testVars['logFiles'])
    for i in range(len(testVars['logFiles'])):
        assert os.path.exists(testVars['logFiles'][i])
        for x in testVars['responses'][i]:
            outputClass = type(testVars['responses'][i][x])
            neighbors = ""
            contentWrite = ""
            if outputClass == list:
                contentWrite += str(x) + " :\n"
                for y in range(len(testVars['responses'][i][x])):
                    contentWrite += "\t" + str(testVars['responses'][i][x][y]['address']) + "\n"   
                
            edit.write_to_file(testVars['logFilesId'][i], contentWrite)
        
        file.close_file(testVars['logFilesId'][i])
        
    dir.change_directory("../../")




