import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from utils.preprocessing import load_data
from core.logistic_regression import LogisticRegression
from core.neural_network import NeuralNetwork  # <-- On ajoute le nouveau modèle
from pipeline.trainer import Trainer
from pipeline.evaluator import Evaluator
from core.clinical_predictor import ClinicalPredictor
from app.api import get_patient_data

def main():
    # 1. Chargement des données
    csv_path = os.path.join("Data", "patient_data.csv") 
    try:
        X, y = load_data(csv_path)
        print(f"Données chargées avec succès : {len(X)} patients.\n")
    except FileNotFoundError:
        print(f"Erreur : Impossible de trouver le fichier {csv_path}")
        return

    # 2. On prépare le patient de test (le même pour tous les modèles)
    nouveau_patient = get_patient_data()
    print(f"Données du nouveau patient (Age, Temp, Toux, Fatigue) : {nouveau_patient}\n")

    # 3. On crée une liste avec tous nos modèles (C'est ça le Polymorphisme !)
    # La liste ne se soucie pas du type de modèle, tant qu'ils héritent de BaseModel
    modeles_a_tester = [
        LogisticRegression(),
        NeuralNetwork()
    ]

    # 4. On boucle sur chaque modèle
    for modele in modeles_a_tester:
        nom_modele = modele.__class__.__name__ # Récupère le nom de la classe (ex: "LogisticRegression")
        print(f"TEST AVEC LE MODÈLE : {nom_modele}")
        
        
        # --- Phase d'entraînement ---
        entraineur = Trainer(modele)
        entraineur.run_training(X, y)

        # --- Phase d'évaluation ---
        evaluateur = Evaluator(modele)
        evaluateur.evaluate(X, y)

        # --- Phase de prédiction ---
        # On injecte le modèle dans le ClinicalPredictor
        predicteur = ClinicalPredictor(model=modele)
        diagnostic = predicteur.diagnose(nouveau_patient)
        
        print(f"Diagnostic final : {diagnostic}\n")

if __name__ == "__main__":
    main()