#!/usr/bin/python

#import matplotlib.pyplot as plt
from random  import *
import math

'''
Method for picking random city using formula or otherwise.
'''
def readFile(libfile):
  #open the supplied file
  with open(libfile) as f:
    #content variable assumes list, with each item pandtaining a line.
    content = f.readlines()
    f.close()
    return content

'''
Method for picking random city using formula or otherwise.
'''
def makeHananGraph(content):

  #List of coordinates in order divided into (index,xcoord,ycoord)
  split_list = []
  x_coords = []
  y_coords = []

  #Hannan graph
  hannan_graph = []
  count_map = []

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
    hannan_graph.append([])
    for y in range(max(y_coords) + 1):
      hannan_graph[x].append(0)
      count_map[x].append((0,0))

  #for each coordinate, if there is a city, mark a 1 in the map.
  for i in range(len(x_coords)):
    hannan_graph[ x_coords[i]][ y_coords[i]] = 1

  #iterate through the mapa and find all points
  for i in range(len(hannan_graph)):
    for j in range(len(hannan_graph[i])):
      if hannan_graph[i][j] == 1:
        #Find new points at the intersection of horizontal and vertical lines
        #from the already existing points on the map i.e. Find Hanan Graph
        for h in range(len(hannan_graph)):
          for k in range(len(hannan_graph[h])):
            #At the points of intersection create the Steiner points
            if hannan_graph[h][k] == 1:
              if hannan_graph[i][k] != 1:
                hannan_graph[i][k] = 2
              if hannan_graph[h][j] != 1:
                hannan_graph[h][j] = 2
                break

  return (hannan_graph, count_map)

'''
Method for picking random city using formula or otherwise.
'''
def reduceHananGraph(hannan_graph):
  #Use the convex hull reduction algorithm to reduce the number of steiner points
  for i in range(len(hannan_graph)):
    for j in range(len(hannan_graph[i])):
      #If the point is a Steiner point...
      if hannan_graph[i][j] == 2:

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
          point = hannan_graph[left][j]
          if point == 2:
            foundLeft = True
          elif point == 1:
            keep = True
            foundLeft = True
          else:
            left = left - 1

        if not keep:

          while (foundRight == False and right < len(hannan_graph)):
            point = hannan_graph[right][j]
            if point == 2:
              foundRight = True
            elif point == 1:
              keep = True
              foundRight = True
            else:
              right = right + 1

          if not keep:
            while (foundUp == False and up >= 0):
              point = hannan_graph[i][up]
              if point == 2:
                foundUp = True
              elif point == 1:
                keep = True
                foundUp = True
              else:
                up = (up - 1)

            if not keep:
              while (foundDown == False and down < len(hannan_graph[i])):
                point = hannan_graph[i][down]
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
            if hannan_graph[left][up] == 2:
              hannan_graph[i][j] = 0
          elif (foundRight and foundUp):
            if hannan_graph[right][up] == 2:
              hannan_graph[i][j] = 0
          elif (foundLeft and foundDown):
            if hannan_graph[left][down] == 2:
              hannan_graph[i][j] = 0
          elif (foundRight and foundDown):
            if hannan_graph[right][down] == 2:
              hannan_graph[i][j] = 0

  return hannan_graph

'''
Method for picking random city using formula or otherwise.
'''
def graphToMatrix(hannan_graph, count_map):

  two_d_plane = []
  necessary_points = []
  x1_coords = []
  y1_coords = []
  x2_coords = []
  y2_coords = []
  node_degree = []

  #Assign each point in the graph an ordered number. This is used later.
  count = 0
  for i in range(len(hannan_graph)):
    for j in range(len(hannan_graph[i])):
      coord = hannan_graph[i][j]
      if coord == 1: 
        x1_coords.append(i)
        y1_coords.append(j)
        count_map[i][j] = (coord,count)
        necessary_points.append(count_map[i][j][1])
        count = count +  1
      elif coord == 2:
        x2_coords.append(i)
        y2_coords.append(j)
        count_map[i][j] = (coord,count)
        count = count +  1

  #Initialize the 2D plane
  for i in range(count):
    node_degree.append(0)
    two_d_plane.append([])
    for j in range(count):
      two_d_plane[i].append(None)

  for i in range(len(hannan_graph)):
    for j in range(len(hannan_graph[i])):
      if hannan_graph[i][j] != 0:

        left = (i - 1)
        right = (i + 1)
        up = (j - 1)
        down = (j + 1)

        foundLeft = False
        foundRight = False
        foundUp = False
        foundDown = False 
        while (foundLeft == False and left >= 0):
          point = hannan_graph[left][j]
          if point != 0:
            foundLeft = True
          else:
            left = left - 1

        while (foundRight == False and right < len(hannan_graph)):
          point = hannan_graph[right][j]
          if point != 0:
            foundRight = True
          else:
            right = right + 1
  
        while (foundUp == False and up >= 0):
          point = hannan_graph[i][up]
          if point != 0:
            foundUp = True
          else:
            up = (up - 1)
    
        while (foundDown == False and down < len(hannan_graph[i])):
          point = hannan_graph[i][down]
          if point != 0:
            foundDown = True
          else:
            down = (down + 1)

        fromPoint = count_map[i][j][1]

        if foundLeft:
          toPoint = count_map[left][j][1]
          distance = i - left
          two_d_plane[fromPoint][toPoint] = {'length' : distance,'pheramone' : mew}
          node_degree[fromPoint] += 1

        if foundRight:
          toPoint = count_map[right][j][1]
          distance = right - i
          two_d_plane[fromPoint][toPoint] = {'length' : distance,'pheramone' : mew}
          node_degree[fromPoint] += 1

        if foundUp:
          toPoint = count_map[i][up][1]
          distance = j - up
          two_d_plane[fromPoint][toPoint] = {'length' : distance,'pheramone' : mew}
          node_degree[fromPoint] += 1

        if foundDown:
          toPoint = count_map[i][down][1]
          distance = down - j
          two_d_plane[fromPoint][toPoint] = {'length' : distance,'pheramone' : mew}
          node_degree[fromPoint] += 1

  return (count_map, two_d_plane, necessary_points, node_degree, x1_coords, x2_coords, y1_coords, y2_coords)
  

