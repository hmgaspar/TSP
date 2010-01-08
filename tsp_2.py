#! /usr/bin/env python
import pylab
import itertools

#Functions

#Create nodes
def create_N(_n,_xmax,_ymax):
	_nodes = []
	for i in range(_n):
 		_tmpx = pylab.rand()*_xmax
		_tmpy = pylab.rand()*_ymax
		_nodes.append((_tmpx, _tmpy))
	return _nodes



#Create edges
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
xmax = 10
ymax = 10

nodes = create_N(n,xmax,ymax)
edges = create_E(nodes)

scores = []

for path in itertools.permutations(range(1, len(nodes))):
	path = [0] + list(path) + [0]
#	distance = 0.0
 # 	for i in range(len(path)-1):
#   		distance += edges[(path[i], path[i+1])]
	distance = sum([ edges[(path[i], path[i+1])] for i in range(len(path)-1) ])
	scores.append((distance, path))



scores = sorted(scores, cmp=lambda x,y: cmp(x[0], y[0]))
print scores[0][1][0]

#Ploting
#plot (nodes,'o')

#show()


print len(edges)
print 'score 0 - ', scores[0]
print 'nodes'
print nodes
print ''
print 'edges'
print edges


#Ploting
pylab.plot([ nodes[i][0] for i in scores[0][1] ], [ nodes[i][1] for i in scores[0][1] ],'-o')

pylab.xlim=(0,10)
pylab.ylim=(0,10)

pylab.show()




