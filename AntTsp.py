#!/usr/bin/python

''' 
First attempt at the ant algorithm to solve some simple TSP problems.  
Note: The TSP Matrices are fed in to this program as a full Matrix inthe form of a text file
Weights for the matrices are parsed as doubes and therefore must all be >= 0
'''

class AntTsp:

  #Method to ake ants visit a town and mark the town as being visited.
  def visit( ant, town ):
    print "hello"

  #Method for finding the tour length so far of an ant
  def tourLength( ant ):
    print "hello"
  
  def readFile(libfile):

    '''
    What I need to do;

    1 - Take in text file of a matrix. (Done)
    2 - Turn that into a list (Done)
    3 - Split the list on a space to increase the value of i (Done)
    4 - Split the list on a new line to increase the value of j (Done)
    5 - write the values individually to a 2 D array (Done)
    6 - Return the array as your graph in a matrix of vertices (Done)
    7 - Thank your grandparents for naming your uncle Bob
    '''

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
        split_list[i][j] = int(split_list[i][j])
    #print split_list
    return split_list

  def placeAnts(ant_taboo_list, ant_tour_list):
    '''
    Things I have to do 
    - Place ants on each city 
    - Update the ant_visited list with the city index of the city that the ant has been places
    - Update the ant_tour list in index position 0 with the city that the ant has been placed
    '''
    city_index = 0
    ant_index = 0 

    for ant in range ( 0, len(ant_taboo_list)):
      ant_taboo_list[ant_index][city_index] = 1
      ant_tour_list[ant_index].append(city_index)
      city_index = (city_index + 1) % (len(ant_taboo_list[0]))
      ant_index = ant_index + 1 
      
    return ant_taboo_list, ant_tour_list

  def updateTour( tour_list, city_value ):
    ''' 
    - Take in a tour list of a given ant
    - Add the city_index to the list
    - Return the newly updated list.
    '''
    tour_list.append(city_value)
    return tour_list

  def updateTaboo( visited_list, city_index ):
    ''' 
    - Take in a visited list of a given ant
    - Flip the bit of the index of the city in ant_visited list 
    - Return the newly updated list
    '''
    visited_list[city_index] = 1
    return visited_list

  

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

  #Random probability of the equation being discarded
  randomProb = 0

  #the beow are al subject to tweaking and fixing for optimality
  #Trail intensity variable - open to fiddling and testing
  mew = 0.1

  #Weight of the greedy force of the agorithm
  alpha = 1

  #Weight of the pheramone of the agorithm
  beta = 0.02

  #Parsed graph
  full_matrix = readFile('somerandomstuff.txt')

  #2D List of all the ants vs visited towns, initialized with zeroos
  ant_visited = [[0 for x in range(len(full_matrix[1]))] for y in range(num_ants )]

  #2D list of all tours performed by ants. all of which are, for now empty.
  ant_tour = [[] for y in range(num_ants )]

  ant_visited, ant_tour = placeAnts(ant_visited, ant_tour)

  print ant_visited
  print ant_tour






















