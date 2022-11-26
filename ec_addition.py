import numpy as np
from elliptic_curve import EllipticCurve

"""
    This script is used to add two points on an elliptic curve

    The user can input the x-coordinates of the two points. Pressing 'enter' will plot the points.
    Pressing 'p' will find solutions above the x-axis and 'n' will find solutions below the x-axis.
"""

# Parameters a and b with default values -1 and 1
a = int(input("Enter a value for a: ") or -1)
b = int(input("Enter a value for b: ") or 1)

ec = EllipticCurve(a, b)

# Plotting
import matplotlib.pyplot as plt
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)


# Function
Z = ec.f(X, Y)

p1 = None
p2 = None
temp = []

x = None
y = None
z = 1

plt_p1, plt_p2, plt_r1, plt_r2, plt_l1, plt_l2, plt_l3 = None, None, None, None, None, None, None

def on_press(event):
    global x, y, z, ec, p1, p2, temp
    global plt_p1, plt_p2, plt_r1, plt_r2, plt_l1, plt_l2, plt_l3

    # Reset the plot
    if p1 is not None and p2 is not None:
        p1 = None
        p2 = None
        x = None
        y = None
        z = 1

        plt_p1.remove()
        plt_p2.remove()
        plt_r1.remove()
        plt_r2.remove()
        plt_l1.remove()
        plt_l2.remove()
        plt_l3.remove()
    
    if event.key == 'p':
        z = 1
        print("Finding solutions above the x-axis")
    elif event.key == 'n':
        z = -1
        print("Finding solutions below the x-axis")
    # If a number is pressed, set the value of the parameter
    elif event.key.isdigit():
        x = int(event.key)
        y = ec.y(x)
        y = y*z 
        print("x = {}, y = {}".format(x, y))
    elif event.key == 'enter':
        if x is None:
            print("Please enter a value for x")
        elif y is None:
            print("Please enter a value for y")
        else:
            print("x = {}, y = {}".format(x, y))
            print("f(x,y) = {}".format(ec.f(x, y)))

            if p1 is None:
                plt_p1 = plt.scatter(x, y, color='red')
                p1 = (x, y)
            elif p2 is None:
                plt_p2 = plt.scatter(x, y, color='red')
                p2 = (x, y)

                # Draw line between the two points
                plt_l1, = plt.plot([p1[0], p2[0]], [p1[1], p2[1]], color='green', linestyle='dashed', alpha=0.5)

                # Add the two points
                r = ec.add(p1, p2)
                plt_r1 = plt.scatter(r[0], -r[1], color='blue')
                plt_r2 = plt.scatter(r[0], r[1], color='green')
                print("r = {}".format(r))

                # Add a line from p1 to -r
                plt_l2, = plt.plot([p1[0], r[0]], [p1[1], -r[1]], color='green', linestyle='dashed', alpha=0.5)

                # Add a line from -r to r
                plt_l3, = plt.plot([r[0], r[0]], [-r[1], r[1]], color='green', linestyle='dashed', alpha=0.5)

            # TODO: reshape the plot to fit the new points
            fig.canvas.draw()
    else:
        # Close the plot
        plt.close()


# Plot
fig = plt.figure()
plt.contour(X, Y, Z, [0], colors='black')
plt.grid()
plt.title("f(x,y) = y^2 - (x^3 + ax + b), a = {}, b = {}".format(a, b))
plt.xlabel("x")
plt.ylabel("y")
fig.canvas.mpl_connect('key_press_event', on_press)
plt.show()