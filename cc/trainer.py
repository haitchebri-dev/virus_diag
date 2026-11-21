from abc import ABC, abstractmethod

#interface
class ModelStrategy(ABC):
    @abstractmethod
    def train(self, X, y):
        pass

#Strategies
class LogisticStrategy(ModelStrategy):
    def train(self, X, y):
        model = LogisticModel()
        return model.train(X, y)

class SVMStrategy(ModelStrategy):
    def train(self, X, y):
        model = SVMModel()
        return model.train(X, y)

#contexyte
class ModelTrainer:
    def __init__(self, strategy: ModelStrategy):
        self.strategy = strategy

    def execute(self, dataset):
        return self.strategy.train(dataset.X, dataset.Y)

#appel
trainer = ModelTrainer(SVMStrategy())
trained_model = trainer.execute(d)

#amelioration
#mettre en place un systeme de logging
#mettre en place un systeme de monitoring
#mettre en place un systeme de telechargement des donnees
#mettre en place un systeme de telechargement des modeles
#mettre en place un systeme de telechargement des donnees