def is_inside(a, b):
    if (b[0] <= a[0] <= b[0] + b[2]) and (b[1] <= a[1] <= b[1] + b[3]):
        # print("True - The point is inside a rectangle.")
        return True
    else:
        # print("False - The point isn't inside a rectangle.")
        return False
