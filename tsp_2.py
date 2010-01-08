#! /usr/bin/env python
from pylab import *
import itertools

#Functions

#Create nodes
def create_N(_n,_xmax,_ymax):
	_nodes = []
	for i in range(_n):
 		_tmpx = rand()*_xmax
		_tmpy = rand()*_ymax
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
n = 3
xmax = 10
ymax = 10

nodes = create_N(n,xmax,ymax)
edges = create_E(nodes)

scores = []

for path in itertools.permutations(range(1, len(nodes))):
	path = [0] + list(path) + [0]
	distance = 0.0
  	for i in range(n-1):
   		distance += edges[(path[i], path[i+1])]
		scores.append((distance, path))


scores = sorted(scores, cmp=lambda x,y: cmp(x[0], y[0]))
print scores[0]

#Ploting
#plot(nodes)
#show()







