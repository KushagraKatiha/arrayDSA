## Check if given points are collinear or not

## Method 1

def collinearPointsTriangleMethod(a,b,c,d,e,f):
    areaOfTriangle = 1/2*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y3))
    result = None
    if areaOfTriangle > 0:
        result = "Points are not collinear"
    else:
        result = "Points are collinear"

    return result

## Method 2

def collinearPointsSlopeMethod(a,b,c,d,e,f):
        result = None
        if ((x2-x1)*(y3-y2) == (x3-x2)*(y2-y1)) == ((x3-x1)*(y3-y1) == (x3-x2)*(y3-y2)) :
            result = "Points are collinear"
        else:
             result = "Points are non collinear"

        return result

## Driver Code

x1, x2, x3, y1, y2, y3 = 1, 3, 1, 6, 0, 9

result = collinearPointsTriangleMethod(x1, x2, x3, y1, y2, y3)
print(result)

result2 = collinearPointsSlopeMethod(x1, x2, x3, y1, y2, y3)
print(result2)