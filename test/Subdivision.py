__author__ = 'Joao'

import unittest
from Geometry.Point import Point2D
from bezierCurveAlgorithms.Subdivision import subdivide
from main.Geometry.Point import ControlPoints
from bezierCurveAlgorithms.deCasteljau import bezier_curve_generator

class Subdivision(unittest.TestCase):
    def setUp(self):
        self.point1 = Point2D(x=0, y=0)
        self.point2 = Point2D(x=15, y=85)
        self.point3 = Point2D(x=-96, y=14)

    def testMiddleSubdiv(self):
        """
        Tests the algorithm when the parameter passed is zero
        """
        point1 = Point2D(x=0, y=0)
        point2 = Point2D(x=15, y=85)
        point3 = Point2D(x=-96, y=14)
        point4 = Point2D(x=-89.6, y=784.666)

        as_control_points = ControlPoints([point1, point2, point3,point4])
        (curve1,curve2) = subdivide(as_control_points,0.5)
        middle_point = bezier_curve_generator(ControlPoints([point1, point2, point3,point4]))(0.5)

        assert curve1[0] == point1 #Starts at the first control point
		assert curve1[3] == middle_point #Ends at the middle of the curve
		assert curve2[0] == middle_point #Starts at the middle of the curve
		assert curve2[3] == point4 #Ends at the last control point


if __name__ == '__main__':
    unittest.main()
