data = input()
arr = []
s = 0
for a in range(len(data)):
    arr.append(data[a])
for a in range(len(arr)):
    if arr[a].isdigit():
        s += int(arr[a])
print(s)