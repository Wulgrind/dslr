import pandas as pd
import matplotlib.pyplot as plt
import sys 
import seaborn as sns

# Charger les données
filePath = sys.argv[1]
data = pd.read_csv(filePath)

# Dictionnaire de correspondance entre les noms de matières et les acronymes
acronyms = {
    'Arithmancy': 'ARI',
    'Astronomy': 'AST',
    'Herbology': 'HER',
    'Defense Against the Dark Arts': 'DADA',
    'Divination': 'DIV',
    'Muggle Studies': 'MS',
    'Ancient Runes': 'AR',
    'History of Magic': 'HOM',
    'Transfiguration': 'TRN',
    'Potions': 'POT',
    'Care of Magical Creatures': 'CMC',
    'Charms': 'CHA',
    'Flying': 'FLY'
}

data = data.rename(columns=acronyms)
pairplot = sns.pairplot(data, vars=list(acronyms.values()))
pairplot.fig.set_size_inches(10, 10)

for ax in pairplot.axes.flatten():
    ax.set_xticks([])  
    ax.set_yticks([])  

plt.show()
