__author__ = 'Joao'

import unittest

from Geometry.Point import Point2D
from main.Geometry.Point import ControlPoints
from Geometry.BoundingBox import BoundingBox


class MyTestCase(unittest.TestCase):

    def setUp(self):
        #A square
        self.point1 = Point2D(0,0)
        self.point2 = Point2D(0,5)
        self.point3 = Point2D(5,0)
        self.point4 = Point2D(5,5)
        pass

    def box_of_a_square(self):

        as_list = [self.point1,self.point2,self.point3,self.point4]
        bb = BoundingBox(as_list)
        assert bb.upper_point == self.point2
        assert bb.bottom_point == self.point3

        as_control_points = ControlPoints(as_list)
        bb = BoundingBox(as_control_points)
        assert bb.upper_point == self.point2
        assert bb.bottom_point == self.point3

    def not_a_square(self):
        as_list = [self.point1,self.point2,self.point3,self.point4,Point2D(90,90)] #No longer a square
        bb = BoundingBox(as_list)
        (correct_upper,correct_bottom) = (Point2D(0,90),Point2D(90,0))
        assert bb.upper_point == correct_upper
        assert bb.bottom_point == correct_bottom

if __name__ == '__main__':
    unittest.main()
