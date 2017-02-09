#!/usr/bin/python

x = [1,2,3,4,-2,1,1,2,3,4,-2,3,-2,6,7,5,4,3,-2,4,5,6,3]
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
  if(len(list_item)) > 2:
    y = [list_item[i:i + 2] for i in range(1, len(list_item))]
    p.append(y)    
unique_edges = [p[i] for i in range(len(p)) \
            if (p[i] not in p[i+1:] and \
  list(reversed(p[i])) not in p[i+1:])]


# ([x[i] for i in range(len(x[1:])) if x[i] not in x[i + 1:] ])
#y = [x[i:i + 2] for i in range(0, len(x))]
print(y)

