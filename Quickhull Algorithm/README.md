# Quickhull Algorithm to Efficiently Find the Convex Hull of a Set of Points in 2 Dimensions

## Overview

This project implements the Quickhull Algorithm, a derivative of the Quicksort Algorithm which uses the divide-and-conquer approach. This approach repeatedly partitions the search space, these partitioned groups are solved individually and reconstructed to provide a solution.

### Modules

- `quickhull` - module that provides the quickhull algorithm
- `graph.py` - module that provides tha ability to display convex hull using `matplotlib`
- `main.py` - module for running algorithm

## Installing Project

### Dependencies

- numpy 1.26.2
- python 3.11.1
- matplotlib 3.7.2

### Installation

Clone repository or download `zip` file, check python and numpy versions are compatible with project.

## Running Project

### Importing Functions \& Modules

To run Quickhull Algorithm use `main.py`.

### Generate Random Set of Points

Generate a set of random 2D points using the imported `generate_points` function, using the highest and lowest point values and desired number of points in set as parameters.

```
random_points = generate_points(high=200, low=0, num_points=20)
```

### Run Algorithm

Run algorithm in `main.py`, using the previously generated points as input. Use quickhull returned value as parameter for `show_graph` function.

```
convex_hull = quickhull(random_points.copy())
print(f"Convexhull Points: {convex_hull}")
show_graph(random_points, convex_hull)
```

View algorithm output in terminal, output contains list of points in convex hull, graph will display in external matplotlib window.
