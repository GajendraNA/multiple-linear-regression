from sklearn.model_selection import train_test_split

def split_data(X, Y, test_size=0.2, random_state=0):
    return train_test_split(X, Y, test_size=test_size, random_state=random_state)

def train_model(model, X_train, Y_train):
    model.fit(X_train, Y_train)
    return model
