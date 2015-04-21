import Queue

def find_path(src, dst, mesh):
	
	path = []
	srcdstPath = []
	visited = []
	adj = mesh['adj']
	boxes = mesh['boxes']
	srcFound = 0
	dstFound = 0
	sy, sx = src
	dy, dx = dst
	srcBox = None
	dstBox = None
	hasPath = 0
	
	#Identify the source and destination boxes
	for box in boxes:
		x1, x2, y1, y2 = box
		
		if sx < x2 and sy < y2 and sx > x1 and sy > y1:
			#print adj[box]
			path.append((src, dst))
			srcBox = box
			srcFound = 1
		
		if dx > x1 and dy > y1 and dx < x2 and dy < y2:
			#print dst
			path.append((src, dst))
			dstBox = box
			dstFound = 1
			
		if srcFound == 1 and dstFound == 1:
			break
			
	
	#Implement the simplest complete search algorithm you can
	
	q = Queue.Queue()
	discovered = []
	q.put(srcBox)
	discovered.append(srcBox)
	while not q.empty():
		node = q.get()
		if node == dstBox:
			hasPath = 1
			break
		for edge in adj[node]:
			if edge not in discovered:
				q.put(edge)
				discovered.append(edge)
		
	if hasPath < 1:
		print "No Path Found"
		
	
	#Modify your simple search to compute a legal list of line segments demonstrating the path
	
	#Modify your simple search to implement Dijkstra's algorithm
	
	#Modify your Dijkstra's implementation into an A* implementation
	
	#Modify your Dijkstra's (or A*) into a bidirectional Dijkstra's (or bidirectional A*)
	
	return path, visited