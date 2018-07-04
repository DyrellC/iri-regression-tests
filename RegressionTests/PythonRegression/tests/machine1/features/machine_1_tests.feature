@machine1
Feature: Test API calls on Machine 1
	Test various api calls to make sure they are responding
	correctly 
	
	Scenario: Configure machine 1
		Given node configuration "./tests/machine1/config.yml" 
		Then set up global environment
	
	Scenario: GetNodeInfo is called
		Given getNodeInfo is called on Node "nodeA" 
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
		
	
	Scenario: GetNeighbors is called
		Given getNeighbors is called on Node "nodeA"
		Then a response with the following is returned:
		|keys							|
		|address						|
		|numberOfAllTransactions		|
		|numberOfAllTransactionRequests	|
		|numberOfNewTransactions		|
		|numberOfInvalidTransactions	|
		|numberOfSentTransactions		|
		|connectionType					|
		
