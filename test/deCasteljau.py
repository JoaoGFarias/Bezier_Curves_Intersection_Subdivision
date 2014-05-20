__author__ = 'Joao'

import unittest
from random import randint
from main.bezierCurveAlgorithms.deCasteljau import bezierCurveGenerator
from main.Geometry.Point import Point2D
from main.Geometry.Point import ControlPoints


class deCasteljauTestCase(unittest.TestCase):
    def setUp(self):
        self.point1 = Point2D(x=0, y=0)
        self.point2 = Point2D(x=15, y=85)
        self.point3 = Point2D(x=-96, y=14)

    def testSinglePoint(self):
        """
        Tests the algorithm when there is only one control point
        """

        #Creates a high-order function the generates point on the Bezier Curve for a set of controls points
        beziercurve = bezierCurveGenerator(ControlPoints([self.point1]))

        #Since there is only one control point, any value passed as parameter should return this point
        assert self.point1 == beziercurve(0)
        assert self.point1 == beziercurve(1)
        assert self.point1 == beziercurve(0.5)
        pass

    def testParameterZero(self):
        """
        Tests the algorithm when the parameter passed is zero
        """

        beziercurve = bezierCurveGenerator(ControlPoints([self.point1, self.point2, self.point3]))

        bezierpoint = beziercurve(0)
        assert isinstance(bezierpoint, self.point1)
        assert self.point1 == bezierpoint
        pass

    def testParameterOne(self):
        """
        Tests the algorithm when the parameter passed is one
        """

        beziercurve = bezierCurveGenerator(ControlPoints([self.point1, self.point2, self.point3]))

        bezierpoint = beziercurve(1)
        assert isinstance(bezierpoint, self.point3)
        assert self.point3 == bezierpoint
        pass

    def testDeCasteljauComplete(self):
        """
        Tests the algorithm for a parameter neither at the start or at the end of the curve, using all 3 points
        """

        beziercurve = bezierCurveGenerator(ControlPoints([self.point1, self.point2, self.point3]))

        bezierpoint = beziercurve(0.5)  #Result => (-16,5;46)

        assert Point2D(-16.5, 46) == bezierpoint

        pass

    def testExaustive(self):
        """
        Tests the algorithm for 10000 points, forcing the recursive aspect of it, due Python's limitation
        """
        controlPointsList = []

        for x in range(0, 10000):
            controlPointsList.append(Point2D(x=randint(0, 1000), y=randint(0, 10000)))

        beziercurve = bezierCurveGenerator(ControlPoints(controlPointsList))

        bezierpoint = beziercurve(0)
        assert isinstance(bezierpoint, controlPointsList[0])
        assert controlPointsList[0] == bezierpoint

        pass
