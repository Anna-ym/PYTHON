from sklearn.datasets import load_diabetes
from sklearn import neighbors
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target

print(diabetes.data.shape)
print(diabetes.target.shape)
print(diabetes.feature_names)
print(diabetes.target)  # target values
print(diabetes.data[0])  # 10 values, 0th row value, first sample features

knn = neighbors.KNeighborsRegressor(n_neighbors=5)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
print(y_pred)
print(y_test)
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
#the average squared difference between the actual values and the values predicted by your model
print("R2 Score:", r2_score(y_test, y_pred))
#model's predictions explain the variance of the actual data compared to a simple baseline
