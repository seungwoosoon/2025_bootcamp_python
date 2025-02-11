n = int(input("input num"))
cnt = 0
for i in range(2, n):
    if (n%i == 0):
        cnt += 1
        break

if cnt == 1:
    print("prime")
else:
    print("not prime")