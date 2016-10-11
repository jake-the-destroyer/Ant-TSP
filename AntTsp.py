#!/usr/bin/python

from random  import *
import math
''' 
First attempt at the ant algorithm to solve some simple TSP problems.  
Note: The TSP Matrices are fed in to this program as a full Matrix inthe form of a text file
'''


#Initialize all class parameters

#Number of generations which, without further optimaity will resut in termination
# Number of Ants
num_ants = 100

#Number of Ants per generation for optimization
num_best_ants = 10

#Random Number for local trail updating
local = 0

#Random number for global trail updating
globe = 0

#Evaporation Rate.
evaporation_rate = 0.5

#Random probability of the equation being discarded
random_prob = 1
#the beow are al subject to tweaking and fixing for optimality
#Trail intensity variable - open to fiddling and testing
mew = 0.1

#Weight of the greedy force of the agorithm
alpha = 1

#Weight of the pheramone of the agorithm
beta = 2

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

      distance = city_list[current_city][next_city]['length']
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
      split_list[i][j] = {'length' : int(split_list[i][j]),'pheramone' : 0.5}
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
      next_city = pickNext(free_cities, ant_index)

      #update both lists with the values of the new city etc.
      ant_tour[ant_index].append(next_city)
      #next_city = free_cities[next_city_index]
 
  return ant_tour
 
'''
Method for picking random city using formula or otherwise.
'''
def pickNext(free_cities, ant_index):
  #Randomly pick a totally random path...
  if randint(0, 100) <= random_prob:
    next_city_index = (randint(0,(len(free_cities) - 1)))
    next_city = free_cities[next_city_index]
    #else, use the formula

  else:
    #Initialize denominator variable
    denominator = 0.0 

    #Make a list of the probabilites to go to the next city
    prob_next = []

    #Initialize total cost of the trails
    total_cost_of_trails = 0.0

    #Initialize the traile intensity for the next trail
    total_prime_trail_intensity = 0.0
 
    #let the current city be last element in the list of places the ant has visited
    current_city = ant_tour[ant_index][-1]
 
    for i in range(0, len(free_cities)):
      total_cost_of_trails += full_matrix[current_city][i]['length']
      total_prime_trail_intensity += full_matrix[current_city][i]['pheramone']

    denominator = pow(total_cost_of_trails, alpha) * pow(total_prime_trail_intensity, beta)

    for i in range(0, len(free_cities)):

      #Let the numerator be the current city to the power of alpha by the current 
      numerator = pow(full_matrix[current_city][i]['length'], alpha) * pow(full_matrix[current_city][i]['pheramone'], beta)

      prob = numerator / (denominator + 1)
      #List of probabilities of travelling to the each city
      prob_next.append(prob)
      actual_prob_next = []

      for i in range(0, len(prob_next)):
        actual_prob_next.append(1 / (prob_next[i] + 1))

      total_prob = sum(actual_prob_next)
      #print(total_prob)
      index_number = uniform(0.0, total_prob)
      current_index = 0.0
      for j in range(0, len(actual_prob_next)):
        next_index = actual_prob_next[j] + current_index
        if current_index <= index_number and index_number <= next_index:
          next_city = free_cities[j]
        current_index += next_index

    #print(actual_prob_next)



  return next_city

'''
Method for updating the trails of the ants.
'''
def updateTrails(ant_tour):
  for i in range(0, len(full_matrix)):
    for j in range(0, len(full_matrix)):
      full_matrix[i][j]['pheramone'] *= evaporation_rate

  quality = []

  for distance in tourLength(ant_tour, full_matrix):
    quality.append(distance)
  #print(quality)
  best_ants = (sorted(range(len(quality)), key=lambda i: quality[i], reverse=True)[:10])
  #print(len(best_ants))
  #print(best_ants)
  for index in best_ants:
    current_city = 0
    for cities in ant_tour[index][1:]:
      update_value = float(quality[index]) /500
      full_matrix[current_city][cities]['pheramone'] += update_value
      full_matrix[cities][current_city]['pheramone'] += update_value
      current_city = cities

#Parsed graph
full_matrix  = readFile('swiss42.tsp')

for i in range(0, 50):
  #2D list of all tours performed by ants. all of which are, for now empty.
  ant_tour = [[] for y in range(num_ants )]

  ant_tour = placeAnts( ant_tour)
  for cities in range(0, len(full_matrix[0])):

    ant_tour = move(ant_tour, full_matrix)

  updateTrails(ant_tour)
  print(tourLength(ant_tour, full_matrix))
