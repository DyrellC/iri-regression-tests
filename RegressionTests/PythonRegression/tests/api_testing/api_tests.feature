@apiTesting
Feature: Test each of the API calls
	In order to ensure the calls are working, an address will need to be 
	defined, and each of the calls tested to make sure they return a correct
	response, and that that response is being logged in the correct location
	
	@getNodeInfo
	Scenario: GetNodeInfo from non-local host
		Given the host is "http://178.128.236.6"
		And the port is 14265 
		Then getNodeInfo will return type dict
		
		'''
		Should have been:
		Given the host is <host> and the port is <port>
		When getNodeInfo is called
		Then it will return type dict
		
		'''
	
	
	@logTest
	Scenario: Log GetNodeInfo response 
		Given the node host is "http://178.128.236.6" and the node port is 14265		
		Then getNodeInfo is called 3 times
		And 3 test log directories will be created
		Then each directory will have a log file containing the response   
	 	
	 	'''
	 	Should have been:
	 	Given ""
	 	When getNodeInfo is called 3 times
	 	Then 3 test log directories will be created
	 	And a response log file will be created in each directory 
	 	'''
	 	
		
	@getNeighbors
	Scenario: GetNeighbors from non-local host
		Given the host is "http://178.128.236.6"
		And the port is 14265
		Then getNeighbors will return type dict
		
		'''
		See above
		'''
		
	@logTest
	Scenario: Log GetNeighbors response
		Given the node host is "http://178.128.236.6" and the node port is 14265
		Then getNeighbors is called 3 times
		And 3 neighbor log directories will be created
		Then each directory will have a file listing the neighbors		

		'''
		See above
		'''
		
		