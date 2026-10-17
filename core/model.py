from abc import ABC, abstractmethod

class BaseModel(ABC):
    @abstractmethod
    def train(self, X, y):
        """Toute classe héritant de BaseModel doit implémenter cette méthode."""
        pass

    @abstractmethod
    def predict(self, patient_data):
        """Toute classe héritant de BaseModel doit implémenter cette méthode."""
        pass