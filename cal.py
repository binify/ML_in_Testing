import pandas as pd
import numpy as np

from app import credit_approval, credit_approval_bug, label, compare
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error, confusion_matrix
from keras.models import model_from_json
from keras.utils import to_categorical

json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
# load weights into new model
model.load_weights("model.h5")
print("Loaded model from disk")

df = pd.read_csv('test5K.csv')

y = df[["label"]].copy()
y = y.values.reshape(-1)

X = df.drop(["approved", "amount", "label"], axis=1)
X = X.values.astype(np.float32)

y_pred = model.predict(X)
y_pred = [np.argmax(i) for i in y_pred]

y_amount_bug = [credit_approval_bug(*s.astype(np.int64))[1] for s in X]
y_bug = [label(i) for i in y_amount_bug]

bug_real = [i == j for i, j in zip(y, y_bug)]

bug_pred = [compare(i, j, 0.2, 0.8) for i, j in zip(y_pred, y_bug)]

print(confusion_matrix(bug_pred, bug_real))
#print("{0:.2f} {1:.2f}".format(approved_rate,rmse))
