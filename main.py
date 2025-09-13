from data_loader import check_csv, display_and_select_csv, load_data
from model import build_model
from train import split_data, train_model
from evaluate import evaluate_model
from predict import predict_user_input
from visualize import graph_results, graph_3d

def welcome():
    print("Welcome to the Multiple Linear Regression Project!")
    print("Press enter key to proceed.")
    input()

def main():
    welcome()
    try:
        csv_files = check_csv()
        if csv_files == 'No csv file found in the directory':
            raise FileNotFoundError('No csv file in the directory')
        csv_file = display_and_select_csv(csv_files)
        print(csv_file, "is selected")
        print("Reading csv file...")
        dataset = load_data(csv_file)
        print("Dataset created successfully")

        X = dataset.iloc[:, :-1].values
        Y = dataset.iloc[:, -1].values

        s = float(input("Enter test size in decimal (0-1): "))
        X_train, X_test, Y_train, Y_test = split_data(X, Y, test_size=s)

        print("Model creation is in progress...")
        model = build_model()
        model = train_model(model, X_train, Y_train)
        print("Model created successfully")

        print("Press Enter to predict test data in trained model")
        input()
        Y_pred = model.predict(X_test)

        for i in range(len(X_test)):
            print(f"For input {X_test[i]} the predicted output is {Y_pred[i]} and actual output is {Y_test[i]}")

        print("Press Enter key to see results in graphical format")
        input()
        graph_results(Y_test, Y_pred)
        graph_3d(X_test, Y_test, Y_pred)

        r2 = evaluate_model(Y_test, Y_pred)
        print("Our model is %2.2f%% accurate" % (r2 * 100))

        predict_user_input(model)

    except FileNotFoundError:
        print('No csv file found in the directory. Please add a csv file and try again.')
        print('Press Enter to exit.')
        input()
        exit()

if __name__ == "__main__":
    main()
    input()
