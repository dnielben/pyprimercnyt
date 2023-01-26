import math

def sumacplx(c1,c2):
    real = c1[0] + c2[0]
    img = c1[1] + c2[1]
    resultado = (real,img)
    return resultado

def prettyPcplx(c):
    print("{} + {}i".format(c[0],c[1]))

def multcplx(c1,c2):
    real = ((c1[0]*c2[0])-(c1[1]*c2[1]))
    img = (c1[0]*c2[1])+(c1[1]*c2[0])  
    resultado = (real,img)
    return resultado

def modulocplx(c):
    modu = math.sqrt(c[0]**2+c[1]**2)
    return modu

if __name__ == '__main__':
    prettyPcplx((7,-4))

    prettyPcplx(sumacplx((3,-8),(4,6)))
    prettyPcplx(multcplx((2,-3),(-1,1)))
    print(modulocplx((-2,-3)))
