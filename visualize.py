import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def graph_results(Y_test, Y_pred):
    plt.scatter(Y_test, Y_pred, color='blue')
    plt.plot([Y_test.min(), Y_test.max()], [Y_test.min(), Y_test.max()], 'r--')
    plt.xlabel("Actual Prices")
    plt.ylabel("Predicted Prices")
    plt.title("Actual vs Predicted Prices")
    plt.legend()
    plt.show()

def graph_3d(X_test, Y_test, Y_pred):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(X_test[:, 0], X_test[:, 1], Y_test, c='red', label='Actual')
    ax.scatter(X_test[:, 0], X_test[:, 1], Y_pred, c='blue', marker='^', label='Predicted')
    ax.set_xlabel("Area")
    ax.set_ylabel("Bedrooms")
    ax.set_zlabel("Price")
    plt.title("3D View: Area vs Bedrooms vs Price")
    ax.legend()
    plt.show()
