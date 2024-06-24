f = open("challenge-1/2.txt", "w")

for i in range(0, 100000, 16):
    v = 85 * i / 16 + 40
    if v % 100 == 0:
        a = v / 100
        b = i
        print(a, f"{b:.1f}*1 + {b*3/4:.1f}*2 + {b*(3/4)**2:.1f}*5 + 5.0*8", file=f)
