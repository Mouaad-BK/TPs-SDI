import mesa
import numpy as np


class CitizenAgent(mesa.Agent):
    """Un individu ayant une opinion qui évolue selon ses voisins."""

    def __init__(self, model, alpha):
        super().__init__(model)

        self.opinion = self.model.random.random()
        self.alpha = alpha

    def step(self):
        neighbors = self.model.grid.get_neighbors(
            self.pos,
            moore=True,
            include_center=False
        )

        if len(neighbors) > 0:
            mean_opinion = np.mean(
                [neighbor.opinion for neighbor in neighbors]
            )

            self.opinion = (
                self.opinion
                + self.alpha * (mean_opinion - self.opinion)
            )