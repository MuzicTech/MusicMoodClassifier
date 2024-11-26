from sklearn.model_selection import train_test_split

X = features_df.drop(columns=["mood"])
y = features_df["mood"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
