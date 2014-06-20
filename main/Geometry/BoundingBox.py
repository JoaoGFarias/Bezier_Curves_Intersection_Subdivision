__author__ = 'Joao'

from Point import Point2D
from Point import ControlPoints

class BoundingBox(object):
    """    """

    def __init__(self, points):
        """Defines the Bouding Box (upper and bottom points) for a given list of points
        @param points: [Points2D] or ControlPoints
        """
        assert (isinstance(points, list)) or (isinstance(points, ControlPoints))
        min_x = points[0].X
        min_y = points[0].Y
        max_x = points[0].X
        max_y = points[0].Y

        for point in points:
            (x,y) = (point.X,point.Y)
            if(x > max_x):max_x = x
            if(x < min_x): min_x = x
            if(y > max_y):max_y = y
            if(y < min_y): min_y = y

        self.upper_point = Point2D(min_x,max_y)
        self.bottom_point = Point2D(max_x,min_y)
        pass

    def __str__(self):
        return "Point(%s,%s)"%(self.X, self.Y)

    @property
    def as_four_points(self):
        """
        Returns a list with four points the represent the Bounding Box
        See how to map the points in the list with the index
        1 --- 2
        |     |
        |     |
        0 --- 3
        @return: [Point2D]
        """
        return [
            Point2D(self.upper_point.X,self.bottom_point.Y),
            Point2D(self.upper_point.X,self.upper_point.Y),
            Point2D(self.bottom_point.X,self.upper_point.Y),
            Point2D(self.bottom_point.X,self.bottom_point.Y)
        ]


if  __name__ == '__main__':
    point1 = Point2D(0,0)
    point2 = Point2D(0,5)
    point3 = Point2D(5,0)
    point4 = Point2D(5,5)

    as_list = [point1,point2,point3,point4]
    bb = BoundingBox(as_list)
    assert bb.upper_point == point2
    assert bb.bottom_point == point3

    as_control_points = ControlPoints(as_list)
    bb = BoundingBox(as_control_points)
    assert bb.upper_point == point2
    assert bb.bottom_point == point3

    as_list = [point1,point2,point3,point4,Point2D(90,90)]
    bb = BoundingBox(as_list)
    (correct_upper,correct_bottom) = (Point2D(0,90),Point2D(90,0))
    assert bb.upper_point == correct_upper
    assert bb.bottom_point == correct_bottom
    pass
