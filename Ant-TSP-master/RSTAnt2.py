#!/usr/bin/python

import matplotlib.pyplot as plt
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
pheramone_factor = 1.0

#Random probability of the equation being discarded
random_prob = 1

#the beow are al subject to tweaking and fixing for optimality
#Trail intensity variable - open to fiddling and testing
mew = 1.0

#Weight of the Pheramone of the agorithm
alpha = 5.0


def readFile(libfile):
  #open the supplied file
  with open(libfile) as f:
    #content variable assumes list, with each item pandtaining a line.
    content = f.readlines()
    f.close()
    return content

def makeHananGraph(content):

  #Initialize lists for the following;

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

  #print (hannan_graph) 
  #print(count_map)
  return (hannan_graph, count_map)

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

  #print(hannan_graph)
  return hannan_graph


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
for i in hannan_graph:
  print(i)
for j in count_map:
  print(j)
