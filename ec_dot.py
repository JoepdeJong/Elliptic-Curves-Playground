# Visualize the dot operation on an elliptic curve

# In[1]:
a = int(input("Enter a value for a: (default -1) ") or -1)
b = int(input("Enter a value for b: (default 1) ") or 1)
prime = int(input("Enter a prime number p: (default 17) ") or 17)


x_p = int(input("Enter the x-coordinate of the first point: "))
x_q = int(input("Enter the x-coordinate of the second point: "))

# In[2]:
from elliptic_curve import EllipticCurve

ec = EllipticCurve(a, b, prime)

# In[3]:
y_p = ec.y(x_p)
y_q = ec.y(x_q)

p = (x_p, y_p)
q = (x_q, y_q)
y_max = ec.y(prime)

# In[4]: Make a grid of points to plot the curve
import numpy as np

x = np.linspace(-10, prime, 100)
y = np.linspace(-y_max, y_max, 300)
X, Y = np.meshgrid(x, y)
Z = ec.f(X, Y)

# In[5]:

from matplotlib import pyplot as plt

fig, ax = plt.subplots()
plt.contour(X, Y, Z, [0], colors='black')
plt.grid()
plt.title("f(x,y) = y^2 - (x^3 + ax + b), a = {}, b = {}".format(a, b))
plt.xlabel("x")
plt.ylabel("y")

# Plot the first point
plt.scatter(p[0], p[1], color='red')

# Plot the second point
plt.scatter(q[0], q[1], color='blue')

# Draw a line from p to q
line_q0q, = ax.plot([p[0], q[0]], [p[1], q[1]], color='gray', linestyle='dashed', alpha=0.5, linewidth=0.5)
line_qq = None

plt.draw()
# In[6]:
def on_press(event):
    global p, q, ec

    if event.key == 'escape':
        plt.close()

    # Save the current point
    q0 = q

    # Calculate the new point from the current point and the point p
    q = ec.dot(p, q, 1)


    # Clear the previous lines
    global line_q0q, line_qq
    # try: 
    #     # line_pq.remove()
    #     line_q0q.remove()
    #     line_qq.remove()
    # except:
    #     pass

    # Draw a line from q0 to -q
    # line_pq = plt.plot([p[0], q[0]], [p[1], -q[1]], color='green', linestyle='dashed', alpha=0.5)

    # Draw a line from q0 to -q
    line_q0q, = ax.plot([q0[0], q[0]], [q0[1], -q[1]], color='gray', linestyle='dashed', alpha=0.5, linewidth=0.5)

    # Draw a line from -q to q
    line_qq, = ax.plot([q[0], q[0]], [-q[1], q[1]], color='gray', linestyle='dashed', alpha=0.5, linewidth=0.5)

    # Draw the new point
    if q == p:
        plt.scatter(q[0], q[1], color='green')
    else:
        plt.scatter(q[0], q[1], color='blue')

    plt.draw()


# In[7]:
fig.canvas.mpl_connect('key_press_event', on_press)
plt.show()

