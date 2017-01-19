#!/usr/bin/python

x_coords = []
y_coords = []
real_map = []
two_d_plane = []

def readFile(libfile):

  #open the supplied file
  with open(libfile) as f:
    #content variable assumes list, with each item pandtaining a line.
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
  for x in range(max(x_coords) + 1):
    real_map.append([])
    for y in range(max(y_coords) + 1):
      real_map[x].append(0)

  #for each coordinate, if there is a city, mark a 1 in the map.
  for i in range(len(x_coords)):
    real_map[ x_coords[i]][ y_coords[i]] = 1

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


  for i in range(len(real_map)):
    for j in range(len(real_map[i])):
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

        while (foundRight == False and right < len(real_map)):
          point = real_map[right][j]
          if point == 2:
            foundRight = True
          elif point == 1:
            keep = True
            foundRight = True
          else:
            right = right + 1

        while (foundUp == False and up >= 0):
          point = real_map[i][up]
          if point == 2:
            foundUp = True
          elif point == 1:
            keep = True
            foundUp = True
          else:
            up = (up - 1)

        while (foundDown == False and down < len(real_map[j])):
          point = real_map[i][down]
          if point == 2:
            foundDown = True
          elif point == 1:
            keep = True
            foundDown = True
          else:
            down = (down + 1)

        if (not keep) and (foundLeft or foundRight) and (foundUp or foundDown):
          print("Delete Point %d %d" % (i, j))


'''
  for i in range(len(real_map)):
    for j in range(len(real_map[i])):
      if real_map[i][j] == 2:
'''
readFile("eil15.tsp")
for i in real_map:
  print(i)
