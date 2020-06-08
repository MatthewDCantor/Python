import numpy as np
import matplotlib.pyplot as plt
"""
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()
"""

def load_data(data_file):
    f = open(data_file , "r")
    X_dat = []
    Y_dat = []

    for data in f:
        X_dat.append(list(map(float, data.split( ))))

    for i in range(len(X_dat)):
        X_dat[i].insert(0,1.0)
        Y_dat.append(X_dat[i][-1])
        del X_dat[i][-1]

    X = np.matrix(X_dat)
    Y = np.matrix(Y_dat).transpose()


    return X,Y

def train(X,Y):

    X_T = X.transpose()
    X_T_X_I = (X_T.dot(X)).getI()
    w = X_T_X_I.dot(X_T).dot(Y)



    return w

def SSE(X,Y,w):

    Z = Y - X.dot(w)

    return Z.transpose().dot(Z)[0,0]

"""Training the data to find weights for test data"""

X,Y = load_data("/Users/matthewcantor/Documents/Python/Linear_reg/Data/housing_train.txt")
w = train(X,Y)


print "SSE for training data:", SSE(X,Y,w)

X_2,Y_2 = load_data("/Users/matthewcantor/Documents/Python/Linear_reg/Data/housing_test.txt")
w_2 = train(X_2,Y_2)
print "SSE for test data:", SSE(X_2,Y_2,w_2)
