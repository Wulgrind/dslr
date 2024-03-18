import pandas as pd
import matplotlib.pyplot as plt
import sys 
import seaborn as sns

filePath = sys.argv[1]
data = pd.read_csv(filePath)

feature1 = data['Astronomy']
feature2 = data['Defense Against the Dark Arts']

# Créer le scatter plot avec différentes couleurs pour chaque caractéristique
plt.figure(figsize=(8, 6))
plt.scatter(feature1, feature2, c='blue', label='Feature 1', alpha=0.5)
plt.title('Comparaison entre Feature 1 et Feature 2')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.grid(True)
plt.show()

#sns.pairplot(data, vars=['Arithmancy', 'Astronomy', 'Herbology', 'Defense Against the Dark Arts', 'Divination', 'Muggle Studies', 'Ancient Runes', 'History of Magic', 'Transfiguration', 'Potions', 'Care of Magical Creatures', 'Charms', 'Flying'])
#plt.show()