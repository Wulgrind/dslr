import sys
import pandas as pd
import numpy as np
import random


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

def gradient_descent(weights, X, y, learning_rate=0.01, num_iterations=1000):
    m = len(y)
    for iteration in range(num_iterations):
        gradients = [0] * len(weights)
        for i in range(m):
            x_biased = [1] + X[i]
            h = hypothesis(weights, x_biased)
            error = h - y[i]

            for j in range(len(weights)):
                gradients[j] += error * x_biased[j]
        for j in range(len(weights)):
            weights[j] -= (learning_rate / m) * gradients[j]
    return weights

def init_weigths(num_features):
    return [random.uniform(-0.01, 0.01) for _ in range(num_features + 1)]

def hypothesis(weights, x):
    z = sum([weights[i] * x[i] for i in range(len(weights))])
    return (sigmoid(z))

def cost_function(weights, X, y):
    m = len(y)
    total_cost = 0

    for i in range(m):
        x_biased = [1] + X[i]
        h = hypothesis(weights, x_biased)
        total_cost += -y[i] * np.log(h) - (1 - y[i]) * np.log(1 - h)
    
    return total_cost / m

def encode_label(y):
    unique_labels = list(set(y))
    label_mapping = {label : index for index, label in enumerate(unique_labels)}
    y_encoded = [label_mapping[label] for label in y]
    return y_encoded, label_mapping

def training(X, y , num_classes, learning_rate = 0.01, num_iterations = 10000):
    all_weights = []
    for class_label in range(num_classes):
        y_binary = [1 if label == class_label else 0 for label in y]

        weights = init_weigths(len(X[0]))

        weights_trained = gradient_descent(weights, X, y_binary)
        all_weights.append(weights_trained)
    
    return all_weights
    
if __name__ == '__main__':
    filePath = sys.argv[1]
    data = pd.read_csv(filePath)

    data = data.dropna(subset=['Defense Against the Dark Arts'])
    data = data.dropna(subset=['Charms'])
    data = data.dropna(subset=['Herbology'])
    data = data.dropna(subset=['Divination'])
    data = data.dropna(subset=['Muggle Studies'])

    X = np.array(data.values[:, [9, 17, 8, 10, 11]], dtype=float)
    X = normalize_features(X)
    y = data['Hogwarts House']
    y_num, school_dict = encode_label(y)

    weights = init_weigths(len(X[0]))
    cost = cost_function(weights, X, y_num)
    weights_trained = gradient_descent(weights, X, y_num)
    weights_all = training(X, y_num, len(school_dict))
    with open('weights.txt', 'w') as f:
        for i, weights in enumerate(weights_all):
            house = list(school_dict.keys())[list(school_dict.values()).index(i)]
            f.write(f"{house},{','.join(map(str, weights))}\n")