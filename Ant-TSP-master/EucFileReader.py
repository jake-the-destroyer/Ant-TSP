#!/usr/bin/python

#import matplotlib.pyplot as plt
from random  import *
import math
''' 
First attempt at the ant algorithm to solve some simple TSP problems.  
Note: The TSP Matrices are fed in to this program as a full Matrix inthe form of a text file
'''

#Initialize all class parameters

#Random Number for local trail updating
local = 0

#Random number for global trail updating
globe = 0

#Evaporation Rate.
evaporation_rate = 0.5

#contribution factor
pheramone_factor = 30.0

#Random probability of the equation being discarded
random_prob = 1

#the beow are al subject to tweaking and fixing for optimality
#Trail intensity variable - open to fiddling and testing
mew = 1.0

#Weight of the greedy force of the agorithm
alpha = 5.0

#Weight of the pheramone of the agorithm
beta = 1.0

x_coords = []
y_coords = []
real_map = []
count_map = []
two_d_plane = []
necessary_points = []

ant_tour = []


def readFile(libfile):
  #open the supplied file
  with open(libfile) as f:
    #content variable assumes list, with each item pandtaining a line.
    content = f.readlines()
    f.close()
    return content

def makeHananGraph(content):

  split_list = []
  resulting_map = []

  #Make a list for each term.
  for term in content:
    split_list.append(term.split())

  #Find the x and y coordinates.
  for coordinate in split_list:
    x_coords.append(int(coordinate[1]))
    y_coords.append(int(coordinate[2]))

  #initialize a count map and real map that contains all zeros
  for x in range(max(x_coords) + 1):
    count_map.append([])
    real_map.append([])
    for y in range(max(y_coords) + 1):
      real_map[x].append(0)
      count_map[x].append((0,0))

  #for each coordinate, if there is a city, mark a 1 in the map.
  for i in range(len(x_coords)):
    real_map[ x_coords[i]][ y_coords[i]] = 1
  
  #iterate through the mapa and find all points
  for i in range(len(real_map)):
    for j in range(len(real_map[i])):
      if real_map[i][j] == 1:
        #Find new points at the intersection of horizontal and vertical lines
        #from the already existing points on the map i.e. Find Hanan Graph
        for h in range(len(real_map)):
          for k in range(len(real_map[h])):
            #At the points of intersection create the Steiner points
            if real_map[h][k] == 1:
              if real_map[i][k] != 1:
                real_map[i][k] = 2
              if real_map[h][j] != 1:
                real_map[h][j] = 2
                break

def reduceHananGraph():
  #Use the convex hull reduction algorithm to reduce the number of steiner points
  for i in range(len(real_map)):
    for j in range(len(real_map[i])):
      #If the point is a Steiner point...
      if real_map[i][j] == 2:

        left = (i - 1)
        right = (i + 1)
        up = (j - 1)
        down = (j + 1)

        foundLeft = False
        foundRight = False
        foundUp = False
        foundDown = False 
        keep = False       

        while (foundLeft == False and left >= 0):
          point = real_map[left][j]
          if point == 2:
            foundLeft = True
          elif point == 1:
            keep = True
            foundLeft = True
          else:
            left = left - 1

        if not keep:

          while (foundRight == False and right < len(real_map)):
            point = real_map[right][j]
            if point == 2:
              foundRight = True
            elif point == 1:
              keep = True
              foundRight = True
            else:
              right = right + 1
  
          if not keep:
            while (foundUp == False and up >= 0):
              point = real_map[i][up]
              if point == 2:
                foundUp = True
              elif point == 1:
                keep = True
                foundUp = True
              else:
                up = (up - 1)
    
            if not keep:
              while (foundDown == False and down < len(real_map[i])):
                point = real_map[i][down]
                if point == 2:
                  foundDown = True
                elif point == 1:
                  keep = True
                  foundDown = True
                else:
                  down = (down + 1)

        '''
        If the adjacent points to current Steiner point are ALL steiner points,
        find the points of intersection of these points on the horizontal axes.
        If these points are also steiner we may delete the original point.
        '''
        if (not keep) and (foundLeft or foundRight) and (foundUp or foundDown):           

          if (foundLeft and foundUp):
            if real_map[left][up] == 2:
              real_map[i][j] = 0
          elif (foundRight and foundUp):
            if real_map[right][up] == 2:
              real_map[i][j] = 0
          elif (foundLeft and foundDown):
            if real_map[left][down] == 2:
              real_map[i][j] = 0
          elif (foundRight and foundDown):
            if real_map[right][down] == 2:
              real_map[i][j] = 0

