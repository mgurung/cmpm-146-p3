import Queue

def find_path(src, dst, mesh):
	
	path = []
	visited = []
	adj = mesh['adj']
	boxes = mesh['boxes']
	detail_points = {}
	srcFound = 0
	dstFound = 0
	sy, sx = src
	dy, dx = dst
	srcBox = None
	dstBox = None
	hasPath = 0
	diffX = 0
	diffY = 0
	#print 'working'
	#Identify the source and destination boxes
	for box in boxes:
		x1, x2, y1, y2 = box
		#print 'working'
		if sx < y2 and sy < x2 and sx > y1 and sy > x1:
			print 'found src'
			#path.append((src, dst))
			diffX = x2 - sx
			diffY = y2 - sy
			srcBox = box
			detail_points[srcBox] = sy, sx
			srcFound = 1
			
	
	for box in boxes:
		x1, x2, y1, y2 = box
		#print 'working'
		if dx > y1 and dy > x1 and dx < y2 and dy < x2:
			print 'found dst'
			#path.append((src, dst))
			dstBox = box
			detail_points[dstBox] = (dy, dx)
			dstFound = 1
	
	#print src
	#print detail_points[srcBox]
	#Implement the simplest complete search algorithm you can
	
	q = Queue.Queue()
	#discovered = []
	q.put(srcBox)
	visited.append(srcBox)
	prev = detail_points[srcBox]
	while not q.empty():
		node = q.get()
		
		if node == dstBox:
			hasPath = 1
			path.append((prev, detail_points[dstBox]))
			break
			
		y, x = detail_points[node]
		
		edges = adj[node]
		for edge in edges:
			if edge not in visited:
				q.put(edge)
				visited.append(edge)
				nx1, nx2, ny1, ny2 = edge
				detail_points[edge] = (min(ny2-1,max(ny1,y)), min(nx2-1,max(nx1,x)))
		
		
		if prev != detail_points[srcBox]:
			path.append((prev, detail_points[node]))
			
		prev = detail_points[node]
	'''	
	prev = None
	curr = None
	for v in visited:
		if !prev:
			prev = detail_points[visited.pop()]
			curr = detail_points[visited.pop()]
		else:
			prev = curr
			curr = detail_points[visited.pop()]
		
	if hasPath < 1:
		print "No Path Found"
	'''	
	
	#Modify your simple search to compute a legal list of line segments demonstrating the path
	
	#Modify your simple search to implement Dijkstra's algorithm
	
	#Modify your Dijkstra's implementation into an A* implementation
	
	#Modify your Dijkstra's (or A*) into a bidirectional Dijkstra's (or bidirectional A*)
	
	return path, visited