#!/usr/bin/python

x = [-1,2,3,4,-2,1,1,2,3,4,-2,3,-2,6,7,5,4,3,-2,4,5,6,3,-2,54,-2]
o = [0]
o += [y for y in range(len(x)) if x[y] == -2]
o.append(-1)
z = []
for inx in range(len(o) - 1):
  z.append([c for c in x[o[inx]+1:o[inx + 1]]])
z[-1].append(x[-1])
print(z)

p = []
for list_item in z:
  if(len(list_item)) > 1:
    print(list_item)
    y = [list_item[i:i + 2] for i in range(0, len(list_item))]
    p = p + y
print(p)
unique_edges = [p[i] for i in range(len(p)) \
            if (p[i] not in p[i+1:] and \
  list(reversed(p[i])) not in p[i+1:] and \
            len(p[i]) > 1)]
print(unique_edges)

# ([x[i] for i in range(len(x[1:])) if x[i] not in x[i + 1:] ])
#y = [x[i:i + 2] for i in range(0, len(x))]

'''

if (ants[0] == -1):
  split_index = [0]
  split_index += [y for y in range(len(ants)) if ants[y] == -2]
  split_index.append(-1)
  z = []
  for inx in range(len(split_index) - 1):
    z.append([c for c in ants[split_index[inx]+1:split_index[inx + 1]]])
    z[-1].append(ants[-1])
    print(ants)
    print("---------------------------------------------")
    print(z)
    y = [ants[i:i + 2] for i in range(1, len(ants))]
    unique_edges = [y[i] for i in range(len(y)) \
                if (y[i] not in y[i+1:] and \
                list(reversed(y[i])) not in y[i+1:])] 
  print(unique_edges)
  total_length = 0
  #for i in unique_edges:
    #print( two_d_plane[i[0]][i[1]])
  return total_length
'''  
