__author__ = 'Joao'

import math

class Point2D(object):
    def __init__(self, x, y):
        """Defines x and y axis"""
        self.X = x
        self.Y = y

    def move(self, dx, dy):
        """Returns the point resulted of the translation"""
        newX = self.X + dx
        newY = self.Y + dy
        return Point2D(x = newX,y = newY)

    def __str__(self):
        return "Point(%s,%s)"%(self.X, self.Y)

    def distance(self, other):
        dx = self.X - other.X
        dy = self.Y - other.Y
        return math.sqrt(dx**2 + dy**2)

    def linear_interpolation(self,other,t):
        """
        Calculates the linear interpolation betwix this point and other
        @param other: Second point. a.linearInterpolation(b,0.5) == b.linearInterpolation(a,0.5)
        @param t: parameter used on the linear interpolation
        @return: The point resulted of the linear interpolation
        @rtype : Point2D
        """
        return Point2D(x = (1-t)*self.X + t*other.X,y = (1-t)*self.Y + t*other.Y)
        pass

class ControlPoints(object):
    def __init__(self, control_points_list):
        """
        Holds a list of points as control points

        @param control_points_list: List of control points  of the Bezier Curve to be generated
        @type control_points_list: object
        """
        assert isinstance(control_points_list, [])
        self.control_points_list = control_points_list
        self.numberOfControlPoints = len(self.control_points_list)
        pass

    def linear_interpolation(self,point1,point2,t):

        """
        Calculates the linear interpolation of controls points

        @param point1: Number of the first point; starting by 0
        @param point2: Number of the second point; starting by 0
        @param t: Parameter used on the linear interpolation
        @return: The point resulted of the linear interpolation
        @rtype : Point2D
        """
        return self.control_points_list[point1].linearInterpolation(self.control_points_list[point2],t)
