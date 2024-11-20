import sys
import pandas as pd
import numpy as np
import csv
from sklearn.metrics import accuracy_score

def normalize_features(X):
    X_normalized = []
    for i in range(len(X[0])):
        col = [row[i] for row in X]
        min_val = min(col)
        max_val = max(col)
        normalized_col = [(x - min_val) / (max_val - min_val) for x in col]
        for j in range(len(X)):
            if i == 0:
                X_normalized.append([normalized_col[j]])
            else :
                X_normalized[j].append(normalized_col[j])
    return X_normalized

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def hypothesis(weights, x):
    z = sum([weights[i] * x[i] for i in range(len(weights))])
    return (sigmoid(z))

def predict(weights, X):
    predictions = []

    for x in X:
        x_biased = [1] + x
        probabilities = [hypothesis(w, x_biased) for w in weights]
        predicted_class = probabilities.index(max(probabilities))
        predictions.append(predicted_class)
    return predictions

if __name__ == '__main__':
    try :
        filePath = sys.argv[1]
        data = pd.read_csv(filePath)
        data = data.fillna(method='ffill')

        X = np.array(data.values[:, [9, 17, 8, 10, 11]], dtype=float)
        X = normalize_features(X)
        weights = []
        houses = []
        with open('weights.txt', 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                house = parts[0]
                houses.append(house)
                weights.append([float(w) for w in parts[1:]])
        predictions = predict(weights, X)

        with open('houses.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            i = 0
            writer.writerow(['Index', 'Hogwarts House'])
            for prediction in predictions :
                house_name = houses[prediction]
                writer.writerow([i, house_name])
                i += 1
        #test_data = pd.read_csv('dataset_truth.csv')
        #predicted_data = pd.read_csv('houses.csv')
        #true_labels = test_data['Hogwarts House']
        #predicted_labels = predicted_data['Hogwarts House']
        #accuracy = accuracy_score(true_labels, predicted_labels)
        #print(f"L'accuracy de votre modèle est : {accuracy * 100:.2f}%")
    except :
        print("You must provide a valid csv file as the first argument")