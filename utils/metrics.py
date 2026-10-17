def calculate_accuracy(y_true, y_pred):
    """
    Calcule le pourcentage de bonnes prédictions.
    """
    if len(y_true) == 0:
        return 0.0
    
    correct = 0
    for i in range(len(y_true)):
        if y_true[i] == y_pred[i]:
            correct += 1
            
    return correct / len(y_true)