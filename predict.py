import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def predict_user_input(model):
    print("Now you can predict the price of a house using the model")
    print("Enter values as: area,bedrooms,age (separated by commas, multiple rows separated by space)")
    user_input = input()
    rows = user_input.split()
    ex = []
    for row in rows:
        values = [float(v) for v in row.split(',')]
        ex.append(values)

    features = np.array(ex)
    prices = model.predict(features)

    plt.scatter(prices, range(len(prices)), color='black')
    plt.xlabel("Predicted Prices")
    plt.ylabel("House Index")
    plt.title("Predicted Prices for User Input")
    plt.show()

    d = pd.DataFrame(features, columns=['Area', 'Bedrooms', 'Age'])
    d['Predicted Price'] = prices
    print(d)
