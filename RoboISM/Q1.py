a = input()
a = a.split()
c = input()
def sorting(a, c):
    if c == 'asc':
        a.sort()
    if c == 'desc':
        a.sort(reverse = True)
    if c == 'None':
        pass
    return a


sorting(a, c)
print(a)