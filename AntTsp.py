#!/usr/bin/python

''' 
First attempt at the ant algorithm to solve some simple TSP problems.  
Note: The TSP Matrices are fed in to this program as a full Matrix inthe form of a text file
Weights for the matrices are parsed as doubes and therefore must all be >= 0
'''

class AntTsp:
  #Initialize all class parameters
  
  #Number of generations which, without further optimaity will resut in termination
  # Number of Ants
  numAnts = 100 

  #Number of Ants per generation for optimization
  numBestAnts = 10

  #Random Number for local trail updating
  local = 0

  #Random number for global trail updating
  globe = 0

  #Random probability of the equation being discarded
  randomProb = 0

  #the beow are al subject to tweaking and fixing for optimality
  #Trail intensity variable - open to fiddling and testing
  mew = 0.1

  #Weight of the greedy force of the agorithm
  alpha = 1

  #Weight of the pheramone of the agorithm
  beta = 0.02



  def readFile(libfile):

    '''

    What I need to do;

    1 - Take in text file of a matrix. (Done)
    2 - Turn that into a list (Done)
    3 - Split the list on a space to increase the value of i (Done)
    4 - Split the list on a new line to increase the value of j (Done)
    5 - write the values individually to a 2 D array (Done)
    6 - Return the array as your graph in a matrix of vertices (Done)
    7 - Thank your grandparents for naming your uncle Bob

    '''
    j = 0
    with open(libfile) as f:
      content = f.readlines()
      f.close()
    #print content  

    split_list = []
    i=0
    for term in content:
      split_list.append(term.split( ))

    for i in range(len(split_list)):
      for j in range(len(split_list[i])):
        split_list[i][j] = int(split_list[i][j])
    print split_list
    return split_list

  '''
    FileReader fr = new FileReader(path)
        BufferedReader buf = new BufferedReader(fr)
        String line;
        int i = 0;

        while ((line = buf.readLine()) != null) {
            String splitA[] = line.split(" ");
            LinkedList<String> split = new LinkedList<String>();
            for (String s : splitA)
                if (!s.isEmpty())
                    split.add(s);

            if (graph == null)
                graph = new double[split.size()][split.size()];
            int j = 0;

            for (String s : split)
                if (!s.isEmpty())
                    graph[i][j++] = Double.parseDouble(s) + 1;

            i++;
        }

        n = graph.length;
        m = (int) (n * numAntFactor);

        // all memory allocations done here
        trails = new double[n][n];
        probs = new double[n];
        ants = new Ant[m];
        for (int j = 0; j < m; j++)
            ants[j] = new Ant();
    }

'''

  readFile('somerandomstuff.txt')
