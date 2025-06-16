def f(i, c, s):
    if s == t and c:
        t_c = tuple(sorted(c))
        if t_c not in seen:
            print(*c)
            seen.add(t_c)
            r.append(c[:])
    if i == n or s > t:
        return
    f(i+1, c+[a[i]], s+a[i])
    f(i+1, c, s)

n, t = map(int, input().split())
a = list(map(int, input().split()))
r = []
seen = set()
f(0, [], 0)

if not r:
    print("NO")


#########################################

def f(i, c, s):
    if s == t and c:
        t_c = tuple(sorted(c))
        if t_c not in seen:
            print(*c)
            seen.add(t_c)
            r.append(c[:])
    if i == n or s > t:
        return
    f(i + 1, c + [a[i]], s + a[i])  # include a[i]
    f(i + 1, c, s)                  # exclude a[i]

# Input
n, t = map(int, input("Enter number of elements and target sum: ").split())
a = list(map(int, input("Enter the elements: ").split()))

r = []
seen = set()
f(0, [], 0)

if not r:
    print("NO")
