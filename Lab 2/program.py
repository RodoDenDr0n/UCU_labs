import math


def sales_prediction():
    a = float(input())
    b = a*1.19
    print(b)
    pass


def yard_to_meter():
    a = float(input())
    mm = a * 914
    m = a * 0.914
    km = a * 0.000914
    print(mm)
    print(m)
    print(km)
    pass


def cashier():
    p1 = float(input())
    p2 = float(input())
    p3 = float(input())
    p4 = float(input())
    p5 = float(input())
    sum = p1+p2+p3+p4+p5
    tax = sum * 14/100
    total = sum + tax
    print(sum)
    print(tax)
    print(total)
    pass


def odometer():
    v0 = float(input())
    a = float(input())
    t1 = float(input())
    t2 = float(input())
    v = v0 + a*t1
    s1 = abs(v*t2 + (a*t1**2)/2)
    s2 = abs(v*t2)
    print(s1)
    print(s2)
    pass


def payment_instalments():
    sum = float(input())
    n = int(input())
    sum *= (105/100)
    n_pay = sum/n
    print(sum)
    print(n_pay)
    pass


def miles_per_galon():
    md = float(input())
    gogu = int(input())
    mpg = md/gogu
    print(mpg)
    pass


def cookie():
    sugar = 1.5
    butter = 1
    flour = 2.75
    bisc = int(input())
    n = bisc*100/48
    sugar = (sugar * n)/100
    butter = n/100
    flour = (flour*n)/100
    print(sugar)
    print(butter)
    print(flour)
    pass


def vineyard():
    R = float(input())
    E = float(input())
    S = float(input())
    V = math.floor((R - 2*E) / S)
    print(V)
    pass


def compound_interest():
    P = float(input())
    r = int(input())
    n = int(input())
    t = int(input())
    A = P * ((1 + (r/100)/n))**(n*t)
    print(A)
    pass


if __name__ == "__main__":
    eval(input() + "()")


# sales_prediction()
# yard_to_meter()
# cashier()
# odometer()
# payment_instalments()
# miles_per_galon()
# cookie()
# vineyard()
# compound_interest()