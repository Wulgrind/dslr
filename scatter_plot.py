import pandas as pd
import matplotlib.pyplot as plt
import sys 
import seaborn as sns

filePath = sys.argv[1]
data = pd.read_csv(filePath)

feature1 = data['Astronomy']
feature2 = data['Defense Against the Dark Arts']

plt.figure(figsize=(8, 6))
plt.scatter(feature1, feature2, c='blue', label='Comparison', alpha=0.5)
plt.title('Comparison between Astronomy and Defense against the Dark Arts')
plt.xlabel('Astronomy') 
plt.ylabel('Defense against the Dark Arts')
plt.show()