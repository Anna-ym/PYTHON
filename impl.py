#implement gaussian using the public dataset load_breast_cancer
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
cancer=load_breast_cancer()
X=cancer.data
y=cancer.target
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.01,random_state=42)
model=GaussianNB()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
print(y_pred)               #predicted values
print(y_test)               #actual values
print("Accuracy: ",accuracy_score(y_test,y_pred))    #checking both are same (1)
print("Confusion Matrix: ",confusion_matrix(y_test,y_pred))
print("Classification Report: ",classification_report(y_test,y_pred))
sample=X_test[0].reshape(1,-1)  #0th row of test data and reshaping it 
sample2=X_test[2].reshape(1,-1)
sample3=X_test[1].reshape(1,-1)
pred=model.predict(sample)
print("Predicted classes: ",cancer.target_names[pred])
pred2=model.predict(sample2)
print("Predicted classes: ",cancer.target_names[pred2])
pred3=model.predict(sample3)
print("Predicted classes: ",cancer.target_names[pred3])