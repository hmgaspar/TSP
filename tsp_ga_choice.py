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
n = 50

#max range (x,y)
xmax = 10
ymax = 10

#GA Parameters
pop_size = 50
mutation_probability = 0.20
number_of_generations = 1000


#nodes = create_N(n,xmax,ymax)
# To insert manually the nodes coordinates
# Do not forget to change the correct number of nodes 'n'
# 
#nodes = [(2,1), (2,2), (2,3),(2,4), (8,9), (8,8), (8,7), (8,6)]
nodes = [(6.2155032958138721, 7.45704978130534), (9.1178789487032326, 5.4518382337065834), (7.6997546026466015, 0.36484406637831479), (3.998777160597081, 5.1895464164473744), (3.9451680356709442, 8.4853802867737738), (3.5207150472719229, 8.7271219834818403), (3.4948778660473314, 1.5762485240303514), (9.5983974843512083, 8.5839652150286909), (1.7122012901208472, 8.4570976231374591), (1.5645862363200491, 7.1004172013111155), (4.7410946052319671, 9.307789932784825), (3.660496617828084, 7.9299435925234256), (9.2928103757057166, 5.8985675114192091), (9.9554857328743669, 2.0224940214610831), (4.3436328797796984, 0.38972413566493946), (5.4430502469885447, 0.10601873234478809), (8.0061038961086037, 1.1520640133184712), (8.0462714809994189, 5.2890461652704177), (0.43476072044286052, 9.3659025378343284), (2.3389958381273934, 7.4758367982241767), (1.4859678706978829, 5.6555209962152162), (3.5787863933574462, 1.4863131595647239), (3.738583492493861, 0.4380957060587809), (0.84946619964966108, 6.8147911507406516), (3.083679960037303, 0.53512524269396122), (7.5754902491727396, 3.9083057102771868), (2.1332257473276628, 5.5931888117544553), (7.0863838385059372, 6.48443343865525), (0.73205128699262212, 1.6197109274478838), (5.9167106104859482, 0.77163260744260498), (0.12904399924628662, 9.6798317459944236), (2.6900015843198952, 6.0754926465105772), (4.7980587734475737, 7.995695565489048), (3.7509963934545834, 9.9643218317639466), (5.5210400886443676, 9.0718529443769178), (3.6177730434461042, 2.1017944664192867), (6.4585342209077208, 8.9439127259860243), (2.3197229196800273, 7.2723025671061521), (3.5135343640837169, 4.0712564701390628), (5.5022283521681672, 0.64902240617188522), (7.9540569446260303, 2.9535029912307467), (8.7444752643029826, 8.6904148015130502), (4.7534621508516608, 0.29506603174690338), (9.4983761664542445, 1.1516603673371373), (9.3959149601189633, 3.7829801667686347), (0.65129130921550038, 3.7070684128024323), (6.035871733520926, 2.6268344713333835), (3.6761040592795347, 7.6471675833368842), (2.7286269453934908, 0.72045641738983313), (8.554644330939821, 7.5338825418773929)]

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
#		u_path = raw_input(': ')
		u_path = '0 36 34 32 10 33 5 4 11 47 30 18 8 19 37 9 23 31 20 26 3 38 45 28 35 6 21 48 24 22 14 42 15 39 29 46 2 16 43 13 44 40 25 17 1 12 7 41 49 27 0'
		print u_path
		p_tmp = [int(x.strip()) for x in u_path.split(' ') if x.strip() ]
		gen_1_pvalues.append(p_tmp)
		distance = 0.0		
		for j in range(len(p_tmp)-1):
			distance += calc_dist(nodes[p_tmp[j]], nodes[p_tmp[j+1]])
		gen_1_svalues.append(distance)

		print ' '
		answer = raw_input('Do you want to suggest a new path? Y/N: ')
		if answer.lower() == 'n': break

pylab.figure(2)
pylab.xlim=(0,xmax)
pylab.ylim=(0,ymax)
x = [ nodes[i][0] for i in gen_1_pvalues[0] ]
y = [ nodes[i][1] for i in gen_1_pvalues[0] ]
pylab.title('User Path')
pylab.xlabel('Minimum total distance: ' + str("%.4f" % gen_1_svalues[0]))
pylab.plot(x , y ,'-o')	
	



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
pylab.figure(3)
pylab.xlim=(0,xmax)
pylab.ylim=(0,ymax)
x = [ nodes[i][0] for i in min_p_gen1 ]
y = [ nodes[i][1] for i in min_p_gen1 ]
pylab.plot(x , y ,'-o')


#for i in range(n):
#	t = pylab.text(x[i], y[i], 'Node ' +str(min_p_gen1[i]) + ' - ' + str(("%.2f" % x[i], "%.2f" %  y[i])))

pylab.title('Final Path')
pylab.xlabel('Minimum total distance: ' + str("%.4f" % min_s_gen1))


#Ploting data for maximum values for each generation
pylab.figure(4)
pylab.plot(range(number_of_generations),generations_s, 'ro')
pylab.xlabel('Generations')
pylab.ylabel('Minimum distance')

pylab.show()






