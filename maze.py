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

num_rows = int(input("rows")) # number of rows
num_cols = int(input("columns")) # number of columns

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

M[0,num_cols-1,2] = 1

# Generate the image for display

for row in range(0,num_rows):
    for col in range(0,num_cols):


        print(row,col,M[row,col])

        cell_data = M[row,col]
        for i in range(10*row+1,10*row+9):
            image[i,range(10*col+1,10*col+9)] = 1
            if (cell_data[0] == 1):
                image[range(10*row+1,10*row+9),10*col] = 1

            if (cell_data[1] == 1):
                image[10*row,range(10*col+1,10*col+9)] = 1

            if (cell_data[2] == 1):
                image[range(10*row+1,10*row+9),10*col+9] = 1

            if (cell_data[3] == 1):
                image[10*row+9,range(10*col+1,10*col+9)] = 1



#######################################

class Bully:

    def __init__(self,celposx,cel):
        self.celposx=num_rows-1
        self.celposy=0
        self.posx=0
        self.posy=0
        self.speed=1.5
        self.x=-1
        self.y=-1
        self.map=M
        self.stackx=[]
        self.stacky=[]

    def celmove(self):
        if(self.celposx!=0 or self.celposy!=num_cols-1):

            print("jalan")
            movee=[]

            self.stackx.append(self.celposx)
            self.stacky.append(self.celposy)

            self.map[self.celposx,self.celposy,4]=0
            if(self.map[self.celposx,self.celposy,0]==1 and self.map[self.celposx,self.celposy-1,4]==1):
                movee.append(0)
            if(self.map[self.celposx,self.celposy,1]==1 and self.map[self.celposx-1,self.celposy,4]==1):
                movee.append(1)
            if(self.map[self.celposx,self.celposy,2]==1 and self.map[self.celposx,self.celposy+1,4]==1):
                movee.append(2)
            if(self.map[self.celposx,self.celposy,3]==1 and self.map[self.celposx+1,self.celposy,4]==1):
                movee.append(3)

            if(len(movee)>0):
                rand=random.randint(0,len(movee)-1)
                move=movee[rand]

                if(move==0):
                    self.celposy-=1
                elif(move==1):
                    self.celposx-=1
                elif(move==2):
                    self.celposy+=1
                elif(move==3):
                    self.celposx+=1
            else:
                print("backtrack")
                if(len(self.stackx)>0):
                    self.stackx.pop()
                    self.stacky.pop()
                if(len(self.stackx)>0):
                    self.celposx=self.stackx.pop()
                    self.celposy=self.stacky.pop()


    def move(self):
        self.posx=self.celposy*10+random.randint(30,70)/10
        self.posy=self.celposx*10+random.randint(30,70)/10
        print("posisi: ",self.posx,self.posy)






varbully=[]


for i in range (30):
    varbully.append(Bully(random.randint(0,num_rows-3),random.randint(0,num_cols-4)))

tmax = 1000
pg=0
fig = plt.figure()

for t in range (tmax):

    fig = plt.figure()
    plt.gca().set_xlim([-10,(num_rows*10)+10])
    plt.gca().set_ylim([-10,(num_cols*10)+10])

    for i in range (0,len(varbully)):
        varbully[i].move()
        plt.scatter (varbully[i].posx,varbully[i].posy,color='blue',s=5)
        varbully[i].celmove()








    plt.title('{0:03d}'.format(pg))
    plt.imshow(image, cmap = cm.Greys_r, interpolation='none')
    filename = 'frame{0:03d}.png'.format(pg)
    pg+=1
    plt.savefig(filename, bbox_inches='tight')

    plt.close(fig)


