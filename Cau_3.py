
A = []
count = 0
n = int(input("Nhap so nguyen n: "))

for i in range(n):
    num = int(input("Nhap so thu "+str(i+1)+": "))
    A.append(num)
    if (num % 2 == 0) and (num %5 == 0):
        count = count +1

print("Có ", count, " số chia hết cho 2 và 5")


