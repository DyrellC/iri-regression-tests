'''
Created on Jun 26, 2018

@author: d
'''
# -*- coding: utf-8 -*-
from aloe import *
from iota import Iota
from util.logging import file_editing
from util.fileHandling import directory_handling, file_handling

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
    try:
        info = api.get_node_info();
    except:
        info = "Error: getNodeInfo did not succeed"
    
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
           

