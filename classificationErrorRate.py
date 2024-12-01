'''
Python script to simulate the calculation error rate usage with the the cost function to minimise to simulate the drawing of the best fit line/devision for a decision tree.
'''

#Import C library modules for calculation
import random
import numpy as np
import matplotlib.pyplot as plt

def costFunction():
    pass
    

def calculateErrorRate(pointsArray):
    proportionOfPoints = []
    for x in range(0, 4):
        xLine = x + 0.5
        # Initialize the count of points in the current grid cell
        count = [0, 0]

        #Loop through each point
        for point in points:
            if point[0] < xLine and point[1] < yLine:
                if point[2] == 1:
                    count[0] += 1
                else:
                    count[1] += 1

        # Calculate the proportion of points in the current grid cell
        if sum(count) > 0:
            proportion = max(count) / sum(count)
        else:
            proportion = 0

    1 - np.norm(proportionOfPoints)


def generateDataPlot(gridSize):

    # Set the seed for reproducibility
    np.random.seed(0)

    # Define the number of points for each class
    num_points = 12

    # Generate random points for class 1
    class1_x = np.array([0.5,1.5,0.5])
    class1_y = np.array([3.5,3.5,2.5])

    # Generate random points for class 2
    
    class2_x = np.array([2.5,3.5,2.5,3.5,1.5,2.5,3.5,0.5,1.5,3.5])
    class2_y = np.array([3.5,3.5,2.5,2.5,1.5,1.5,1.5,0.5,0.5,0.5])

   # Create a scatter plot
    plt.scatter(class1_x, class1_y, label='Class 1', color='blue',s = 200)
    plt.scatter(class2_x, class2_y, label='Class 2', color='red', s = 200)
    plt.axis([0, 4, 0, 4])
    
    # Set the title andar labels
    plt.title('Random Points')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')

    # Show the legend and plot
    plt.legend()
    plt.show()

    #Combine the points into a single array with labels
    pointsArray = np.array(list(zip(class1_x, class1_y, np.ones(len(class1_x)))))  
    # Class 1 points
    pointsArray = np.vstack((pointsArray, np.array(list(zip(class2_x, class2_y, np.zeros(len(class2_x))))))  
    # Class 2 points

    return pointsArray

#Main start function
def main():
    gridSize = input('Enter grid size to calculate: ')
    print(str(gridSize))
    array = generateDataPlot(int(gridSize))
    print(array[0]) 
    calculateErrorRate()

#Call main
main()


