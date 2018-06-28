Feature: Test GetNodeInfo API call
	In order to ensure the calls are working,
	an address will need to be defined,
	and the response needs to be checked.
	
	Scenario: GetNodeInfo from non-local host
		Given the host is "https://node.iotanode.host"
		And the port is 443 
		Then getNodeInfo will return type dict