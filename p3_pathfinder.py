import Queue

def find_path(src, dst, mesh):
	
	path = []
	srcdstPath = []
	visited = []
	adj = mesh['adj']
	boxes = mesh['boxes']
	detail_points = {}
	srcFound = 0
	dstFound = 0
	sy, sx = src
	SRC = sx, sy
	dy, dx = dst
	srcBox = None
	dstBox = None
	hasPath = 0
	diffX = 0
	diffY = 0
	
	#Identify the source and destination boxes
	for box in boxes:
		x1, x2, y1, y2 = box
		
		if sx < x2 and sy < y2 and sx > x1 and sy > y1:
			#print adj[box]
			#path.append((src, dst))
			diffX = x2 - sx
			diffY = y2 - sy
			detail_points[box] = sx, sy
			srcBox = box
			srcFound = 1
		
		if dx > x1 and dy > y1 and dx < x2 and dy < y2:
			#print dst
			#path.append((src, dst))
			detail_points[box] = dx, dy
			dstBox = box
			dstFound = 1
			
		if srcFound == 1 and dstFound == 1:
			break
			
	
	#Implement the simplest complete search algorithm you can
	
	q = Queue.Queue()
	discovered = []
	q.put(srcBox)
	discovered.append(srcBox)
	prev = None
	while not q.empty():
		node = q.get()
		
		if node == dstBox:
			hasPath = 1
			break
		edges = adj[node]
		for edge in edges:
			if edge not in discovered:
				q.put(edge)
				discovered.append(edge)
				nx1, nx2, ny1, ny2 = edge
				detail_points[edge] = nx2 - diffX, ny2 - diffY
		
		if node == srcBox:
			prev = detail_points[node]
		elif prev != detail_points[node]:
			path.append((prev, detail_points[node]))
		
		prev = detail_points[node]
		
	if hasPath < 1:
		print "No Path Found"
		
	
	#Modify your simple search to compute a legal list of line segments demonstrating the path
	
	#Modify your simple search to implement Dijkstra's algorithm
	
	#Modify your Dijkstra's implementation into an A* implementation
	
	#Modify your Dijkstra's (or A*) into a bidirectional Dijkstra's (or bidirectional A*)
	
	return path, visited