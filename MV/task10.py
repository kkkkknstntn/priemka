import numpy as np
t = 15
h = 1
x = []
y_res_t = []
p_x = []
q_x = []
f_x = []
determinat = 1
def funct(x):
    return 4*x*x*x*x - 3*x*x*x + 6*x - 2
def switch(index,matrix,b):
    main_elem = matrix[index,index]
    in_2 = index
    for i in range(index+1,len(matrix)):
        if abs(matrix[i][index]>main_elem):
            main_elem = matrix[i,index]
            in_2 = i
        if main_elem != 0:
            temp = np.zeros(len(matrix))
            temp[i] = matrix[i,index]
            matrix[i,index] = matrix[i,in_2]
            matrix[i,in_2] = temp[i]
def method_gauss(matrix, b,n,E,determinat):
    x_res = np.zeros(n)
    cnt = 0
    for i in range(n):
        p1 = matrix[i,i]
        determinat *= p1
        if abs(p1) <=E:
            cnt += 1
            switch(i,matrix,b)
            p1 = matrix[i,i]
        for j in range(n):
            matrix[i,j] /= p1
        b[i] /= p1
        for k in range(i+1,n):
            consta = matrix[k,i]
            for j in range(n):
                matrix[k,j] -= (consta * matrix[i,j])
            b[k] -= consta*b[i]
        x_res[n-1] = b[n-1]
        cnt_s = 1
        for j in range(n-2,-1,-1):
            k = 1
            dif = 0
            while k <= cnt_s:
                dif += (matrix[j,j+k] * x_res[j+k])
                k += 1
            x_res[j] = b[j] - dif
            cnt_s += 1
    if cnt_s % 2 != 0:
        determinat *=-1
    return x_res
i = 0
while i <= t:
    x.append(i)
    y_res_t.append(i*i*(i-1))
    p_x.append(i*i)
    q_x.append(i)
    f_x.append(funct(i))
    i += h
n = len(f_x)
y_res_m = np.zeros(n,dtype=float)
eps = np.zeros(n,dtype=float)
matrix = np.zeros((n-2,n-2),dtype=float)
b = np.zeros(n-2,dtype=float)
for i in range(n-2):
    b[i] = f_x[i+1]
for i in range(n-2):
    for j in range(n-2):
        #первая производная
        first_s = (j+1) * (j+x[i+1]**(j-1)) * (x[i]-1) + (x[i+1]**j) + (j+1)*(x[i+1]**j)
        #вторая производная
        second_s = (p_x[i+1]*(j+1)) * (x[i+1]**j) * (x[i+1]-1) + (x[i+1]**(j-1))
        third_s = q_x[i+1] * (x[i+1]**(j+1)) * (x[i+1]-1)
        matrix[i,j] = first_s+second_s+third_s
#краевый условия
y_res_m[0] = 0
y_res_m[len(y_res_t)-1] = 0
A = method_gauss(matrix,b,n-2,0.01,determinat)
for i in range(1,n-1):
    sum = 0.0
    for j in range(n-2):
        sum += A[j] * x[i]**(j+1) *(x[i]-1)
    y_res_m[i] = sum
for i in range(n):
    eps[i] = abs(y_res_t[i] - y_res_m[i])
print("x(k):", end=" ")
for i in range(len(x)):
    print('{:.2f}'.format(x[i]),end=" ")
print()
print("y(t):", end=" ")
for i in range(len(y_res_t)):
    print('{:.2f}'.format(y_res_t[i]),end=" ")
print()
print("y(m):", end=" ")
for i in range(n):
    print('{:.2f}'.format(y_res_m[i]),end=" ")
print()
print("e(k):", end=" ")
for i in range(n):
    print('{:.2f}'.format(eps[i]),end=" ")
