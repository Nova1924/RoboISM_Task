data = input()
arr = data.split()
for a in range(len(arr)):
    arr[a] = int(arr[a])
arr.sort()
max = 0
num = arr[0]
for a in arr:
    freq = arr.count(a)
    if freq > max:
        max = freq
        num = a
print("Highest Frequency :" + str(num))