__author__ = 'Joao'

from Geometry.Point import Point2D

class Line(object):

    def __init__(self, p1, p2):
        """Defines two points that form the straigt line"""

        assert isinstance(p1, Point2D)
        assert isinstance(p2, Point2D)
        self.p1 = p1
        self.p2 = p2

    def __eq__(self, other):
        return self.is_on_line(other.p1) and self.is_on_line(other.p2)

    def __str__(self):
        return "Point(%s,%s)"%(self.X, self.Y)


    def is_on_line(self, point):
        """ Checks whether a point is on the line"""
        (x,x1,x2) = (point.x,self.p1.X,self.p2.X)
        (y,y1,y2) = (point.y,self.p1.Y,self.p2.Y)
        #Using the interpolation formula, to check if there is parameter t: X = (1-t)*A + t*B
        return (x-x1)/x2-x1 == (y-y1)/y2-y1

    def linear_interpolation(self,t):
        """
        Calculates the linear interpolation on the line
        @param t: Interpolation parameter
        @return: Point2D
        """
        return self.p1.linear_interpolation(self.p2,t)

    def top_and_bottom_points(self,height,width):
        """
        Calculates points on the line that touch the extremities of the screen
        Useful to draw the line
        @param height: Maximum of height of the screen
        @param width: Maximum of width of the screen
        @return: The two points that touch the extremities of the screen
        @rtype : (Point2D,Point2D)
        """
        pass
