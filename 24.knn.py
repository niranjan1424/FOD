import numpy as np
from sklearn.neighbors import KNeighborsClassifier

def get_input_features():
    # Get input features from the user
    num_features = int(input("Enter the number of features: "))
    features = []
    for i in range(num_features):
        feature = float(input(f"Enter feature {i + 1}: "))
        features.append(feature)
    return np.array(features).reshape(1, -1)

def get_k_value():
    # Get the value of k from the user
    k = int(input("Enter the value of k (number of neighbors): "))
    return k

def main():
    # Sample labeled dataset (replace this with your actual dataset)
    data = np.array([[1, 2, 1],
                     [2, 3, 1],
                     [3, 1, 0],
                     [4, 2, 0]])

    X = data[:, :-1]  # Features
    y = data[:, -1]   # Labels

    # Create KNN classifier
    knn = KNeighborsClassifier()
    # Fit the classifier on the data
    knn.fit(X, y)

    # Get input features for the new patient
    new_patient_features = get_input_features()

    # Get the value of k from the user
    k = get_k_value()

    # Predict the label for the new patient
    prediction = knn.predict(new_patient_features)

    if prediction[0] == 1:
        print("The patient has the medical condition.")
    else:
        print("The patient does not have the medical condition.")

if __name__ == "__main__":
    main()

