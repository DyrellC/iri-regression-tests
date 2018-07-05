@machine1
Feature: Test API calls on Machine 1
	Test various api calls to make sure they are responding
	correctly 
	

	
	Scenario: GetNodeInfo is called
		Given getNodeInfo is called on "nodeA" 
		Then a response with the following is returned:
		|keys								|
		|appName							|	
		|appVersion							|
		|duration							|
		|jreAvailableProcessors				|
		|jreFreeMemory						|
		|jreMaxMemory						|
		|jreTotalMemory						|
		|jreVersion							|		
		|latestMilestone					|
		|latestMilestoneIndex				|
		|latestSolidSubtangleMilestone		|
		|latestSolidSubtangleMilestoneIndex |
		|milestoneStartIndex				|
		|neighbors							|
		|packetsQueueSize					|
		|time								|
		|tips								|
		|transactionsToRequest				|
	
		
	Scenario: Log GetNodeInfo
		Given a response for "getNodeInfo" exists
		Then create the log directory "./tests/features/machine1/logs/get_node_info_logs/"
		And log the response to the file "getNodeInfoLog.txt"		 
		
	
	Scenario: GetNeighbors is called
		Given getNeighbors is called on "nodeA"
		Then a response with the following is returned:
		|keys							|
		|address						|
		|numberOfAllTransactions		|
		|numberOfAllTransactionRequests	|
		|numberOfNewTransactions		|
		|numberOfInvalidTransactions	|
		|numberOfSentTransactions		|
		|connectionType					|
		
	
	Scenario: Log GetNeighbors
		Given a response for "getNeighbors" exists
		Then create the log directory "./tests/features/machine1/logs/get_neighbors_logs/"
		And log the neighbor response to the file "getNeighborsLog.txt"		 
		
		
