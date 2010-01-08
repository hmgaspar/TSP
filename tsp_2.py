#! /usr/bin/env python
import pylab
import itertools

#Simple code to find the exact solution to the travel salesman problem
# It creates random nodes
# n = number of nodes
# The problem has (n-1)! solutions


#Functions
#Create nodes
def create_N(_n,_xmax,_ymax):
	_nodes = []
	for i in range(_n):
 		_tmpx = pylab.rand()*_xmax
		_tmpy = pylab.rand()*_ymax
		_nodes.append((_tmpx, _tmpy))
	return _nodes



#Create edges for all nodes
def create_E(_nodes):
	_edges = {}
	for i in range(len(_nodes)):
  		for j in range(len(_nodes)):
   			x = _nodes[i][0] - _nodes[j][0]
    			y = _nodes[i][1] - _nodes[j][1] 
    			dist = (x**2 + y**2)**0.5
    			_edges[(i,j)] = dist
	return _edges



#Code
n = 8

#max range (x,y)
xmax = 10
ymax = 10

nodes = create_N(n,xmax,ymax)
edges = create_E(nodes)

scores = []

#Calculating the distance for all possibles paths startinh in node 0
#
for path in itertools.permutations(range(1, len(nodes))):
	path = [0] + list(path) + [0]
	distance = 0.0
 	for i in range(len(path)-1):
   		distance += edges[(path[i], path[i+1])]
#Another way, without the 'for'
#	distance = sum([ edges[(path[i], path[i+1])] for i in range(len(path)-1) ])
	scores.append((distance, path))


# Sorting the solutions from min to max distances
# scores[0] is the minimum, scores[-1] is the maximum
scores = sorted(scores, cmp=lambda x,y: cmp(x[0], y[0]))

print 'Number of nodes: ', n
print 'Minimum distance: ', scores[0][0]
print 'Path: ', scores[0][1]

#Ploting


#Ploting
pylab.xlim=(0,10)
pylab.ylim=(0,10)
pylab.plot([ nodes[i][0] for i in scores[0][1] ], [ nodes[i][1] for i in scores[0][1] ],'-o')

t = ax.text(x, y, str((x,y)), withdash=True,
	dashdirection=dd,
	dashlength=dl,
	rotation=r,
	dashrotation=dr,
	dashpush=dp,
	)


pylab.show()




