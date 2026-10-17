from utils.metrics import calculate_accuracy

class Evaluator:
    def __init__(self, model):
        self.model = model

    def evaluate(self, X_test, y_test):
        print("Évaluation du modèle en cours...")
        
        # 1. On demande au modèle de prédire sur les données de test
        predictions_proba = [self.model.predict(x)[0] for x in X_test]
        
        # 2. On convertit les probabilités (ex: 1.0) en classes (0 ou 1)
        predictions = [1 if p >= 0.5 else 0 for p in predictions_proba]
        
        # 3. On calcule la précision (accuracy)
        accuracy = calculate_accuracy(y_test, predictions)
        
        print(f"Précision du modèle : {accuracy * 100:.2f}%")
        return accuracy