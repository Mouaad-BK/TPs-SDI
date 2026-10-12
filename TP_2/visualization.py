import matplotlib.pyplot as plt


def plot_global_evolution(model_data):
    fig, ax1 = plt.subplots(figsize=(10, 5))

    color = "tab:blue"

    ax1.set_xlabel("Ticks (Temps)")
    ax1.set_ylabel("Opinion Moyenne", color=color)

    ax1.plot(
        model_data.index,
        model_data["Opinion Moyenne"],
        color=color,
        label="Moyenne"
    )

    ax1.tick_params(axis="y", labelcolor=color)
    ax1.set_ylim(0, 1)

    ax2 = ax1.twinx()

    color = "tab:red"

    ax2.set_ylabel("Variance (Dispersion)", color=color)

    ax2.plot(
        model_data.index,
        model_data["Variance (Dispersion)"],
        color=color,
        linestyle="--",
        label="Variance"
    )

    ax2.tick_params(axis="y", labelcolor=color)

    plt.title(
        "Évolution globale de l'opinion "
        "(Moyenne et Dispersion)"
    )

    fig.tight_layout()
    plt.show()


def plot_individual_trajectories(agent_data):
    agent_opinions = agent_data.unstack(level=1)["Opinion"]

    sample_agents = agent_opinions.columns[:20]

    plt.figure(figsize=(10, 5))

    for agent_id in sample_agents:
        plt.plot(
            agent_opinions.index,
            agent_opinions[agent_id],
            alpha=0.6
        )

    plt.title(
        "Trajectoires des opinions individuelles "
        "(Échantillon de 20 agents)"
    )

    plt.xlabel("Ticks (Temps)")
    plt.ylabel("Opinion [0, 1]")
    plt.ylim(0, 1)

    plt.show()