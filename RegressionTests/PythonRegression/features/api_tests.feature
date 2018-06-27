Feature: Test GetNodeInfo API call
	In order to ensure the calls are working,
	an address will need to be defined,
	and the response needs to be checked.
	
	Scenario: GetNodeInfo from non-local host
		Given The host is https://node.iotanode.host
		And The port is 443 
		Then GetNodeInfo will return type dict