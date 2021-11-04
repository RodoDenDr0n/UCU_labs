"""AREA OF QUADRANGLE"""


#=====< Main Function >=====#
def four_lines_area(coef_k1, coef_c1, coef_k2, coef_c2, coef_k3, coef_c3, coef_k4, coef_c4):
    """
    This function gets the coefficients of the four lines
    and returns the area of quadrangle
    """
    if coef_k1 == coef_k2 == coef_k3 or \
       coef_k1 == coef_k2 == coef_k4 or \
       coef_k1 == coef_k3 == coef_k4 or \
       coef_k2 == coef_k3 == coef_k4:
        return 0
    else:
        try:
            coordinate_x1, coordinate_y1 = lines_intersection(coef_k1, coef_c1, coef_k2, coef_c2)
            coordinate_x2, coordinate_y2 = lines_intersection(coef_k2, coef_c2, coef_k3, coef_c3)
            coordinate_x3, coordinate_y3 = lines_intersection(coef_k3, coef_c3, coef_k4, coef_c4)
            coordinate_x4, coordinate_y4 = lines_intersection(coef_k4, coef_c4, coef_k1, coef_c1)
            diagonal_f1 = distance(coordinate_x1, coordinate_y1, coordinate_x3, coordinate_y3)
            diagonal_f2 = distance(coordinate_x2, coordinate_y2, coordinate_x4, coordinate_y4)
            side_a = distance(coordinate_x1, coordinate_y1, coordinate_x2, coordinate_y2)
            side_b = distance(coordinate_x2, coordinate_y2, coordinate_x3, coordinate_y3)
            side_c = distance(coordinate_x3, coordinate_y3, coordinate_x4, coordinate_y4)
            side_d = distance(coordinate_x4, coordinate_y4, coordinate_x1, coordinate_y1)
            return quadrangle_area(side_a, side_b, side_c, side_d, diagonal_f1, diagonal_f2)
        except:
            return None


#=====< Intersection Coordinates >=====#
def lines_intersection(coef_k1, coef_c1, coef_k2, coef_c2):
    """
    This function gets the coefficients of the two lines and
    identifies the coordinates of intersection between two lines
    """
    if coef_k1 == coef_k2:
        return None
    else:
        coordinate_x = (coef_c2-coef_c1)/(coef_k1-coef_k2)
        coordinate_y = (coef_k1*coordinate_x)+coef_c1
        return round(coordinate_x, 2), round(coordinate_y, 2)


#=====< Distance Between Coordinates >=====#
def distance(coordinate_x1, coordinate_y1, coordinate_x2, coordinate_y2):
    """
    This function gets the coordinates of intersection
    between two lines and calculates the length of the line
    """
    dist = ((coordinate_x2 - coordinate_x1) ** 2 + \
                (coordinate_y2 - coordinate_y1) ** 2) ** 0.5
    return round(dist, 2)


#=====< Quadrangle Area >=====#
def quadrangle_area(side_a, side_b, side_c, side_d, diagonal_f1,\
                    diagonal_f2):
    """
    This function gets the length of quadrangle's sides
    and diagonals and calculates the area of quadrangle
    """
    try:
        area = (((4 * (diagonal_f1 ** 2) * (diagonal_f2 ** 2) - \
                    (side_b ** 2 + side_d ** 2 - side_a ** 2 - side_c ** 2) ** 2) / 16) ** 0.5)
        return round(area, 2)
    except:
        return None


print(four_lines_area(0, 20, 3, -0.3, 0.1, 10, -5, 3))
