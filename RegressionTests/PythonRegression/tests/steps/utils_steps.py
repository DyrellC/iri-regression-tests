from aloe import step, world
from util.fileHandling import directory_handling,file_handling
from util.logging import file_editing
import os

dir = directory_handling.DirectoryHandling()
file = file_handling.FileHandling()
edit = file_editing.FileEditing()

testVar = {'key':'value'}



def test_started(step):
    testVar.update({'testdir':"./oneTestLog"})
    testVar.update({'logdir':"./test%dLogs" % 1})
    
def file_directory_created(step):
    dir.make_directory(testVar['testdir'])
    
def log_directory_created(step):
    dir.change_directory(testVar['testdir'])
    dir.make_directory(testVar['logdir'])
    dir.change_directory("../") 

 
##Scenario 2 
   
def tests_started(step,number):
    testVar["testdir"] = "./multipleTestLogs"
    testVar["logdir"] = []
    max = int(number)
    testVar["numTests"] = max

    for i in range(max):
        lognum = i + 1
        testVar['logdir'].append("./test%dLogs" % lognum)
        
def log_directories_created(step):
    dir.change_directory(testVar['testdir'])
    max = len(testVar['logdir'])
    for i in range(max):
        dir.make_directory(testVar['logdir'][i])
            
    dir.change_directory("../") 
  
  
##Scenario 3  
    
def test_log_exists(step):
    testVar["dirLoc"] = './oneTestLog/test1Logs'
    exists = os.path.isdir(testVar['dirLoc'])
    assert exists is True

def create_test_file(step,content):
    print(testVar)
    dir.change_directory(testVar['dirLoc'])
    testFile = file.make_file('Test1')
    testVar['testFile'] = []
    testVar['testFile'[0]] = testFile
    edit.write_to_file(testVar['testFile'[0]], content)
    file.close_file(testVar['testFile'[0]])
 
         
         
def check_file(step,output):
    testFile = file.open_file_read('Test1')
    testVar['testFile'[0]] = testFile
    fileContents = edit.read_from_file(testVar['testFile'[0]])
    file.close_file(testVar['testFile'[0]])
    dir.change_directory("../../")
    assert fileContents == output, 'fileContents = {} \nOutput = {}'.format(fileContents,output) 


##Scenario 4 

def log_directories_exist(step,num):
    logDirs = []
    testVar['numTests'] = int(num)
    for i in range(testVar['numTests']):
        logNum = i+1
        logDirs.append('./multipleTestLogs/test%dLogs' % logNum) 
    
    testVar['logDirs'] = logDirs
    
    for i in range(len(testVar['logDirs'])):
        exists = os.path.exists(testVar['logDirs'][i])
        assert exists == True, "Path doesn't exist {}".format(testVar['logDirs'][i])
    
def create_log_directories(step):
    logFiles = []
    for i in range(len(testVar['logDirs'])):
        logFile = testVar['logDirs'][i] + "/TestLog"
        logFiles.append(logFile)
    
    testVar['logFiles'] = logFiles
    logFilesId = []
    assert len(testVar['logFiles']) > 0, "logFiles is empty {}".format(testVar['logFiles'])    
    
    for i in range(len(testVar['logFiles'])):
        logFileId = file.make_file(testVar['logFiles'][i])
        logFilesId.append(logFileId)
        exists = os.path.exists(testVar['logFiles'][i])
        assert exists is True, "Log file not created"

    testVar['logFilesId'] = logFilesId 

        
def write_to_log_files(step,content):
    for i in range(len(testVar['logFilesId'])):
        edit.write_to_file(testVar['logFilesId'][i], content) 
        file.close_file(testVar['logFilesId'][i])
        
def check_log_files(step,output):
    for i in range(len(testVar['logFiles'])):
        logFile = file.open_file_read(testVar['logFiles'][i])
        lines = edit.read_from_file(logFile)
        assert lines == output, "Lines = {}\nOutput = {}".format(lines,output) 
        
        