def graphToMatrix():

  
  #Assign each point in the graph an ordered number. This is used later.
  count = 0
  for i in range(len(real_map)):
    for j in range(len(real_map[i])):
      coord = real_map[i][j]
      if coord == 1 or coord == 2:
        count_map[i][j] = (coord,count)
        count = count +	1

  #Initialize the 2D plane
  for i in range(count):
    two_d_plane.append([])
    for j in range(count):
      two_d_plane[i].append(None)

  for i in range(len(real_map)):
    for j in range(len(real_map[i])):
      if real_map[i][j] != 0:
        if real_map[i][j] == 1:
          necessary_points.append(count_map[i][j][1])

        left = (i - 1)
        right = (i + 1)
        up = (j - 1)
        down = (j + 1)

        foundLeft = False
        foundRight = False
        foundUp = False
        foundDown = False 

        while (foundLeft == False and left >= 0):
          point = real_map[left][j]
          if point != 0:
            foundLeft = True
          else:
            left = left - 1

        while (foundRight == False and right < len(real_map)):
          point = real_map[right][j]
          if point != 0:
            foundRight = True
          else:
            right = right + 1
  
        while (foundUp == False and up >= 0):
          point = real_map[i][up]
          if point != 0:
            foundUp = True
          else:
            up = (up - 1)
    
        while (foundDown == False and down < len(real_map[i])):
          point = real_map[i][down]
          if point != 0:
            foundDown = True
          else:
            down = (down + 1)

        fromPoint = count_map[i][j][1]

        if foundLeft:
          toPoint = count_map[left][j][1]
          distance = i - left
          two_d_plane[fromPoint][toPoint] = {'length' : distance,'pheramone' : mew}
		  
        if foundRight:
          toPoint = count_map[right][j][1]
          distance = right - i
          two_d_plane[fromPoint][toPoint] = {'length' : distance,'pheramone' : mew}
		
        if foundUp:
          toPoint = count_map[i][up][1]
          distance = j - up
          two_d_plane[fromPoint][toPoint] = {'length' : distance,'pheramone' : mew}

        if foundDown:
          toPoint = count_map[i][down][1]
          distance = down - j
          two_d_plane[fromPoint][toPoint] = {'length' : distance,'pheramone' : mew}


def shortestPathByManhattan():
  shortest_distance = []
  total_points = len(two_d_plane)
  for i in range(total_points):
    shortest_distance.append([])
    for j in range(total_points):
      shortest_distance[i].append(None)
  count = 0
  for i in range(len(count_map)):
    for j in range(len(count_map[i])):
      if count_map[i][j][0] == 1 or count_map[i][j][0] == 2:
        
          count += 1
          for k in range(len(count_map)):
            for l in range(len(count_map[k])):
              if count_map[k][l][0] == 1 or count_map[k][l][0] == 2:
                shortest_distance[count_map[i][j][1]][count_map[k][l][1]] = \
                        abs(i - k) +  abs(j - l)

  return shortest_distance



'''
method to initially place ants on each necessary point in the graph. 
'''
def placeAnts():
  ant_index = 0
  for ant in range(0, len(ant_tour)):
    ant_tour[ant].append(-1)
    ant_tour[ant].append(necessary_points[ant])
  return ant_tour


'''
Method to move an ant to the next available city, based on some 
probabilities.
'''
def move():

  #Generate a list of all active ants.
  active_ants = [x for x in range(len(ant_tour)) if ant_tour[x][0] == -1]
  #Pick one of the active ants at random. 
  ant_index = active_ants[randint(0, len(active_ants)-1)]
  #find a list of free cities
  free_cities = [] 

  for city in range(len(two_d_plane[ant_tour[ant_index][-1]])):
    if two_d_plane[ant_tour[ant_index][-1]][city] != None and city not in ant_tour[ant_index]:
      free_cities.append(city)
  
  if len(free_cities) > 0:
    next_city = pickNext(free_cities, ant_index)
  else:
    next_city = deconfuse(ant_index)
  
  ant_tour[ant_index].append(next_city)

'''
Function that will deconfuse an ant (for the most part).
'''
def deconfuse(confused_ant):
  #Generate a set of all points in the confused ant's taboo.
  possible_points = list(set(ant_tour[confused_ant]))

  positions = []
  #Find the positions of the remaining active ants.
  for ant in range(len(ant_tour)):
    if ((ant != confused_ant) and (ant_tour[ant][0] != None)):
      positions.append(ant_tour[ant][-1])

  #Reduce dulpicates in the positions list.
  cleaned_positions = list(set(positions))
  
  #For each possible point, find the sum of the distance 
  #to all other points occupied by other active ants
  possible_points_distances = []
  for visited in possible_points:
    distance_sum = 0
    for ant_positions in cleaned_positions:
      distance_sum += SSSD[visited][ant_positions]
    possible_points_distances.append(distance_sum)

  #Find the index of the minimim distance, use this point as the next city on which to place an ant
  next_city = possible_points_distances.index(min(possible_points_distances))
  ant_tour[confused_ant].append(-2)
  return next_city

