@apiTesting
Feature: Test GetNodeInfo API call
	In order to ensure the calls are working,
	an address will need to be defined,
	and the response needs to be checked.
	
	@getNodeInfo
	Scenario: GetNodeInfo from non-local host
		Given the host is "https://node.iotanode.host"
		And the port is 443 
		Then getNodeInfo will return type dict
	
	@logTest
	Scenario: Log GetNodeInfo response 
		Given the node host is "https://node.iotanode.host" and the node port is 443		
		Then getNodeInfo is called 3 times
		And 3 test log directories will be created
		Then each directory will have a log file containing the response   