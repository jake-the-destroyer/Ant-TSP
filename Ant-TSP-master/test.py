def tourLength():
    y = [ants[i:i + 2] for i in range(1, len(ants), 2)]
    unique_edges = [y[i] for i in range(len(y)) \
                if (y[i] not in y[i+1:] and \
      list(reversed(y[i])) not in y[i+1:])]
  total_length = 0
  for i in unique_edges:
    print( two_d_plane[i[0]][i[1]])
  return total_length




x = [1,2,2,2,2,2,3,3,2,3,3,2]
# ([x[i] for i in range(len(x[1:])) if x[i] not in x[i + 1:] ])
y = [x[i:i + 2] for i in range(0, len(x))]
#z = [y[i] for i in range(len(y)) if (y[i] not in y[i+1:] and list(reversed(y[i])) not in y[i+1:]) ]
#a = [blah.reverse() for blah in z]
#print(z)
#print(a)
print(y)




#a = [1,2]
#A = [[1,2],[3,4]]
#print(a in A)
