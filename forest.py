import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.preprocessing import StandardScaler

dataset = pd.read_csv('creditcard.csv')


X = dataset.iloc[:, 0:30].values
y = dataset.iloc[:, 30].values

print("Enter the testing size")
inp = -1.0

while(inp <= 0 or inp >= 100.0 or inp == 1.0):
    inp = float(input("the size must be positive and less than 100: "))
    if (inp > 1.0 and inp/100.0 < 1.0):
        print("assuming percentages")
        inp /= 100.0

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=inp, random_state=0)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

regressor = RandomForestClassifier(n_estimators=100, random_state=0)
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)


print(classification_report(y_test,y_pred))
print("Accuracy: ")
print(accuracy_score(y_test, y_pred))


