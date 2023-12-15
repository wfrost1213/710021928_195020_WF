"""Module for running the quickhull algorithm and plotting the results."""

# importing quickhull module for quickhull algorithm and generating points
from quickhull import quickhull, generate_points
# importing graph module for plotting graph
from graph import show_graph

# generate random points
random_points = generate_points(high=200, low=0, num_points=20)

# run the quickhull algorithm
convex_hull = quickhull(random_points.copy())

# print the results
print(f"Convex Hull Points: {convex_hull}")

# plot the results
show_graph(random_points, convex_hull)
