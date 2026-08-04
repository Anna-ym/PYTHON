from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

iris=load_iris()
X=iris.data
y=iris.target

#to split the dataset into training and testing sets
#X_train=used for training purpose,y_train=labels,X_test=unseen data for testing,y_test=output for the unseen data,y_test=actual value
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)      #random_state=controls the randomness of splitting data.ensures you get the same result every time you run the code

#gaussian for medical classification idea is base theorem
#gaussian model creation and train the model
model=GaussianNB()

#train the model:for training purpose fit()
model.fit(X_train,y_train)

#prediction on test data or unseen data
y_pred=model.predict(X_test)

print(y_pred)
print(y_test)
print(accuracy_score(y_test,y_pred))    #checking both are same (1)
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