'''
Method for creating the node's pheramone table.
'''
def createPheramoneTable(two_d_plane, node_degree):
  length = len(two_d_plane)
  node_table = []
  #for each node, create a 2d table
  for node in range(length):
    node_table.append([])

    #create a row for all possible destinations.
    for destination in range(length):
      node_table[node].append([])
      
      #Append n probabilities, where n is a neighbor of a given node.
      for neighbor in range(length):
        if two_d_plane[node][neighbor] != None:
          prob = round((1.0/node_degree[node]), 2)
          node_table[node][destination].append(
                 {'neighbor' : neighbor, 'probability' : prob})
        
  return node_table

'''
Method for calculating the probabilities for the pheramone tables. 
'''
def updatePherTable(node, destination):

  prob = round((1.0/node_degree[node]), 2)
 

  #Initialize denominator variable
  denominator = 0.000001 
  #Make a list of the probabilites to go to the next city
  prob_next = []
  #Initialize total cost of the trails
  total_cost_of_trails = 0.0
  #Initialize the trail intensity for the next trail
  total_prime_trail_intensity = 0.0
  #Find the values for the denominator - Pheramone of all unvisited cities from current node & pheramone
  for i in pheramone_table[node][destination]:
    neighbor = i['neighbor']
    from_point = min(node, neighbor)
    to_point = max(node, neighbor)
    
    trail_cost = two_d_plane[from_point ][to_point ]['length']
    pheramone = two_d_plane[from_point ][to_point ]['pheramone']

    total_cost_of_trails = pow((1.0 / (trail_cost)), alpha)
    total_prime_trail_intensity = pheramone

    denominator += total_cost_of_trails * total_prime_trail_intensity

  #for each free city....
  for i in pheramone_table[node][destination]:
    neighbor = i['neighbor']
    from_point = min(node, neighbor)
    to_point = max(node, neighbor)
    
    trail_cost = two_d_plane[from_point][to_point]['length']
    pheramone = two_d_plane[from_point][to_point]['pheramone']

    #Let the numerator be the current city to the power of alpha by the current 
    numerator = (pow(( 1.0 / (trail_cost)), alpha)) * (pheramone)
    prob = numerator / denominator
    i['probability'] = round(prob, 2)


'''
Method for placing an ant on a source node. 
'''
def placeAnt(source_node):
  ant = []
  ant.append(source_node)
  return ant

'''
Method to move an ant to the next available city, based on some 
probabilities.
'''
def move(ant, destination):

  #mark the current node.
  current_node = ant[-1]
  next_nodes = []

  #Create a list of the probability of moving to any on of the 
  #neighbors of the current node for the given destination.
  for neighbor in pheramone_table[current_node][destination_node]:
    next_nodes.append(neighbor['probability'])

  neighbor = next_nodes.index(max(next_nodes))
  next_city = pheramone_table[current_node][destination_node][neighbor]['neighbor']
  if(next_city in ant):
    ant.append(next_city)
    ant_dead = True
  else:
    ant.append(next_city)
    ant_dead = False
  
  updateTrails(ant, ant_dead)
  return ant, ant_dead


