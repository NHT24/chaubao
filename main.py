
A = []
count_chan = 0
count_le = 0
n = int(input("Nhap so nguyen n: "))

for i in range(n):
    num = int(input("Nhap diem thu"+str(i+1)+": "))
    A.append(num)
    if num % 2 == 0:
        count_chan = count_chan+1
    else:
        count_le = count_le+1

print("Có ", count_chan, " số chẵn")
print("Có ", count_le, " số lẻ")

