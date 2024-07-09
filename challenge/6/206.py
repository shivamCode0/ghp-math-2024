import re
import math

r = re.compile(r"1\d2\d3\d4\d5\d6\d7\d8\d9\d0")

a = "1_2_3_4_5_6_7_8_9_0"
a1 = int(a.replace("_", "0"))
a2 = int(a.replace("_", "9"))

a1 = math.floor(math.sqrt(a1))
a2 = math.ceil(math.sqrt(a2))

print(a1, a2)

a1 = round(a1, 10)

print(a1, a2, a2 - a1)
print("testing")

for i in range(a1, a2, 10):
    # print every 1 % of the way
    if i % int(1e6) == 0:
        print(i)
    if r.search(str(i**2)):
        print(i)
        break
# 1192213971
