import pandas as pd
import matplotlib.pyplot as plt
import sys 
import seaborn as sns

filePath = sys.argv[1]
data = pd.read_csv(filePath)

sns.pairplot(data, vars=['Arithmancy', 'Astronomy', 'Herbology', 'Defense Against the Dark Arts', 'Divination', 'Muggle Studies', 'Ancient Runes', 'History of Magic', 'Transfiguration', 'Potions', 'Care of Magical Creatures', 'Charms', 'Flying'])
plt.show()