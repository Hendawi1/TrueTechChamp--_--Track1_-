#!/usr/bin/env python3
import sys
from fractions import Fraction

def heron_sq(a, b, c):
    if not (a+b>c and a+c>b and b+c>a):
        return 0
    s = Fraction(a+b+c, 2)
    area_sq = s*(s-a)*(s-b)*(s-c)
    return area_sq if area_sq > 0 else 0

def main():
    data = sys.stdin.read().strip().split()
    if len(data) < 3:
        return
    a, b, c = map(int, data)
    
    candidates = [
        (a+b, a+c, b+c),
        (abs(a-b), a+c, b+c),
        (a+b, abs(a-c), b+c),
        (a+b, a+c, abs(b-c))
    ]
    
    res = []
    for d01, d02, d12 in candidates:
        if 0 in (d01, d02, d12):  # совпадение окружностей
            continue
        area_sq = heron_sq(d01, d02, d12)
        if area_sq and area_sq.denominator == 1:
            res.append(area_sq.numerator)
    
    if not res:
        print(-1)
    else:
        print(min(res), max(res))

if __name__ == "__main__":
    main()

