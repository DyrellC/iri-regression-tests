from aloe import step, world
from util.fileHandling import directory_handling, file_editing

dir = directory_handling.DirectoryHandling()

@step(r'A test is started')
def test_started(step):
    world.testdir = "./oneTestLog"
    world.logdir = "./test%dLogs" % 1
    
@step(r'A file directory should be created')
def file_directory_created(step):
    dir.make_directory(world.testdir)
    
@step(r'A log directory should be created inside it')
def log_directory_created(step):
    dir.change_directory(world.testdir)
    dir.make_directory(world.logdir)
    dir.change_directory("../") 

   
@step(r'(\d+) tests are started')
def tests_started(step,number):
    world.testdir = "./multipleTestLogs"
    world.logdir = []
    max = int(number)
    for i in range(max):
        lognum = i + 1
        world.logdir.append("./test%dLogs" % lognum)
        
@step(r'A separate subdirectory should be created for each test')
def log_direcotories_created(step):
    dir.change_directory(world.testdir)
    max = len(world.logdir)
    for i in range(max):
        dir.make_directory(world.logdir[i])
            
    dir.change_directory("../") 

        
