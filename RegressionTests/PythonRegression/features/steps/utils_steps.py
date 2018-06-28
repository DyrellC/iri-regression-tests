from aloe import step, world
from util.fileHandling import directory_handling, file_editing
import os

dir = directory_handling.DirectoryHandling()
file = file_editing.FileEditing()

testVar = {'key':'value'}


@step(r'a test is started')
def test_started(step):
    testVar.update({'testdir':"./oneTestLog"})
    testVar.update({'logdir':"./test%dLogs" % 1})
    
@step(r'a file directory should be created')
def file_directory_created(step):
    dir.make_directory(testVar['testdir'])
    
@step(r'a log directory should be created inside it')
def log_directory_created(step):
    dir.change_directory(testVar['testdir'])
    dir.make_directory(testVar['logdir'])
    dir.change_directory("../") 

 
##Scenario 2 
   
@step(r'(\d+) tests are started')
def tests_started(step,number):
    testVar["testdir"] = "./multipleTestLogs"
    testVar["logdir"] = []
    max = int(number)
    testVar["numTests"] = max

    for i in range(max):
        lognum = i + 1
        testVar['logdir'].append("./test%dLogs" % lognum)
        
@step(r'a separate subdirectory should be created for each test')
def log_direcotories_created(step):
    dir.change_directory(testVar['testdir'])
    max = len(testVar['logdir'])
    for i in range(max):
        dir.make_directory(testVar['logdir'][i])
            
    dir.change_directory("../") 
  
  
##Scenario 3  
    
@step(r'the test log directory exists')
def test_log_exists(step):
    testVar["dirLoc"] = './oneTestLog/test1Logs'
    
    exists = os.path.isdir(testVar['dirLoc'])
    assert exists is True

@step(r'create a test log file and write "([^"]*)" to it')
def create_test_file(step,content):
    dir.change_directory(testVar['dirLoc'])
    testFile = file.make_file('Test1')
    testVar['testFile'] = []
    testVar['testFile'[0]] = testFile
    file.write_to_file(testVar['testFile'[0]], content)
    file.close_file(testVar['testFile'[0]])
 
         
         
@step(r'check that the file contains "([^"]*)"')
def check_file(step,output):
    testFile = file.open_file_read('Test1')
    testVar['testFile'[0]] = testFile
    fileContents = file.read_from_file(testVar['testFile'[0]])
    file.close_file(testVar['testFile'[0]])
    dir.change_directory("../../")
    assert fileContents == output, 'fileContents = {} \nOutput = {}'.format(fileContents,output) 


##Scenario 4 

@step(r'(\d+) test log directories exist')
def log_directories_exist(step,num):
    testVar['logDirs'] = []
    testVar['numTests'] = int(num)
    for i in range(testVar['numTests']):
        logNum = i+1
        testVar['logDirs'[i]] = './oneTestLog/test%dLogs' % logNum
    
    for i in range(len(testVar['logDirs'])):
        exists = os.path.exists(testVar['logDirs'[i]])
        assert exists == True
    
@step(r'create a log file in each directory')
def create_log_directories(step):
    testVar['logFiles'] = []
    for i in range(len(testVar['logDirs'])):
        logFile = testVar['logDirs'[i]] + "/TestLog"
        testVar['logFiles'[i]] = logFile
     
    testVar['logFilesId'] = []    
    for i in range(len(testVar['logFiles'])):
        logFileId = file.make_file(testVar['logFiles'[i]])
        testVar['logFilesId'[i]] = logFileId
        
@step(r'write "([^"]*)" with test tag into each file')
def write_to_log_files(step,content):
    for i in range(len(testVar['logFilesId'])):
        file.write_to_file(testVar['logFilesId'[i]], content) 
        file.close_file('logFilesId'[i])
        
@step(r'check that each file has "([^"]*)" as its contents')
def check_log_files(step,output):
    for i in range(len(testVar['logFiles'])):
        logFile = file.open_file_read(testVar['logFiles'[i]])
        lines = file.read_from_file(logFile)
        assert lines == output, "Lines = {}\nOutput = {}".format(lines,output) 
        
        
