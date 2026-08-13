import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import neighbors 
iris=load_iris()
X=iris.data
y=iris.target
knn=neighbors.KNeighborsClassifier(n_neighbors=3)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)
knn.fit(X_train,y_train)
y_pred=knn.predict(X_test)
print(y_pred)
print(y_test)
print("Accuracy Score: ",accuracy_score(y_test,y_pred))
print(iris.target_names[y_pred])
new_sample=np.array([[5.1,3.5,1.4,0.2]])
for sample in [new_sample]:
    pred = knn.predict([sample])[0]
    print("Predicted Class: ",iris.target_names[pred])
prediction=knn.predict(new_sample)
print("predicted class: ",prediction)
print(iris.target_names[prediction])
