class Trainer:
    def __init__(self, model):
        self.model = model

    def run_training(self, X, y):
        print("Démarrage du pipeline d'entraînement...")
        # Le Trainer délègue l'apprentissage au modèle lui-même
        self.model.train(X, y)
        print("Fin de l'entraînement.")