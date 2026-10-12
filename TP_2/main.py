from model import OpinionModel
from visualization import (
    plot_global_evolution,
    plot_individual_trajectories
)


# Paramètres du modèle
WIDTH = 10
HEIGHT = 10
ALPHA = 0.5
STEPS = 50


# Création et exécution du modèle
model = OpinionModel(
    width=WIDTH,
    height=HEIGHT,
    alpha=ALPHA,
    seed=42
)

for _ in range(STEPS):
    model.step()


# Récupération des données collectées
model_data = model.datacollector.get_model_vars_dataframe()
agent_data = model.datacollector.get_agent_vars_dataframe()


# Affichage des résultats
plot_global_evolution(model_data)
plot_individual_trajectories(agent_data)