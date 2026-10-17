import csv

def load_data(filepath):
    """
    Lit le fichier CSV et sépare les features (X) de la cible (y).
    """
    X = [] # Les données (age, temp, etc.)
    y = [] # La cible (0 ou 1)
    
    with open(filepath, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # On extrait les 4 premières colonnes
            features = [
                float(row['age']), 
                float(row['temperature']), 
                int(row['cough']), 
                int(row['fatigue'])
            ]
            X.append(features)
            # On extrait la dernière colonne (infected)
            y.append(int(row['infected']))
            
    return X, y

def normalize_data(X):
    """
    (Optionnel pour plus tard) Normalise les données pour le réseau de neurones.
    """
    return X # On laisse tel quel pour l'instant