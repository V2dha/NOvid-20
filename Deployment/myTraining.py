import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pickle

def data_split(data,ratio):
    np.random.seed(42)
    shuffled = np.random.permutation(len(data))
    test_set_size = int(len(data) * ratio)
    test_indices = shuffled[:test_set_size]
    train_indices = shuffled[test_set_size:]
    return data.iloc[train_indices] , data.iloc[test_indices]


if __name__ == "__main__":

    # Read the data
    df = pd.read_csv('data.csv')
    x = df[['Fever','Body Pain','AGE','Runny Nose','Diff Breath']]
    y = df[['Infection Prob']]
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.4)
    
    
    clf = LogisticRegression()
    clf.fit(x_train,y_train)

    # open a file, where you want to store the data
    file = open('model.pkl', 'wb')

    # dump information to that file
    pickle.dump(clf, file)
    file.close()




