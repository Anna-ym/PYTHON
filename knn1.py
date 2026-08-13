#write a py pgm to predict diabetes using knn classification
from sklearn.datasets import load_diabetes
from sklearn import neighbors
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
diabetes=load_diabetes()
X=diabetes.data
y=diabetes.target
print(diabetes.data.shape)
print(diabetes.target.shape)
print(diabetes.feature_names)
print(diabetes.target) #target values
print(diabetes.data[0]) #10 values ,0th row value, first sample features -0.2 to +0.2
knn=neighbors.KNeighborsClassifier(n_neighbors=3)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)
knn.fit(X_train,y_train)
y_pred=knn.predict(X_test)
print(y_pred)
print(y_test)
print(accuracy_score(y_test,y_pred)*100)