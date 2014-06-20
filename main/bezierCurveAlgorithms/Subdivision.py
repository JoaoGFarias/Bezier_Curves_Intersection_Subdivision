__author__ = 'Joao'

from Geometry.Point import ControlPoints
from Geometry.Point import Point2D
from bezierCurveAlgorithms.deCasteljau import bezier_curve_generator
from fn import recur

def subdivide(control_points,t = 0.5):
    """
    @param control_points: The control points of the Bezier curve
    @param t: parameter used to subdivide
    @return: A tuple with two ControlPoint objects, represent each curve
    """

    if(isinstance(control_points,list)): control_points = ControlPoints(control_points)
    [curve1,curve2] = aux_subdivide(control_points,[],[],t)
    return ControlPoints(curve1),ControlPoints(curve2)
    pass

@recur.tco  #Avoids stack overflow due recursion
def aux_subdivide(points, curve1=None, curve2=None, t=0.5):
    if not curve1: curve1 = [points[0]]
    if not curve2:curve2 = [points[len(points)-1]]
    if len(points) <= 1:
        return False, [curve1,curve2] #End of the recursion
    else:
        new_points = []

        for i in range(0,len(points)-1):
            new_points.append(points[i].linear_interpolation(points[i+1],t))
        curve1.append(new_points[0])
        curve2.insert(0,new_points[len(new_points)-1]) #Add at the start of the list

        return True, (new_points,curve1,curve2,t)



if __name__ == '__main__':

    point1 = Point2D(x=0, y=0)
    point2 = Point2D(x=15, y=85)
    point3 = Point2D(x=-96, y=14)
    point4 = Point2D(x=-89.6, y=784.666)

    as_control_points = ControlPoints([point1, point2, point3,point4])
    (curve1,curve2) = subdivide(as_control_points,0.5)
    middle_point = bezier_curve_generator(ControlPoints([point1, point2, point3, point4]))(0.5)

    assert curve1[0] == point1 #Starts at the first control point
    assert curve1[3] == middle_point #Ends at the middle of the curve
    assert curve2[0] == middle_point #Starts at the middle of the curve
    assert curve2[3] == point4 #Ends at the last control point