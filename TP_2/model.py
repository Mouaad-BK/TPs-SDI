import mesa
import numpy as np

from agent import CitizenAgent


class OpinionModel(mesa.Model):
    """Modèle simulant la formation de l'opinion publique sur une grille."""

    def __init__(self, width, height, alpha=0.2, seed=None):
        super().__init__(seed=seed)

        self.grid = mesa.space.MultiGrid(
            width,
            height,
            torus=True
        )

        self.alpha = alpha

        # Initialisation de la population :
        # un agent par case
        for _, (x, y) in self.grid.coord_iter():
            agent = CitizenAgent(self, self.alpha)
            self.grid.place_agent(agent, (x, y))

        self.datacollector = mesa.DataCollector(
            model_reporters={
                "Opinion Moyenne": lambda m: np.mean(
                    [a.opinion for a in m.agents]
                ),
                "Variance (Dispersion)": lambda m: np.var(
                    [a.opinion for a in m.agents]
                )
            },
            agent_reporters={
                "Opinion": "opinion"
            }
        )

    def step(self):
        self.datacollector.collect(self)

        self.agents.shuffle_do("step")