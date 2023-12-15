"""Module providing the quickhull algorithm for constructing convex hulls."""

# importing numpy module for vector operations
import numpy as np

# convex hull empty list of points
hull = []


def generate_points(high, low, num_points):
    """Generate random points.

    Parameters
    - high float : the highest value for a point
    - low float : the lowest value for a point
    - num_points int : the number of points to generate

    Returns
    - points [[float, float]] : a nested list of points in 2D space
    """

    # return a numpy array of random points in n dimensions.
    points = np.random.rand(num_points, 2) * (high - low) + low
    return points.tolist()


def get_max_and_min(points):
    """Function for finding the lowest and highest point along the x-axis.

    Parameters
    - points [[float, float]] : a nested list of points in 2D space

    Returns
    - s[0] [float, float] : the lowest point along the x-axis
    - s[-1] [float, float] : the highest point along the x-axis
    """

    # sort the points by x-axis value
    s = sorted(points, key=lambda x: x[0])

    # add the lowest and highest points (by x-value) to the convex hull
    hull.append(s[0])
    hull.append(s[-1])

    return s[0], s[-1]


def split_points(p1, p2, points):
    """Function to split points into two sides of a line.

    Parameters
    - p1 [float, float] : a point in 2D space
    - p2 [float, float] : a point in 2D space
    - points [[float, float]] : a nested list of points in 2D space to be
      divided into two sides of line p1 -> p2

    Returns
    - side1 [[float, float]] : list of points one side of line p1 -> p2
    - side2 [[float, float]]: list of points other side of line p1 -> p2
    """

    # initialising to hold points on either side of the line
    side1 = []
    side2 = []

    # iterate through points
    for p in points:

        # calculate the determinant
        d = (p[0] - p1[0]) * (p2[1] - p1[1]) - \
            (p[1] - p1[1]) * (p2[0] - p1[0])

        # if determinant is positive, point is on side 1
        if d >= 0:
            side1.append(p)

        # if determinant is negative, point is on side 2
        else:
            side2.append(p)

    return side1, side2


def split_out(p1, p2, points):
    """Function to split points into two sides of a line.

    Parameters
    - p1 [float, float] : a point in 2D space
    - p2 [float, float] : a point in 2D space
    - points [[float, float]] : a nested list of points in 2D space to
      find points on the outside of line p1 -> p2

    Returns
    - out [[float, float]] : list of points outside of line p1 -> p2
    """

    # initialising empty list to hold points on the outside of the line
    out = []

    # iterate through points
    for p in points:

        # calculate the determinant
        d = (p[0] - p1[0]) * (p2[1] - p1[1]) - \
            (p[1] - p1[1]) * (p2[0] - p1[0])

        # if determinant is positive, point is outside the line
        if d >= 0:
            out.append(p)

    return out


def get_distance(p1, p2, p):
    """Function for finding the distance between a point and a line.

    Parameters
    - p1 [float, float] : a point in 2D space
    - p2 [float, float] : a point in 2D space
    - p [float, float] : a point in 2D space to find distance from line p1 -> p2

    Returns
    - distance float : the distance between point p and line p1 -> p2
    """

    # calculate distance of point from line
    distance = abs((p1[0] - p[0]) * (p2[1]-p1[1]) -
                   (p1[0] - p2[0]) * (p[1] - p1[1]))

    return distance


def in_triangle(p1, p2, p3, p) -> bool:
    """Function for finding if a point is in a triangle.

    Parameters
    - p1 [float, float] : a point in 2D space
    - p2 [float, float] : a point in 2D space
    - p3 [float, float] : a point in 2D space
    - p [float, float] : a point in 2D space to find if it is in triangle p1, p2, p3

    Returns
    - bool : True if point is in triangle, False otherwise
    """

    # Calculate area of triangle p1, p2, p3
    side1 = (p[0] - p2[0]) * (p1[1] - p2[1]) - \
        (p1[0] - p2[0]) * (p[1] - p2[1])
    side2 = (p[0] - p3[0]) * (p2[1] - p3[1]) - \
        (p2[0] - p3[0]) * (p[1] - p3[1])
    side3 = (p[0] - p1[0]) * (p3[1] - p1[1]) - \
        (p3[0] - p1[0]) * (p[1] - p1[1])

    # check if point is in triangle
    return (side1 < 0.0) == (side2 < 0.0) == (side3 < 0.0)


def findhull(sk, p1, p2):
    """Recursive function for finding the convex hull.

    Parameters
    - sk [[float, float]] : a nested list of points in 2D space
    - p1 [float, float] : a point in 2D space
    - p2 [float, float] : a point in 2D space

    """

    # base case for checking if there are no points on the side
    if not sk:
        return

    # initialise furthest and furthest point
    furthest = 0
    furthest_point = 0

    # iterate through points on the side
    for p in sk:

        # use get_distance method to find distance of point from line
        d = get_distance(p1, p2, p)

        # if distance is greater than furthest, update furthest and furthest point
        if d > furthest and d != 0:
            furthest = d
            furthest_point = p

    # remove furthest point from side
    sk.remove(furthest_point)

    # insert furthest point into convex hull
    hull.insert(hull.index(p2), furthest_point)

    # use split_out method to find points to the right of
    # line p1 -> furthest_point and p2 -> furthest_point
    s1 = split_out(p1, furthest_point, sk)
    s2 = split_out(furthest_point, p2, sk)

    # recursive call to findhull method
    findhull(s1, p1, furthest_point)
    findhull(s2, furthest_point, p2)


def quickhull(points: list):
    """Function fot using quickhull algorithm to find convex hull.

    Parameters
    - points [[float, float]] : a nested list of points in 2D space

    Returns
    - hull [[float, float]] : a nested list of points in 2D space that form the convex hull

    """

    # use get_max_and_min method to find the most left and right points
    min_x, max_x = get_max_and_min(points)

    # remove min and max points from points list
    points.remove(min_x)
    points.remove(max_x)

    # insert min and max points into convex hull
    side1, side2 = split_points(min_x, max_x, points)

    # call to findhull method with each side and min and max points
    findhull(side1, min_x, max_x)
    findhull(side2, max_x, min_x)

    return hull
