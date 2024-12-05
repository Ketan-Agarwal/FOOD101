def getinput():
    t = []
    while(len(t)!=4):
        t = list(map(int, input("Enter exactly 4 coefficients of cubic polynomial separated by spaces: ").split()))
        if len(t) != 4:
            print(f"You entered {len(t)} coefficients, not 4.")

    return tuple(t)

def getx():
    return int(input("Enter the value of x at where slope is to be determined: "))


def slope_of_cubic(tup, x):
    slope_at_x = tup[0]*3*(x**2) + tup[1]*2*x + tup[2]
    return slope_at_x



print(slope_of_cubic(getinput(), getx()))