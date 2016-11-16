#!/usr/bin/python

x_coords = []
y_coords = []
real_map = []


def readFile(libfile):

  #open the supplied file
  with open(libfile) as f:
    #content variable assumes list, with each item portaining a line.
    content = f.readlines()
    f.close()

  split_list = []
  resulting_map = []
  #Make a list for each term.
  for term in content:
    split_list.append(term.split())

  #Find the x and y coordinates.
  for coordinate in split_list:
    x_coords.append(int(coordinate[1]))
    y_coords.append(int(coordinate[2]))
    
  #initialize a map that contains all zeros
  for x in range(max(x_coords)):
    real_map.append([])
    for y in range(max(y_coords)):
      real_map[x].append(0)

  #for each coordinate, if there is a city, mark a 1 in the map.
  for i in range(len(x_coords)):
    real_map[int(x_coords[i])][int(y_coords[i])] = 1


readFile("eil51.tsp")
#print x_coords
#print y_coords    
print real_map      
