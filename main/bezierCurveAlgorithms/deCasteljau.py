__author__ = 'Joao'

from fn import recur

def bezier_curve_generator(control_points_list):
    """
    Creates a high-order function that returns points on the Bezier curve created
    for a given set of points
    @rtype : function
    @type control_points_list: ControlPoints
    @param control_points_list: List of control points  of the Bezier Curve to be generated
    """

    def foo(t):
        control_points=control_points_list.getControPoints()
        return bezier_curve(control_points,t)
    return foo

@recur.tco  #Avoids stack overflow due recursion
def bezier_curve(points, t):

    """

    @param points: Control points of the bezier curve
    @param t: Interpolation paramter for finding the point
    @return: A Point2D representing the point on the bezier curve
    """
    if len(points) <= 1:
        return False, points[0] #End of the recursion
    else:
        newPoints = []

        for i in range(0,len(points)-1):
            newPoints.append(points[i].linear_interpolation(points[i+1],t))

        return True,(newPoints,t)