class ClinicalPredictor:
    def __init__(self, model):
        # Recevoir un modèle déjà entraîné
        self.model = model
        
    def diagnose(self, patient_data):
        # On suppose que predict() retourne une probabilité (ex: 0.8)
        prediction = self.model.predict(patient_data)[0]
        
        # Retourner "Infecté" si prédiction >= 0.5, sinon "Sain"
        if prediction >= 0.5:
            return "Infecté"
        else:
            return "Sain"



#2. Le concept de POO  
#Le concept est le Polymorphisme (et plus précisément en Python, le Duck Typing). 
#Explication : Grâce à ce concept, ClinicalPredictor n'a pas besoin de savoir si le modèle est une régression logistique, 
#un réseau de neurones, etc. Il s'en fiche du type de l'objet. 
#La seule condition est que l'objet passé en paramètre possède une méthode predict(). 
#Cela permet d'utiliser n'importe quel modèle IA de manière interchangeable.

#3. Pourquoi séparer la prédiction de l'entraînement ?

#Il est important de les séparer pour plusieurs raisons :

#Séparation des responsabilités (Principe de responsabilité unique) : Le Trainer a pour seule tâche d'apprendre à partir des données. Le ClinicalPredictor a pour seule tâche de faire des diagnostics rapides. Mélanger les deux rend le code complexe et difficile à maintenir.
#Ressources et Performance : L'entraînement est très lourd (calculs, temps, GPU). La prédiction doit être légère et instantanée. On ne veut pas recharger tout le processus d'entraînement juste pour faire une prédiction.
#Maintenance et Mise à jour : Si vous améliorez votre modèle (nouvel entraînement), vous n'avez pas besoin de modifier le code du ClinicalPredictor. Vous lui donnez simplement le nouveau modèle entraîné.
#Sécurité / Déploiement : En production (dans un hôpital par exemple), on déploie uniquement le ClinicalPredictor avec le modèle sauvegardé. On n'a pas besoin (et on ne veut pas) y installer le code complexe d'entraînement ni les données brutes d'entraînement.
