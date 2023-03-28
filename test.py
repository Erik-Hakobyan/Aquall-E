# import numpy as np
import matplotlib.pyplot as plt

# A = np.array([[1,0,0],[1,0,1],[1,1,0],[1,1,1]])
# B = (A.T).dot(A) 
# C = np.linalg.inv(B)
# D = C.dot(A.T)
# E = np.array([[1],[4],[3],[7]])
# print(D.dot(E))
def descent(w0,w1,alpha,num_iter):
    w_0 = []
    w_1 = []
    for i in range(1,num_iter+1):
        temp0 = w0 - (alpha*(2*(w0+(2*w1)-4)+2*(w0+(3*w1)-3)))
        temp1 = w1 - (alpha*(4*(w0+(2*w1)-4)+6*(w0+(3*w1)-3)))
        w0 = temp0
        w1 = temp1
        w_0.append(w0)
        w_1.append(w1)
        f = (((w0+(2*w1)-4)**2)+((w0+(3*w1)-3)**2))
        print(i, "step")
        print("w0: ",w0," w1: ",w1," f: ",f)
    return w_0,w_1


def main():

    # num_iter = 10
    # plt.plot(range(1,num_iter+1), descent(0,0,0.06,10)[0], label = "alpha: 0.06 w0")
    # plt.plot(range(1,num_iter+1), descent(0,0,0.06,10)[1], label = "alpha: 0.06 w1")

    # plt.plot(range(1,num_iter+1), descent(0,0,0.001,10)[0], label = "alpha: 0.001 w0")
    # plt.plot(range(1,num_iter+1), descent(0,0,0.001,10)[1], label = "alpha: 0.001 w1")

    # plt.plot(range(1,num_iter+1), descent(0,0,0.03,10)[0], label = "alpha: 0.03 w0")
    # plt.plot(range(1,num_iter+1), descent(0,0,0.03,10)[1], label = "alpha: 0.03 w1")
    # plt.legend()
    # plt.xlabel("Number of Iterations")
    # plt.ylabel("w0 and w1 Value")
    # plt.show()
    descent(0,0,0.03,1000)
main()