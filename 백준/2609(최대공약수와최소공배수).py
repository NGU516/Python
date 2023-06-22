import math
a,b = map(int, input().split())
lcm = math.lcm(a,b)
gcd = math.gcd(a,b)
print(gcd)
print(lcm)
