n = int(input())

c = {
    "AC": 0,
    "WA": 0,
    "TLE": 0,
    "RE": 0
}

for i in range(n):
    s = input()
    c[s] += 1

print("AC x", c["AC"])
print("WA x", c["WA"])
print("TLE x", c["TLE"])
print("RE x", c["RE"])