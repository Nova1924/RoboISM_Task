data = input()
arr = []
for a in range(len(data)):
    arr.append(data[a])
count = 1
for a in range(int(len(arr) / 2) + 1):
    if arr[a] == arr[-a - 1]:
        pass
    else:
        count = 0
        print("Not a Palindrome")
        break
if count == 1:
    print("It is a Palindrome")