data = input()
arr = []
for a in range(len(data)):
    arr.append(data[a])
for a in range(len(arr) - 4):
    if arr[a].isdigit():
        arr[a] = "*"
for a in range(len(arr)):
    print(arr[a], end ="")