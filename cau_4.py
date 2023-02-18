A = []
count_so_hoan_hao = 0
count_so_nguyen_to = 0
n = int(input("Nhap so nguyen n: "))
for i in range(n):
    num = int(input("Nhap so thu "+str(i+1)+": "))
    A.append(num)

# số hoàn hảo
for i in range(n):
    s = 0
    for j in range(1,A[i]):
        if A[i] % j == 0:
            s = s + j
    if s == A[i]:
        count_so_hoan_hao = count_so_hoan_hao+1

print("Có ", count_so_hoan_hao, " số hoàn hảo")

#so nguyên tố
for i in range(n):
    check = 0
    for j in range(2,A[i]):
        if A[i] % j == 0:
            check = 1
    if check == 0:
        count_so_nguyen_to = count_so_nguyen_to + 1


print("Có ", count_so_nguyen_to, " số nguyên tố")

