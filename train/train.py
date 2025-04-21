import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

df_org = pd.read_csv('data/water_potability.csv')

# Handle NAs
df = df_org.dropna()

# Train and test sets
X = df.drop('Potability',axis=1)
Y = df['Potability']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=100)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.fit_transform(X_test)

# Input variables
print(X.columns, X_train.shape)

# Train the model
Model_RF = RandomForestClassifier()
Model_RF.fit(X_train,Y_train)

# Prediction
Y_pred = Model_RF.predict(X_test)

# Model performance
print(f'Accuracy of the Random Forest model: {round(accuracy_score(Y_test,Y_pred)*100,2)}%')
print(confusion_matrix(Y_test, Y_pred))
print(classification_report(Y_test, Y_pred))

# Save the model and the scaler
joblib.dump(Model_RF, "../src/model.joblib")
joblib.dump(scaler, "../src/scaler.joblib")
