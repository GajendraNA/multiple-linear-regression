from sklearn.metrics import r2_score

def evaluate_model(Y_test, Y_pred):
    r2 = r2_score(Y_test, Y_pred)
    return r2
