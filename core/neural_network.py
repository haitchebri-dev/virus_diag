from core.model import BaseModel

class NeuralNetwork(BaseModel):
    def __init__(self):
        self.is_trained = False

    def train(self, X, y):
        print("   [NeuralNetwork] Entraînement (simulation)...")
        self.is_trained = True

    def predict(self, patient_data):
        # Simulation d'une prédiction (retourne 0.6 au hasard pour tester)
        import random
        return [random.uniform(0.0, 1.0)]