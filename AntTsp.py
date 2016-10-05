#!/usr/bin/python

from random import randint

''' 
First attempt at the ant algorithm to solve some simple TSP problems.  
Note: The TSP Matrices are fed in to this program as a full Matrix inthe form of a text file
'''

class AntTsp:

  #Initialize all class parameters

  #Number of generations which, without further optimaity will resut in termination
  # Number of Ants
  num_ants = 100

  #Number of Ants per generation for optimization
  numBestAnts = 10

  #Random Number for local trail updating
  local = 0

  #Random number for global trail updating
  globe = 0

  #Evaporation Rate.
  global evaporation_rate
  evaporation_rate = 0.5

  #Random probability of the equation being discarded
  global random_prob 
  random_prob = 1
  #the beow are al subject to tweaking and fixing for optimality
  #Trail intensity variable - open to fiddling and testing
  mew = 0.1

  #Weight of the greedy force of the agorithm
  alpha = 1

  #Weight of the pheramone of the agorithm
  beta = 0.02

  '''
  Method for finding the tour length so far of an ant
  '''
  def tourLength( ant_tour_list, city_list ):
    #List of lengths of totals of tours.
    i = len(ant_tour_list[1])
    length = []
	
    #For each ant....
    for ant in ant_tour_list:
      ant_total = 0
      #And for each city in the ant list
      current_city = ant[0]
      for city_values in ant[1:]:
        #Look up the value to travel from previous city to next city
		
        next_city = city_values
		
        distance = city_list[current_city][next_city][0]
        ant_total += distance
        current_city = next_city
        #Add on to the total time taken
		
      length.append(ant_total)
	
    #Return the list of values of total distance for each ant.
    return length

  '''
  Method for reading in a file and converting it to
  a 3d list of cities with distances and tuples
  '''  
  def readFile(libfile):

    j = 0
    with open(libfile) as f:
      content = f.readlines()
      f.close()

    split_list = []
    i=0
    for term in content:
      split_list.append(term.split( ))

    for i in range(len(split_list)):
      for j in range(len(split_list[i])):
        split_list[i][j] = (int(split_list[i][j]), 0)
    return split_list

  '''
  method to initially place ants throughout the graph cyclically 
  '''
  def placeAnts(ant_tour):

    city_index = 0
    ant_index = 0 

    for ant in range ( 0, len(ant_tour)):
      #ant_taboo_list[ant_index][city_index] = 1
      ant_tour[ant_index].append(city_index)
      city_index = (city_index + 1) % (len(full_matrix[0]))
      ant_index = ant_index + 1 
      
    return ant_tour

  '''
  Method to move an ant to the next available city, based on some 
  probabilities.
  '''
  def move(ant_tour, city_list):

    #For each ant in the list of ants
    total_ants = len(ant_tour)
    for ant_index in range(0, total_ants):
      #find a list of free cities
      free_cities = [] 
      for item in range(0, len(city_list)):
        if item not in ant_tour[ant_index]:
          free_cities.append(item)

      #free_cities = [i for i, x in enumerate(ant_taboo[ant_index]) if x == 0]  
      #use a probability to choose the next path NEED TO PROPERLY IMPLEMENT THIS
      if len(free_cities) > 0:
        '''
        Want to do this with an external function....
        '''
        #Randomly pick a totally random path...
        if randint(0, 1) <= random_prob:
          next_city_index = (randint(0,(len(free_cities) - 1)))
          next_city = free_cities[next_city_index]
        #else, use the formula
        else:
          print("hello")

        #next_city_index = (randint(0,(len(free_cities) - 1)))
        #next_city = free_cities[next_city_index]
        #next_city = self.pickNext(free_cities)

        #update both lists with the values of the new city etc.
        ant_tour[ant_index].append(next_city)
	  
    return ant_tour
	  
  '''
  Method for picking random city using formula or otherwise.
  '''
  def pickNext(free_cities):
    #Randomly pick a totally random path...
    if randint(0, 1) <= random_prob:
      next_city_index = (randint(0,(len(free_cities) - 1)))
      next_city = free_cities[next_city_index]
    #else, use the formula
    else:
      print("hello")
    return next_city

  '''
  Method for updating the trails of the ants.
  '''
  def updateTrails():
    for i in range(0, len(full_matrix)):
      for j in range(0, len(full_matrix)):
        full_matrix[i][j][1] *= evaporation_rate

    '''
    for each ant in the list of ants... 

    - find the contribution by dividing Q(normally 500) by the total tour length
    - update the trail of the whole tour performed by the ants.
    for (Ant a : ants) {
       double contribution = Q / a.tourLength();
       for (int i = 0; i < n - 1; i++) {
         trails[a.tour[i]][a.tour[i + 1]] += contribution;
       }
       trails[a.tour[n - 1]][a.tour[0]] += contribution;
     }
    '''





  #Parsed graph
  global full_matrix
  full_matrix  = readFile('somerandomstuff.txt')

  #2D List of all the ants vs visited towns, initialized with zeroos
  #ant_visited = [[0 for x in range(len(full_matrix[1]))] for y in range(num_ants )]

  #2D list of all tours performed by ants. all of which are, for now empty.
  ant_tour = [[] for y in range(num_ants )]

  ant_tour = placeAnts( ant_tour)
  for cities in range(0, len(full_matrix[0])):

    ant_tour = move(ant_tour, full_matrix)
  
  print(ant_tour)
  print(tourLength(ant_tour, full_matrix))
