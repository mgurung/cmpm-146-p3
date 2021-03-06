import Queue
from heapq import heappush, heappop
from math import sqrt

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
	
	for box in boxes:
		x1, x2, y1, y2 = box
		#print 'working'
		if sx < y2 and sy < x2 and sx > y1 and sy > x1:
			print 'found src'
			#path.append((src, dst))
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
	

	
	q = Queue.Queue()
	queue = []
	dist = {}
	prev = {}

	distance = 0
	dist[srcBox] = distance
	prev[srcBox] = None
	heappush(queue, [0,srcBox,dstBox])
	heappush(queue, [0,dstBox,srcBox])
	q.put(srcBox)
	visited.append(srcBox)
	
	while queue:
		_,node,goal = heappop(queue)
		
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
			x3 = x2 - x		#for Djikstra's delete the d in dx
			y3 = y2 - y		#for Djikstra's delete the d in dy
			distance = dist[node] + sqrt(x3*x3+y3*y3)
			if edge not in dist or distance < dist[edge]:
				dist[edge] = distance
				prev[edge] = node
				heuristicValue = dist[edge] + sqrt((x2 -dx)*(x2 - dx)+(y2- dy)*(y2-dy))
				#q.put(edge)
				visited.append(edge)
				heappush(queue, [distance+heuristicValue,edge])
				
		
	if node == dstBox:
		while prev[node] != None:
			path.append((detail_points[prev[node]], detail_points[node]))
			node = prev[node]
		
	if hasPath < 1:
		print "No Path Found"
	
	return path, visited