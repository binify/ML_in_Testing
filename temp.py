df = pd.read_csv('train10K.csv')
y_approved = df[['label']].copy()
y_approved = y_approved.values.reshape(-1).tolist()

df1 = df[df['approved']==0]
y_amount = df[['label']].copy()
y_amount = y_amount.values.reshape(-1).tolist()

X = df.drop(["approved","amount","label"],axis=1)
X = X.values.astype(np.float32)

X_approved = df1.drop(["approved","amount","label"],axis=1)
X_approved = X_approved.values.astype(np.float32)

train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

y_train = train_set[["approved"]].copy()
X_train = train_set.drop(["approved","amount","label"],axis=1)
X_train = X_train.values.astype(np.float32)
y_train = y_train.values.reshape(-1)

y_test = test_set[["approved"]].copy()
y_test = y_test.values.reshape(-1)
X_test = test_set.drop(["approved","amount","label"],axis=1)
X_test = X_test.values.astype(np.float32)


y_approved_bug = [credit_approval_bug(*s.astype(np.int64))[0] for s in X]
# approved_rate = (1 - sum(1 for x,y in zip(approved_bug,y_approved.tolist()) if x == y) / len(approved_bug))*100
approved_rate = (1 - accuracy_score(y_approved_bug,y_approved))*100

y_amount_bug = [credit_approval_bug(*s.astype(np.int64))[1] for s in X]
rmse = sqrt(mean_squared_error(y_amount,y_amount_bug))

print(y_approved_bug[:20])
print(y_approved[:20])
