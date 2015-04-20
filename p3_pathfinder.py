

def find_path(src, dst, mesh):
	
	path = []
	visited = []
	adj = mesh['adj']
	boxes = mesh['boxes']
	srcFound = 0
	dstFound = 0
	sy, sx = src
	dy, dx = dst
	
	for box in boxes:
		x1, x2, y1, y2 = box
		
		if sx < x2 and sy < y2 and sx > x1 and sy > y1:
			#print src
			path.append((src,dst))
			srcFound = 1
		
		if dx > x1 and dy > y1 and dx < x2 and dy < y2:
			#print dst
			path.append((src,dst))
			dstFound = 1
			
		if srcFound == 1 and dstFound == 1:
			break
		
		
		
			
	print path
	
	return path, visited