
A = []
count_chan = 0
count_le = 0

k = int(input("Nhap so nguyen k: "))
n = int(input("Nhap so nguyen n: "))

for i in range(n):
    num = int(input("Nhap so thu "+str(i+1)+": "))
    A.append(num)

print("Các số >=" , k , " là:")

for i in range(n):
    if A[i] >= k:
        print(A[i])


