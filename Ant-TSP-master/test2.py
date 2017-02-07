#!/usr/bin/python

x = [1,2,3,4,-2,1,1,2,3,4,-2,3,5,6,7,5,4,3,-2,4,5,6,3]
o = [0]
o += [y for y in range(len(x)) if x[y] == -2]
o.append(-1)
z = []
for inx in range(len(o) - 1):
  z.append([c for c in x[o[inx]+1:o[inx + 1]]])
print(o)
print(z)
