from collections import deque
# create the graph
adj_lists = []
adj_lists.append([1,4]) 		# vertex 0's neighbors
adj_lists.append([0,2,4,6])		# vertex 1's neighbors (...)
adj_lists.append([1,3,7])
adj_lists.append([2,7])
adj_lists.append([0,1,5])
adj_lists.append([4,6,8,9])
adj_lists.append([1,5,7,10])
adj_lists.append([2,3,6])
adj_lists.append([5])
adj_lists.append([5,10])
adj_lists.append([6,9,12])
adj_lists.append([10,12])
adj_lists.append([10,11,13])
adj_lists.append([12])

def depthFirstSearch(start, goal):
	closedList = []
	openList = []
	history = []
	openList.append(start)
	fromNode = start
	while not len(openList) == 0:
		active = openList.pop()
		history.append((active, fromNode))
		if active in closedList:
			continue
		if active == goal:
			return history
		for v in adj_lists[active][::-1]: # reverse the list
			if not v in closedList:
				openList.append(v)
		closedList.append(active)
		fromNode = active
	return False

def breadthFirstSearch(start, goal):
	closedList = []
	openList = deque([])
	history = []
	openList.append(start)
	fromNode = start
	while not len(openList) == 0:
		active = openList.popleft()
		history.append((active, fromNode))
		if active in closedList:
			continue
		if active == goal:
			return history
		for v in adj_lists[active][::-1]: # reverse the list
			if not v in closedList:
				openList.append(v)
		closedList.append(active)
		fromNode = active
	return False

# showdown
for k in range(0,14):
	print("From ",k)
	dfs = depthFirstSearch(k, 13)
	bfs = breadthFirstSearch(k,13)
	dfs_hist_len = len(dfs)
	bfs_hist_len = len(bfs)
	print("DFS length: ", dfs_hist_len)
	print("BFS length: ", bfs_hist_len)
	if bfs_hist_len == dfs_hist_len:
		print("Tie!")
	elif bfs_hist_len < dfs_hist_len:
		print("Winner: BFS!")
	else:
		print("Winner: DFS!")
	print()


