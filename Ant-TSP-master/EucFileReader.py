#!/usr/bin/python

x_coords = []
y_coords = []
real_map = []
two_d_plane = []

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
    real_map[ x_coords[i] -1 ][ y_coords[i] - 1 ] = 1

  for i in range(len(real_map)):
    for j in range(len(real_map[i])):
      if real_map[i][j] == 1:
        #Find new points
        for h in range(len(real_map)):
          for k in range(len(real_map[h])):
            if real_map[h][k] == 1:
              if real_map[i][k] != 1:
                real_map[i][k] = 2
              if real_map[h][j] != 1:
                real_map[h][j] = 2
                break

readFile("eil15.tsp")
for i in real_map:
  print(i)
