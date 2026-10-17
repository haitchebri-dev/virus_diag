from core.model import BaseModel

class LogisticRegression(BaseModel):
    def __init__(self):
        self.is_trained = False
        # On va simuler des "poids" appris par le modèle
        self.seuil_temperature = 0 

    def train(self, X, y):
        print("   [LogisticRegression] Entraînement en cours...")
        # Un vrai algorithme ajusterait des poids complexes.
        # Ici, on cherche juste une température moyenne de séparation.
        temp_infectes = [X[i][1] for i in range(len(y)) if y[i] == 1]
        temp_sains = [X[i][1] for i in range(len(y)) if y[i] == 0]
        
        if temp_infectes and temp_sains:
            moy_infectes = sum(temp_infectes) / len(temp_infectes)
            moy_sains = sum(temp_sains) / len(temp_sains)
            self.seuil_temperature = (moy_infectes + moy_sains) / 2
        
        self.is_trained = True
        print(f"   [LogisticRegression] Modèle entraîné (Seuil de temp : {self.seuil_temperature:.2f}°C)")

    def predict(self, patient_data):
        if not self.is_trained:
            raise Exception("Erreur : Le modèle n'est pas entraîné !")
            
        # patient_data est une liste : [age, temperature, cough, fatigue]
        temperature = patient_data[1]
        
        # On retourne une "probabilité" simulée (1.0 ou 0.0) basée sur le seuil
        if temperature >= self.seuil_temperature:
            return [1.0] # 100% de chance d'être infecté
        else:
            return [0.0] # 0% de chance (donc sain)