import Queue
from heapq import heappush, heappop

def find_path(src, dst, mesh):
	
	path = []
	visited = []
	adj = mesh['adj']
	boxes = mesh['boxes']
	detail_points = {}
	sy, sx = src
	dy, dx = dst
	srcBox = None
	dstBox = None
	hasPath = 0
	
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
			detail_points[srcBox] = sx, sy
			
	
	for box in boxes:
		x1, x2, y1, y2 = box
		#print 'working'
		if dx > y1 and dy > x1 and dx < y2 and dy < x2:
			print 'found dst'
			#path.append((src, dst))
			dstBox = box
			detail_points[dstBox] = dx, dy
	

	#Implement the simplest complete search algorithm you can
	
	q = Queue.Queue()
	queue = []
	dist = {}
	prev = {}

	distance = 0
	dist[srcBox] = distance
	prev[srcBox] = None
	heappush(queue, srcBox)
	q.put(srcBox)
	visited.append(srcBox)
	
	while queue:
		node = heappop(queue)
		
		if node == dstBox:
			print 'dstBox found'
			hasPath = 1
			break
			
		x, y = detail_points[node]
		
		edges = adj[node]
		
		for edge in edges:
			nx1, nx2, ny1, ny2 = edge
			detail_points[edge] =  (min(nx2-1,max(nx1,x)), min(ny2-1,max(ny1,y)))
			x2, y2 = detail_points[edge]
			x3 = x2 - x
			y3 = y2 - y
			distance = dist[node] #+ sqrt(x3*x3+y3*y3)
			if edge not in dist or distance < dist[edge]:
				dist[edge] = distance
				prev[edge] = node
				q.put(edge)
				visited.append(edge)
				heappush(queue, edge)
				
		
	if node == dstBox:
		while node != srcBox:
			path.append((detail_points[prev[node]], detail_points[node]))
			node = prev[node]
		
		
	if hasPath < 1:
		print "No Path Found"
		
	
	#Modify your simple search to compute a legal list of line segments demonstrating the path
	
	#Modify your simple search to implement Dijkstra's algorithm
	
	#Modify your Dijkstra's implementation into an A* implementation
	
	#Modify your Dijkstra's (or A*) into a bidirectional Dijkstra's (or bidirectional A*)
	
	return path, visited