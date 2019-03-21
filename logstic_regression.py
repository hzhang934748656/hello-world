import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#data pre-processing
dataset = pd.read_csv("bank.csv",sep = ';',index_col = False)
print(dataset)
dataset = dataset.iloc[:,[0,1,2,3,4,5,6,7,8,11,12,13,14,15,16]]
dataset.to_csv("bank7.csv")
#Transfer the class parameter to the numerical parameters
F = pd.get_dummies(dataset,columns = ['job','marital','education','default','housing','loan','contact','poutcome'])
mask = []
for i in range(0,39):
    if i ==6:
        mask.append(False)
    else:
        mask.append(True)
X = F.iloc[:,mask].values

y_mapping = {'no':0,'yes':1 }
y = F['y'].map(y_mapping).values

#y = F.iloc[:, 6].values
df = pd.DataFrame(X)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.25,random_state = 0)


#Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

#Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, y_train)

#predicting the test set result
y_pred = classifier.predict(X_test)

#Making the confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)