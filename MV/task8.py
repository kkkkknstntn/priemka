import numpy as np
t = 15
h = 1
x = []
y_res_t = []
p_x = []
q_x = []
f_x = []
def funct(x):
    return 4*x*x*x*x - 3*x*x*x + 6*x - 2
def method_progon(a,b,c,d,m):
    p = np.zeros(m,dtype=float)
    q = np.zeros(m,dtype=float)
    p[0] = c[0] / b[0]
    q[0] = -1*d[0] / b[0]
    for i in range(m-1):
        p[i+1] = c[i+1] / (b[i+1] - a[i+1] * p[i])
        q[i+1] = (a[i+1] * q[i] - d[i+1]) / (b[i+1] - a[i+1] * p[i])
    x = np.zeros(m)
    x[m-1] = q[m-1]
    for i in range(m-1,0,-1):
        x[i-1] = p[i-1]*x[i]*q[i-1]
    return x
i = 0
while i <= t:
    x.append(i)
    y_res_t.append(i*i*(i-1))
    p_x.append(i*i)
    q_x.append(i*i*i)
    f_x.append(funct(i))
    i += h
y_res_m = np.zeros(len(y_res_t),dtype=float)
eps = np.zeros(len(y_res_t),dtype=float)
y_res_m[0] = 0
y_res_m[len(y_res_t)-1] = 0
m = len(p_x) - 2
array_a = np.zeros(m,dtype=float)
array_b = np.zeros(m,dtype=float)
array_c = np.zeros(m,dtype=float)
array_d = np.zeros(m,dtype=float)
array_a[0] = 0
array_c[m-1] = 0
for i in range(1,m):
    array_a[i] =  1/(h*h) - p_x[i+1] / (2*h)
for i in range(m):
    array_b[i] =  2/(h*h) - q_x[i+1]
    array_d[i] = f_x[i+1]
for i in range(m-1):
    array_c[i] = 1/(h*h)+p_x[i+1]/(2*h)
y_res = method_progon(array_a,array_b,array_c,array_d,m)
for i in range(1,m+1):
    y_res_m[i] = y_res[i-1]
for i in range(len(p_x)):
    eps[i] = abs(y_res_t[i] - y_res_m[i])
print("x(k)",end=" ")
for i in range(len(x)):
    print('{:.2f}'.format(x[i]),end=" ")
print()
print("y(t)",end=" ")
for i in range(len(y_res_t)):
    print('{:.2f}'.format(y_res_t[i]),end=" ")
print()
print("y(m)",end=" ")
for i in range(len(y_res_m)):
    print('{:.2f}'.format(y_res_m[i]),end=" ")
print()
print("e(k)",end=" ")
for i in range(len(eps)):
    print('{:.2f}'.format(eps[i]),end=" ")
