#! /usr/bin/env python
import pylab
import itertools
import time
import random
from multiprocessing import Process


#Simple code to find the exact solution to the travel salesman problem
# It creates random nodes
# n = number of nodes
# The problem has (n-1)! solutions


#Functions

#Factorial
def fact(x): return (1 if x==0 else x * fact(x-1))

#Create nodes
def create_N(_n,_xmax,_ymax):
	_nodes = []
	for i in range(_n):
 		_tmpx = pylab.rand()*_xmax
		_tmpy = pylab.rand()*_ymax
		_nodes.append((_tmpx, _tmpy))
	return _nodes

#Calculate distance given 2 points
def calc_dist(_n1,_n2):
	x = _n1[0] - _n2[0]
	y = _n1[1] - _n2[1] 
	dist = (x**2 + y**2)**0.5
	return dist


#Roulette Wheel
def roulette(values, fitness):
	n_rand = random.random()*fitness
	sum_fit = 0
	for i in range(len(values)):
		sum_fit += 1/values[i]
		if sum_fit >= n_rand:
			break
	return i	




# TSP with GA Code
run_t = time.time()

#numeber of nodes
n = 30

#max range (x,y)
xmax = 10
ymax = 10

#GA Parameters
pop_size = 50
mutation_probability = 0.20
number_of_generations = 500


nodes = create_N(n,xmax,ymax)

# To insert manually the nodes coordinates
# Do not forget to change the correct number of nodes 'n'
# 
#nodes = [(2,1), (2,2), (2,3),(2,4), (8,9), (8,8), (8,7), (8,6)]


#Ploting Nodes
pylab.ion()
pylab.xlim=(0,xmax)
pylab.ylim=(0,ymax)
x = [ nodes[i][0] for i in range(n) ]
y = [ nodes[i][1] for i in range(n) ]
pylab.plot(x , y ,'o')
for i in range(n):
	t = pylab.text(x[i], y[i], 'Node ' +str(i))

#Variables & Lists to be used during the code
gen_1_pvalues = []
gen_1_svalues = []
generations_p = []
generations_s = []
u_paths = []
fitness = 0


u_choice = raw_input('Do you want to suggest a path? Y/N: ')


if u_choice.lower() == 'y':
	while True:	
		print 'Enter the desired path, starting and finishing in node 0, separated by spaces'
		u_path = raw_input(': ')
		p_tmp = [int(x.strip()) for x in u_path.split(' ') if x.strip() ]
		gen_1_pvalues.append(p_tmp)
		distance = 0.0		
		for j in range(len(p_tmp)-1):
			distance += calc_dist(nodes[p_tmp[j]], nodes[p_tmp[j+1]])
		gen_1_svalues.append(distance)

		print ' '
		answer = raw_input('Do you want to suggest a new path? Y/N: ')
		if answer.lower() == 'n': break

		



#Creating first population - random path values
path_init = range(1,n)
for i in range(pop_size-len(gen_1_pvalues)):
	p_tmp = path_init
	random.shuffle(p_tmp)
	p_tmp = [0] + p_tmp + [0]
	gen_1_pvalues.append(p_tmp)

	distance = 0.0
	for j in range(len(p_tmp)-1):
		distance += calc_dist(nodes[p_tmp[j]], nodes[p_tmp[j+1]])
	gen_1_svalues.append(distance)

	#Create total fitness
	fitness += 1/distance


#Getting minimum value for initial population
min_s_gen1 = gen_1_svalues[0]
min_p_gen1 = []
min_p_gen2 = []
for i in range(pop_size):
	if gen_1_svalues[i] <= min_s_gen1:
		min_s_gen1 = gen_1_svalues[i]
		min_p_gen1 = gen_1_pvalues[i]



#Starting GA loop

