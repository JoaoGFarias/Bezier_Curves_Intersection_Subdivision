__author__ = 'Joao'

import unittest
from random import randint
from main.bezierCurveAlgorithms.deCasteljau import bezier_curve_generator
from main.bezierCurveAlgorithms.deCasteljau import de_casteljau_level
from main.Geometry.Point import Point2D
from main.Geometry.Point import ControlPoints


class DeCasteljauTestCase(unittest.TestCase):
    def setUp(self):
        self.point1 = Point2D(x=0, y=0)
        self.point2 = Point2D(x=15, y=85)
        self.point3 = Point2D(x=-96, y=14)

    def test_casteljau_level(self):
        """
        Tests the function used to make one level of the De Casteljau Algorithm
        """

        resulted_points = de_casteljau_level([self.point1,self.point2,self.point3],0.5)

        assert len(resulted_points) == 2
        assert resulted_points[0].X == 7.5
        assert resulted_points[0].Y == 42.5
        assert resulted_points[1].X == -40.5
        assert resulted_points[1].Y == 49.5

        pass


    def test_single_point(self):
        """
        Tests the algorithm when there is only one control point
        """

        #Creates a high-order function the generates point on the Bezier Curve for a set of controls points
        bezier_curve = bezier_curve_generator(ControlPoints([self.point1]))

        #Since there is only one control point, any value passed as parameter should return this point
        assert self.point1 == bezier_curve(0)
        assert self.point1 == bezier_curve(1)
        assert self.point1 == bezier_curve(0.5)
        pass

    def test_parameter_zero(self):
        """
        Tests the algorithm when the parameter passed is zero
        """

        bezier_curve = bezier_curve_generator(ControlPoints([self.point1, self.point2, self.point3]))

        bezier_point = bezier_curve(0)
        assert isinstance(bezier_point, self.point1)
        assert self.point1 == bezier_point
        pass

    def test_parameter_one(self):
        """
        Tests the algorithm when the parameter passed is one
        """

        bezier_curve = bezier_curve_generator(ControlPoints([self.point1, self.point2, self.point3]))

        bezier_point = bezier_curve(1)
        assert isinstance(bezier_point, self.point3)
        assert self.point3 == bezier_point
        pass

    def test_de_casteljau_complete(self):
        """
        Tests the algorithm for a parameter neither at the start or at the end of the curve, using all 3 points
        """

        bezier_curve = bezier_curve_generator(ControlPoints([self.point1, self.point2, self.point3]))

        bezier_point = bezier_curve(0.5)  #Result => (-16,5;46)

        assert Point2D(-16.5, 46) == bezier_point

        pass

    def test_exaustive(self):
        """
        Tests the algorithm for 10000 points, forcing the recursive aspect of it, due Python's limitation
        """
        control_points_list = []

        for x in range(0, 10000):
            control_points_list.append(Point2D(x=randint(0, 1000), y=randint(0, 10000)))

        bezier_curve = bezier_curve_generator(ControlPoints(control_points_list))

        bezier_point = bezier_curve(0)
        assert isinstance(bezier_point, control_points_list[0])
        assert control_points_list[0] == bezier_point

        pass
