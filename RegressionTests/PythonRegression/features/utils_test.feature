Feature: Test file creation 
	Test the file creation utility to make sure 
	it functions as intended
	
	
	Scenario: Create a test log directory 
		Given A test is started 
		Then A file directory should be created
		And A log directory should be created inside it
		
	
	Scenario: Create multiple test log directories
		Given 5 tests are started
		Then A file directory should be created
		And A separate subdirectory should be created for each test
		
	