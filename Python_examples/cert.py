l = [i for i in range(20)]
f = [i * 2 for i in l if i % 2]
k = [i * 2 for i in l if i != 2 * (i // 2)]
print(l)
print(f)
print(k)

s = set("f")

f = {name for name in s}
print(s)
print(f)
