import pandas as pd

# Charger le fichier CSV en DataFrame pandas
df = pd.read_csv('fichier.csv')

# Garder seulement les colonnes Period, Data_value et Series_title_2
df = df[['Period', 'Data_value', 'Series_title_2']]

# Supprimer les lignes contenant une cellule vide
df = df.dropna()

# Filtrer les résultats pour garder seulement ceux avec Credit, Debit et Services dans la colonne Series_title_2
df = df[df['Series_title_2'].isin(['Credit', 'Debit', 'Services'])]

# Ajouter une colonne ID auto-incrémenté
df['ID'] = range(1, len(df) + 1)

# Recréer un fichier result.csv qui contient le nouveau fichier nettoyé
df.to_csv('result.csv', index=False)
