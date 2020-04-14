import numpy as np
np.random.seed(3)
def matrix_factorization(A, K, eta, steps):
    # khởi tạo 2 ma trận W, H radom
    W = np.random.rand(user, K)
    H = np.random.rand(K, item)
    step =0
    while(step < steps):
        for u in range(0, user):
            for i in range(0, item):
                if A[u][i] >0 :
                    r_bar =0
                    for k in range(K):
                        r_bar += np.dot(W[u][k], H[k][i])
                    eui = A[u][i] - r_bar
                    for k in range(K):
                        W[u][k] += 2*eta*(eui* H[k][i])
                        H[k][i] += 2*eta*(eui* W[u][k])
        step +=1
    return np.dot(W,H)

A = np.array([[1,4,5,0,3],
              [5,1,0,5,2],
              [4,1,2,5,0],
              [0,3,4,0,4]])
print('A', A)

soUser = A.shape[0]
soItem = A.shape[1] 
print('So user:', user)
print('So item:', item)

MF =matrix_factorization(A,3,0.01,1000)
Y =np.array([[round(MF[i][j]) for j in range(item)]for i in range(user)]) #làm tròn
print('Ma tran ban dau: ', A)
print('Ma tran sau khi ap dung MF: ', MF)
print('Ma tran làm tròn:',Y)