'''
Method for picking random city using formula or otherwise.
'''
def pickNext(free_cities, ant_index):
  #Randomly pick a totally random path...
  if randint(0, 100) <= random_prob:
    next_city_index = (randint(0, (len(free_cities) - 1)))
    next_city = free_cities[next_city_index]
    #else, use the formula

  else:
    #Initialize denominator variable
    denominator = 0.0 
    #Make a list of the probabilites to go to the next city
    prob_next = []
    #Initialize total cost of the trails
    total_cost_of_trails = 0.0
    #Initialize the trail intensity for the next trail
    total_prime_trail_intensity = 0.0
    #let the current city be last element in the list of places the ant has visited
    current_city = ant_tour[ant_index][-1]
    #Find the values for the denominator - Pheramone of all unvisited cities from current node & pheramone
    for i in free_cities:
      sigma = 0
      trail_cost = two_d_plane[current_city][i]['length']
      pheramone = two_d_plane[current_city][i]['pheramone']

      for j in compileTaboo(ant_index):
        sigma += SSSD[i][j]
      total_cost_of_trails = pow((1.0 / (trail_cost + sigma)), alpha)
      total_prime_trail_intensity = pow(pheramone, beta)

      denominator += total_cost_of_trails * total_prime_trail_intensity

    #for each free city....
    for i in free_cities:
      sigma = 0
      trail_cost = two_d_plane[current_city][i]['length']
      pheramone = two_d_plane[current_city][i]['pheramone']

      for j in compileTaboo(ant_index):
        sigma += SSSD[i][j]

      #Let the numerator be the current city to the power of alpha by the current 
      numerator = (pow(( 1.0 / (trail_cost + sigma)), alpha)) * (pow(pheramone, beta))
      prob = numerator / denominator
      #List of probabilities of travelling to the each city
      prob_next.append(prob)

    #Get the random number between 0 and the total probability
    index_number = uniform(0.0, 1.0)
      
    #Initialize the current index i.e the lower bound of the probability of choosing the given city
    current_index = 0.0

    #iterate through the list of probabilities...
    for j in range(0, len(prob_next)):
      #upper bound for P(choosing a path)
      next_index = prob_next[j] + current_index

      if current_index <= index_number and index_number <= next_index:
        next_city = free_cities[j]
      current_index = next_index

  return next_city

'''
Method for generating the set of taboo point of all ants excluding the 'excluded ants', taboo.
'''
def compileTaboo(excluded_ant):
  fresh_travels = []
  for ant in ant_tour:
    if not ant == ant_tour[excluded_ant]:
      for place in ant[1:]:
        fresh_travels.append(place)
  return list(set(fresh_travels))
      

'''
Method for one ant consiming another.
'''
def gobble():
  finished = False
  active_ants = 0
  for current_ant in range(len(ant_tour) - 1):
    if ant_tour[current_ant][0] == -1:  
      active_ants += 1

      for next_ant in range(current_ant + 1, len(ant_tour)):
        if ant_tour[next_ant][0] == -1:
          cacc = ant_tour[current_ant][-1]
          nacc = ant_tour[next_ant][-1]
          if (cacc == nacc):
              ant_tour[current_ant] = ant_tour[current_ant] + ant_tour[next_ant][1:-1]
              ant_tour[next_ant][0] = None

  if active_ants == 1:
    finished = True

  return finished


'''
Method for updating the trails of the ants.
'''
def updateTrails():
  for i in range(0, len(two_d_plane)):
    for j in range(0, len(two_d_plane)):
      two_d_plane[i][j]['pheramone'] *= evaporation_rate

  quality = []

  for distance in tourLength():
    quality.append(distance)
  #print(quality)
  best_ants = (sorted(range(len(quality)), key=lambda i: quality[i], reverse=True)[:10])
  #print(len(best_ants))
  #print(best_ants)
  for index in best_ants:
    current_city = 0
    for cities in ant_tour[index][1:]:
      update_value = float(quality[index]) / pheramone_factor
      two_d_plane[current_city][cities]['pheramone'] += update_value
      two_d_plane[cities][current_city]['pheramone'] += update_value
      current_city = cities
  #print(two_d_plane[0][0]['pheramone'])


'''
Method for finding the tour length so far of an ant
GIVE THIS A PARAMETER OF ANT INDEX
'''
def tourLength():
  for ants in ant_tour:
    if (ants[0] == -1):
      split_index = [0]
      split_index += [y for y in range(len(ants)) if ants[y] == -2]
      split_index.append(-1)
      z = []
      for inx in range(len(split_index) - 1):
        z.append([c for c in ants[split_index[inx]+1:split_index[inx + 1]]])
      z[-1].append(ants[-1])
      p = []
      for list_item in z:
        if(len(list_item) > 1):
          y = [list_item[i:i+2] for i in range(0, len(list_item))]
          p = p + y
          unique_edges = [p[i] for i in range(len(p)) \
            if (p[i] not in p[i+1:] and \
                list(reversed(p[i])) not in p[i+1:] and \
                len(p[i]) > 1)]

  total_length = 0
  for i in unique_edges:
    print( two_d_plane[i[0]][i[1]])
  return total_length


content = readFile("eil15.tsp")
makeHananGraph(content)
reduceHananGraph()
graphToMatrix()
SSSD = shortestPathByManhattan()

for i in range(1000):
  found = False
  ant_tour = [[] for y in range(len(necessary_points))]
  ant_tour = placeAnts()
  lengths_of_shortest_paths = []
  while not found:
    move()
    found = gobble()
  lengths_of_shortest_paths.append(tourLength())

print(min(lengths_of_shortest_paths))
for p in count_map:
  print(p)
