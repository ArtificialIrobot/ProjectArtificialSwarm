import random
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import numpy as np
import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import random
import math
from random import shuffle, randrange
matplotlib.rcParams['xtick.direction'] = 'out'
matplotlib.rcParams['ytick.direction'] = 'out'

num_rows = 10 # number of rows
num_cols = 10 # number of columns

# The array M is going to hold the array information for each cell.
# The first four coordinates tell if walls exist on those sides
# and the fifth indicates if the cell has been visited in the search.
# M(LEFT, UP, RIGHT, DOWN, CHECK_IF_VISITED)
M = np.zeros((num_rows,num_cols,5), dtype=np.uint8)

# The array image is going to be the output image to display
image = np.zeros((num_rows*10,num_cols*10), dtype=np.uint8)

# Set starting row and column
r = 0
c = 0
history = [(r,c)] # The history is the stack of visited locations

# Trace a path though the cells of the maze and open walls along the path.
# We do this with a while loop, repeating the loop until there is no history,
# which would mean we backtracked to the initial start.
while history:
    M[r,c,4] = 1 # designate this location as visited
    # check if the adjacent cells are valid for moving to

    check = []
    if c > 0 and M[r,c-1,4] == 0:
        check.append('L')
    if r > 0 and M[r-1,c,4] == 0:
        check.append('U')
    if c < num_cols-1 and M[r,c+1,4] == 0:
        check.append('R')
    if r < num_rows-1 and M[r+1,c,4] == 0:
        check.append('D')

    if len(check): # If there is a valid cell to move to.
        # Mark the walls between cells as open if we move
        history.append([r,c])
        move_direction = random.choice(check)
        if move_direction == 'L':
            M[r,c,0] = 1
            c = c-1
            M[r,c,2] = 1
        if move_direction == 'U':
            M[r,c,1] = 1
            r = r-1
            M[r,c,3] = 1
        if move_direction == 'R':
            M[r,c,2] = 1
            c = c+1
            M[r,c,0] = 1
        if move_direction == 'D':
            M[r,c,3] = 1
            r = r+1
            M[r,c,1] = 1
    else: # If there are no valid cells to move to.
	# retrace one step back in history if no move is possible
        r,c = history.pop()


# Open the walls at the start and finish
M[9,0,0] = 1
M[0,9,2] = 1

# Generate the image for display

for row in range(0,num_rows):
    for col in range(0,num_cols):
        tes=0
        tes1=0

        print (M[row,col])

        cell_data = M[row,col]
        for i in range(10*row+1,10*row+9):
            image[i,range(10*col+1,10*col+9)] = 1
            if cell_data[0] == 1: image[range(10*row+1,10*row+9),10*col] = 1
            if cell_data[1] == 1: image[10*row,range(10*col+1,10*col+9)] = 1
            if cell_data[2] == 1: image[range(10*row+1,10*row+9),10*col+9] = 1
            if cell_data[3] == 1: image[10*row+9,range(10*col+1,10*col+9)] = 1


#######################################

class Bully:

    def __init__(self,posx,posy):
        self.celposx=0
        self.celposy=0
        self.celposx=0
        self.celposy=0
        self.posx=posx
        self.posy=posy
        self.speed=0.1
        self.x=-1
        self.y=-1
        self.cell_row = M[0]
        self.celll_col = M[1]
        self.prev_Block_Row = -1
        self.prev_Block_Col = -1

    def celmove(self):
        available = []
        if self.cell_row != self.prev_Block_Row and self.cell_row != self.prev_Block_Col:
            if(M[self.celposx,self.celposy,0]==1):
                available.append(0)
            if(M[self.celposx,self.celposy,1]==1):
                available.append(1)
            if(M[self.celposx,self.celposy,2]==1):
                available.append(2)
            if(M[self.celposx,self.celposy,3]==1):
                available.append(3)
            if len(available) > 0 :
                rand = random.randint(0,len(available)-1)
                move=rand
                while len(available) > 0:
                    available.pop()
        else :
        	self.prev_Block = self.cell_block

        if(move==0):
            self.celposx += self.speed
       	elif(move==1):
            self.celposy += self.speed
        elif(move==2):
            self.celposx += self.speed
        elif(move==3):
            self.celposy += self.speed



    def move(self):
        print (self.celposx)
        print (self.celposy)

        self.posx=self.celposx*10
        self.posy=(num_rows*num_cols)-(self.celposy*10)


    def getx(self):
        return self.posx
    def gety(self):
        return self.posy





varbully=[]


for i in range (1):
    varbully.append(Bully(random.randint(0,num_rows-1)*1.0,random.randint(num_rows*num_cols-3,num_rows*num_cols-3)*1.0))

tmax = 50

fig = plt.figure()
for t in range (tmax):
    fig = plt.figure()
    plt.gca().set_xlim([-10,(num_rows*num_cols)+10])
    plt.gca().set_ylim([-10,(num_rows*num_cols)+10])


    for i in range (len(varbully)):
        plt.scatter (varbully[i].getx(),varbully[i].gety(),color='red',s=50)
        varbully[i].celmove()
        varbully[i].move()





    plt.title('{0:03d}'.format(t))
    plt.imshow(image, cmap = cm.Greys_r, interpolation='none')
    filename = 'frame{0:03d}.png'.format(t)
    plt.savefig(filename, bbox_inches='tight')
    plt.close(fig)


