# Conway's 'random' game of life
# adapted from https://www.geeksforgeeks.org/conways-game-life-python-implementation/

import numpy as np 
import matplotlib.pyplot as plt  
import matplotlib.animation as animation 
  
# values for grid
ON = 255
OFF = 0
vals = [ON, OFF] 
  
def randomGrid(N): 
  
    """returns a grid of NxN random values"""
    outgrid = np.random.choice(vals, N*N, p=[0.001, 0.999]).reshape(N, N) 
    return outgrid
  
def update(frameNum, img, grid, N): 
    
    """updates each cell based on neighbors"""
    newGrid = grid.copy() 
    for i in range(N): 
        for j in range(N): 
  
            # compute 8-neghbor sum 
            # using toroidal boundary conditions - x and y wrap around  
            # so that the simulaton takes place on a toroidal surface. 
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] + 
                         grid[(i-1)%N, j] + grid[(i+1)%N, j] + 
                         grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] + 
                         grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])/255) 
  
            # apply markov chain transition probabilities 
            if grid[i, j]  == ON: 
                if (total >= 0) and (total <= 3):
                    newGrid[i, j] = np.random.choice(vals, 1, p=[.9,.1])
                elif (total >= 4) and (total <= 5): 
                    newGrid[i, j] = np.random.choice(vals, 1, p=[.2,.8])
                elif (total >= 6):
                    newGrid[i, j] = np.random.choice(vals, 1, p=[.1,.9])
            else: 
                if (total >= 1) and (total <= 3):
                    newGrid[i, j] = np.random.choice(vals, 1, p=[.05,.95])
                elif (total >= 4) and (total <= 5): 
                    newGrid[i, j] = np.random.choice(vals, 1, p=[.1,.90])
                elif (total >= 6):
                    newGrid[i, j] = np.random.choice(vals, 1, p=[.01,.99])
  
    # update data 
    img.set_data(newGrid) 
    grid[:] = newGrid[:] 
    return img, 
  
# main() function 
def main(): 
  
    # set grid size 
    N = 100
          
    # set animation update interval 
    updateInterval = 50
  
    # declare grid 
    grid = np.array([]) 
    grid = randomGrid(N) 
  
    # set up animation 
    fig, ax = plt.subplots() 
    img = ax.imshow(grid, interpolation='nearest') 
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ), 
                                  frames = 10, 
                                  interval=updateInterval, 
                                  save_count=50) 
  
    plt.show() 
  
# call main 
if __name__ == '__main__': 
    main() 