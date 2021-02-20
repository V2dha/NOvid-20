import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle


if __name__ == "__main__":

    # Read the data
    df = pd.read_csv('data.csv')
    sample=pd.DataFrame(df)
    sample.Breathing_Problem.replace(('Yes', 'No'), (1, 0), inplace=True) 
    sample.Fever.replace(('Yes', 'No'), (1, 0), inplace=True) 
    sample.Dry_Cough.replace(('Yes', 'No'), (1, 0), inplace=True) 
    sample.Sore_throat.replace(('Yes', 'No'), (1, 0), inplace=True) 
    sample.Running_Nose.replace(('Yes', 'No'), (1, 0), inplace=True) 
    sample.Asthma.replace(('Yes', 'No'), (1, 0), inplace=True)
    sample.Chronic_Lung_Disease.replace(('Yes', 'No'), (1, 0), inplace=True) 
    sample.Headache.replace(('Yes', 'No'), (1, 0), inplace=True) 
    sample.Heart_Disease.replace(('Yes', 'No'), (1, 0), inplace=True) 
    sample.Diabetes.replace(('Yes', 'No'), (1, 0), inplace=True) 
    sample.Hyper_Tension.replace(('Yes', 'No'), (1, 0), inplace=True) 
    sample.Fatigue.replace(('Yes', 'No'), (1, 0), inplace=True) 
    sample.Gastrointestinal.replace(('Yes', 'No'), (1, 0), inplace=True) 
    sample.Abroad_travel.replace(('Yes', 'No'), (1, 0), inplace=True) 
    sample.Contact_with_COVID_Patient.replace(('Yes', 'No'), (1, 0), inplace=True) 
    sample.Attended_Large_Gathering.replace(('Yes', 'No'), (1, 0), inplace=True) 
    sample.Visited_Public_Exposed_Places.replace(('Yes', 'No'), (1, 0), inplace=True) 
    sample.Family_working_in_Public_Exposed_Places.replace(('Yes', 'No'), (1, 0), inplace=True) 
    sample.Wearing_Masks.replace(('Yes', 'No'), (1, 0), inplace=True) 
    sample.Sanitization_from_Market.replace(('Yes', 'No'), (1, 0), inplace=True)  
    sample.COVID.replace(('Yes', 'No'), (1, 0), inplace=True) 

    x=df[['Breathing_Problem','Fever','Dry_Cough','Sore_throat','Running_Nose','Asthma','Chronic_Lung_Disease',
    'Headache','Heart_Disease', 'Diabetes','Hyper_Tension','Fatigue','Gastrointestinal','Abroad_travel',
    'Contact_with_COVID_Patient','Attended_Large_Gathering','Visited_Public_Exposed_Places',
    'Family_working_in_Public_Exposed_Places','Wearing_Masks','Sanitization_from_Market']].to_numpy()
    y=df[['COVID']].to_numpy()

    x_train,x_test,y_train,y_test=train_test_split(x, y, test_size = 0.2,random_state=2)
    
    
    clf = RandomForestClassifier()
    clf.fit(x_train,y_train.ravel())

    # open a file, where you want to store the data
    file = open('model.pkl', 'wb')

    # dump information to that file
    pickle.dump(clf, file)
    file.close()