'''
Method for updating the trails of the ants.
'''
def updateTrails(ant, ant_dead):
  from_point = min(ant[-2], ant[-1])
  to_point = max(ant[-2], ant[-1])

  if ant_dead:
    included_cost = 0
  else:
    included_cost = 1 / (1 + two_d_plane[from_point][to_point]['length'])

  two_d_plane[from_point][to_point]['pheramone'] = \
          ((1 - evaporation_rate) * two_d_plane[from_point][to_point]['pheramone']) + included_cost

  #print(two_d_plane[from_point][to_point])

'''
Method for updating the trails of the ants.
'''
def updateTrailsGlobal(ant, degree_satisfied):
  included_cost = 0

  if degree_satisfied:
    path_length = 0
    for vertex in range(len(ant) - 1):
      from_point = ant[vertex]
      to_point = ant[vertex + 1]
      path_length += two_d_plane[from_point][to_point]['length']
      
    included_cost = 1 / (1 + path_length)
  for vertex in range(len(ant) -1):
    from_point = min(ant[vertex], ant[vertex + 1])
    to_point = max(ant[vertex], ant[vertex + 1])
    two_d_plane[from_point][to_point]['pheramone'] = \
          ((1 - evaporation_rate) * two_d_plane[from_point][to_point]['pheramone']) + included_cost


'''
Build all of the ant trees based on the pheramone tables.
'''
def buildTree(tree, source, destination):
  current_node = source
  visited = [current_node]
  while current_node != destination:
    prev_node = current_node
    next_nodes = []
    for i in pheramone_table[current_node][destination]:
      if i['neighbor'] not in visited:
        next_nodes.append(i['probability'])  
      else:
        next_nodes.append(-1)
    neighbor = next_nodes.index(max(next_nodes))
    current_node = pheramone_table[current_node][destination_node][neighbor]['neighbor']
    #print(current_node)
    visited.append(current_node)
    tree.append((prev_node,current_node))

  return tree

#Initialize all class parameters

  #Random Number for local trail updating
local = 0

  #Random number for global trail updating
globe = 0

  #Evaporation Rate.
evaporation_rate = 0.5

  #contribution factor
pheramone_factor = 1.0

  #Random probability of the equation being discarded
random_prob = 1

  #Trail intensity variable - open to fiddling and testing
mew = 1.0

  #Weight of the Pheramone of the agorithm
alpha = 5.0

content = readFile("eil15.tsp")

hannan_graph, count_map = makeHananGraph(content)

hannan_graph = reduceHananGraph(hannan_graph)

count_map, two_d_plane, necessary_points, node_degree, x1_coords, x2_coords, y1_coords, y2_coords  \
                     = graphToMatrix(hannan_graph, count_map)

pheramone_table = createPheramoneTable(two_d_plane, node_degree)
'''
Test for the creation of the pheramone table.

#for node in pheramone_table:
#  for destination in node:
#    for neighbor in destination:
#      print(neighbor)
'''

source_node = necessary_points[randint(0, len(necessary_points)-1)]
necessary_points.remove(source_node)
tree = []
while len(necessary_points) > 0:
  destination_node = necessary_points[randint(0, len(necessary_points)-1)]
  necessary_points.remove(destination_node)
  full_paths = []
  for i in range(100):
    ant = placeAnt(source_node)
  
  
    '''
    Test to check whether the ant is placed correctly.
    
    print(source_node)
    print(destination_node)
    print(ant)
    '''
  
  
    ant_dead = False
    at_destination = False
    while (not ant_dead) and (not at_destination):
      at_destination = ant[-1] == destination_node
      if( not at_destination):
        ant, ant_dead = move(ant, destination_node)
  
    updateTrailsGlobal(ant, True)
    for node in ant:
      updatePherTable(node, destination_node)
    if at_destination:
      full_paths.append(ant)
  #print(source_node)
  #print(destination_node)
  #for i in full_paths:
    #print(i)
      #print(source_node)
     # print(destination_node)
     # print(ant_tour[-1])
     # print(ant_dead)
     # print("----------------------------")
  #print(necessary_points)
  
  tree = buildTree(tree, source_node, destination_node)
  print(tree)
#plt.scatter(x1_coords, y1_coords, c='b')
#plt.scatter(x2_coords, y2_coords, c='r')


from_path_point = []
to_path_point = []
hi = 0
for i in tree:
  print(i)
  found_x = False
  found_y = False
  for j in range(len(count_map)):
    limit = len(count_map[j])
    k = 0
    while k < (limit):
      if count_map[j][k][1] == i[1] and not found_x:
        from_path_point.append([j, k])
        found_x = True

      if count_map[j][k][1] == i[0] and not found_y:
        to_path_point.append([j, k])
        found_y = True
      k += 1


#for point in range(len(from_path_point)):
#  plt.plot([from_path_point[point][0], to_path_point[point][0]], \
#           [from_path_point[point][1], to_path_point[point][1]])

#plt.show()
