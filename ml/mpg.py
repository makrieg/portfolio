from datasets import load_dataset
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

dataset = load_dataset("scikit-learn/auto-mpg")
traindata = dataset["train"]

data_dict = traindata.to_dict()

print(data_dict.keys())

y = data_dict["mpg"]

print(data_dict["cylinders"][:5])

x= []

num_rows = len(y)
for i in range(num_rows):
    row = [
        data_dict["cylinders"][i],
        data_dict["displacement"][i],
        int(data_dict["horsepower"][i] if data_dict["horsepower"][i] != "?" else 0),
        data_dict["weight"][i],
        data_dict["acceleration"][i],
        data_dict["model year"][i],
        data_dict["origin"][i]
    ]

    print(f'Row {i}: {row}')
    x.append(row)

    weight = data_dict["weight"]
    plt.figure(figsize=(7,4))
    plt.scatter(weight, y, alpha=0.5)
    plt.title("Weight vs MPG")
    plt.xlabel("Weight")
    plt.ylabel("MPG")
    plt.tight_layout()
    plt.show()

    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42)

    model = LinearRegression()
    model.fit(X=x_train, y=y_train)

    y_pred = model.predict(X=x_test)
    plt.figure(figsize=(6,6))
    plt.scatter(y_test, y_pred, alpha=0.5)
    plt.title("Actual vs Predicted MPG")
    plt.xlabel("Actual MPG")
    plt.ylabel("Predicted MPG")
    plt.tight_layout()
    plt.show()

    print("\nSample Predictions:")
    for i in range(10):
        print(f"Actual: {y_test[i]:.2f}, Predicted: {y_pred[i]:.2f}")
        
