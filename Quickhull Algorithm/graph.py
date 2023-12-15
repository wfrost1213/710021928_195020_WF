"""Module for generating random points in and plotting graphs of points"""

# importing numpy module for vector operations
import numpy as np

# importing matplotlib module for plotting graph
import matplotlib.pyplot as plt

# importing quickhull module for quickhull algorithm
from quickhull import generate_points, quickhull


def show_graph(points, hull):
    """Plot the points on graph."""

    points = np.array(points)

    # plot a scatter graph of points
    # plt.scatter(points[:, 0], points[:, 1])

    plt.scatter(points[:, 0], points[:, 1])
    plt.title("Convex Hull of a Set of Random 2 Dimensional Points")

    for p1, p2 in zip(hull, hull[1:]):

        plt.plot([p1[0], p2[0]], [p1[1], p2[1]],
                 color='red', linestyle='-', linewidth=2)

        plt.plot([hull[0][0], hull[-1][0]], [hull[0][1], hull[-1][1]],
                 color='red', linestyle='-', linewidth=2)

    plt.show()
