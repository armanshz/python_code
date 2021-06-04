# generate a random matrix 
import numpy as np
Random_A = np.random.randint(0,11,(5,5)) 
print(Random_A)

To standardize all the following answers, we will be using a fixed matrix shown below 
A = np.matrix([[0,3,0,5,5],[6,2,7,8,1],[10,9,4,4,4],[9,1,0,1,7],[5,1,8,8,0]])

# Qns 1(i)
B= np.diag(A)
print(B)

# Qns 1(ii)
C=np.linalg.det(A)
print(C)

# Qns 1(iii)
D=np.linalg.inv(A)*C 
print(D)

# Qns 1(iv)
E=np.max(A,axis=0) 
print(np.max(E))

# Qns 1(v)
F=np.min(A,0)
print(np.min(F))

# Qns 1(vi)
G=np.sum(E)
print(G)

# Qns 1(vii)
H=np.average(A,axis=0)
print(np.sum(H))

# Qns 1(viii)
I=np.sort(A,0)
print(I)

# Qns 1(ix)
J=np.sort(A,1)
print(J)

# Qns 1(x)
K=np.sort(A,1)
print(K)

# Qns 1(xi)
L = np.ones((4,6))
print(L)
print(A+L)

# Qns 1(xii)
[x,y]=np.linalg.eig(A)
print([x,y])

# Qns 1(xiii)
[p,q]=np.shape(A)
print([p,q])

# Qns 1(xiv)
print(A[:,2])

# Qns 1(xv)
print(A[3,:])

# Qns 1(xvi)
A[3,4]=0
print(A)

# Qns 1(xvii)
print(max(A[:,0]))

# Qns 1(xviii)
print(np.average(A[2,:]))

# Qns 1(xix)
M=np.matmul(A,A)
print(M)

# Qns 1(xx)
N=np.square(A)
print(N)