for i in range(number_of_generations):
	#Reseting list for 2nd generation
	gen_2_pvalues = []
	gen_2_svalues = []
	selected = []

	#Selecting individuals to reproduce
	for j in range(pop_size):
		ind_sel = roulette(gen_1_svalues,fitness)
		selected.append(gen_1_pvalues[ind_sel][1:-1])
		
	#Crossing the selected members
	for j in range(0, pop_size, 2):
		sel_ind_A = selected[j]
		sel_ind_B = selected[j+1]
	#select path to cross over
		cut_point = random.randint(0,n-2)
		
	#Crossing
		tmp_A = sel_ind_A[cut_point]
		tmp_B = sel_ind_B[cut_point]

		ind_A = sel_ind_B.index(tmp_A)
		ind_B = sel_ind_A.index(tmp_B)
		
		sel_ind_A[cut_point] = tmp_B
		sel_ind_A[ind_B] = tmp_A

		sel_ind_B[cut_point] = tmp_A
		sel_ind_B[ind_A] = tmp_B


	#mutation A
		ran_mut = random.random()
		if ran_mut < mutation_probability:
			random.shuffle(sel_ind_A)

	#mutation B
		ran_mut = random.random()
		if ran_mut < mutation_probability:
			random.shuffle(sel_ind_B)


	#Creating Generation 2
		sel_ind_A = [0] + sel_ind_A + [0]
		gen_2_pvalues.append(sel_ind_A)
		distance = 0.0
		for k in range(len(sel_ind_A)-1):
			distance += calc_dist(nodes[sel_ind_A[k]], nodes[sel_ind_A[k+1]])
		gen_2_svalues.append(distance)

		sel_ind_B = [0] + sel_ind_B + [0]
		gen_2_pvalues.append(sel_ind_B)
		distance = 0.0
		for k in range(len(sel_ind_B)-1):
			distance += calc_dist(nodes[sel_ind_B[k]], nodes[sel_ind_B[k+1]])
		gen_2_svalues.append(distance)
		




	#Getting minimum value
	min_s_gen2 = gen_2_svalues[0]
	for j in range(pop_size):
		if gen_2_svalues[j] <= min_s_gen2:
			min_s_gen2 = gen_2_svalues[j]
			min_p_gen2 = gen_2_pvalues[j]
	
	


	#Elitism one individual
	if min_s_gen1 < min_s_gen2:
		min_s_gen2 = min_s_gen1
		min_p_gen2 = min_p_gen1
		gen_2_svalues[0] = min_s_gen1
		gen_2_pvalues[0] = min_p_gen1

	#Transform gen2 into gen1
	gen_1_pvalues = gen_2_pvalues
	gen_1_svalues = gen_2_svalues
	min_p_gen1 = min_p_gen2
	min_s_gen1 = min_s_gen2
	generations_p.append(min_p_gen2)
	generations_s.append(min_s_gen2)

	#Creating new fitness
	fitness = 0
	distance = 0.0
	for j in range(pop_size):
		for k in range(len(gen_2_pvalues[j])-1):
			distance += calc_dist(nodes[gen_2_pvalues[j][k]], nodes[gen_2_pvalues[j][k+1]])
		fitness += 1/distance


print 'Runtime: ', time.time() -run_t,'s'


print 'Number of nodes: ', n
print 'Minimum distance: ', min_s_gen1
print 'Path: ', min_p_gen1
print 'Population size: ', pop_size
print 'Number of generations: ', number_of_generations
print 'Number of possible solutions: ' + str(n-1) + '! = ' + str(fact(n-1))



#Ploting
pylab.figure(2)
pylab.xlim=(0,xmax)
pylab.ylim=(0,ymax)
x = [ nodes[i][0] for i in min_p_gen1 ]
y = [ nodes[i][1] for i in min_p_gen1 ]
pylab.plot(x , y ,'-o')


for i in range(n):
	t = pylab.text(x[i], y[i], 'Node ' +str(min_p_gen1[i]) + ' - ' + str(("%.2f" % x[i], "%.2f" %  y[i])))

pylab.title('Path: ' + str(min_p_gen1))
pylab.xlabel('Minimum total distance: ' + str("%.4f" % min_s_gen1))


#Ploting data for maximum values for each generation
pylab.figure(3)
pylab.plot(range(number_of_generations),generations_s, 'ro')
pylab.xlabel('Generations')
pylab.ylabel('Minimum distance')

pylab.show()






