from scipy import integrate
import math


def f(x):
    return x + 1


v, err = integrate.quad(f, 1, 2)
print(v)

r0 = 17.18
c = 1.985
h0 = 2.45


def r(h):
    r1 = r0 + c * math.log(h / h0)
    rh = c / h
    return r1 * math.sqrt(1 + rh ** 2)


# S = 2 * pi * integrate(r*sqrt(1+ rh**2), (h, 0, h0))
s, err1 = integrate.quad(r, 0, h0)
print(s)


def h3(R):
    h1 = h0*math.exp((R-r0)/c)
    return math.sqrt(1+h1**2/c**2)*R


s1, err2 = integrate.quad(h3, 0, r0)
print(s1)
