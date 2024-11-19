import sys
import matplotlib.pyplot as plt

def calculate_variance(scores):
    mean = sum(scores) / len(scores)
    sum_squared_diff = sum((x - mean) ** 2 for x in scores)
    variance = sum_squared_diff / len(scores)

    return variance

def plot_histogram(data, xlabel, ylabel, title):
    plt.hist(data, bins=10, alpha=0.7, color='blue', edgecolor='black')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()

if __name__ == "__main__":
    filePath = sys.argv[1]
    data = []
    with open(filePath, 'r') as file:
        lines = file.readlines()
        features = lines[0].split(',')[6:] # remove les elements non numeriques
        features[12] = features[12][:-1] #remove le \n
        lines.pop(0)
        for line in lines :
            newLine = []
            values = line.split(',')[6:]
            values[12] = values[12][:-1]
            for val in values:
                if len(val) > 0 :
                    newLine.append(float(val))
            data.append(newLine)
        courses = dict()
        i = 0
        while i < len(features):
            courses[features[i]] = calculate_variance(data[i])
            i += 1
        plt.bar(courses.keys(), courses.values(), color='blue', alpha=0.7)
        plt.xlabel('Courses')
        plt.ylabel('Variance')
        plt.title('Comparaison des variances selon les cours')
        plt.show() 
        
