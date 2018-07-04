from tests.steps import utils_steps
from aloe import *

utils = utils_steps

@step(r'a test is started')
def start_test(step):
    utils.test_started(step)

@step(r'a file directory should be created')
def file_directory_created(step):
    utils.file_directory_created(step)

@step(r'a log directory should be created inside it')
def log_directory_created(step):
    utils.log_directory_created(step)

@step(r'(\d+) tests are started')
def tests_started(step,numTests):
    utils.tests_started(step,numTests)

@step(r'a separate subdirectory should be created for each test')
def log_directories_created(step):
    utils.log_directories_created(step)

@step(r'the test log directory exists')
def test_log_exists(step):
    utils.test_log_exists(step)

@step(r'create a test log file and write "([^"]*)" to it')
def create_test_file(step,content):
    utils.create_test_file(step,content)

@step(r'check that the file contains "([^"]*)"')
def check_file(step,content):
    utils.check_file(step,content)

@step(r'(\d+) test log directories exist')
def log_directories_exist(step,numTests):
    utils.log_directories_exist(step,numTests)

@step(r'create a log file in each directory')
def create_log_directories(step):
    utils.create_log_directories(step)
    
@step(r'write "([^"]*)" with test tag into each file')
def write_to_log_files(step,content):
    utils.write_to_log_files(step,content)
    
@step(r'check that each file has "([^"]*)" as its contents')
def check_log_files(step,content):
    utils.check_log_files(step,content)
    