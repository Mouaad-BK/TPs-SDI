
# Agentic AI avec LangChain

## Présentation

Ce notebook est consacré à la découverte et à l'implémentation des agents d'IA avec **LangChain**. Il présente les principales fonctionnalités permettant de créer des agents capables d'utiliser des outils, de conserver une mémoire, d'adapter leur comportement et d'appliquer des mécanismes de sécurité.

## Objectifs

- Créer un agent simple avec LangChain.
- Configurer et sélectionner dynamiquement un modèle.
- Gérer la mémoire des conversations.
- Ajouter des outils aux agents.
- Utiliser un moteur de recherche et un interpréteur Python.
- Personnaliser le comportement des agents avec des middlewares.
- Générer des réponses structurées.
- Intégrer un système RAG comme outil d'un agent.
- Mettre en place des garde-fous et une validation humaine.

## Technologies utilisées

- **Python** : langage de programmation.
- **LangChain** : création et gestion des agents.
- **LangGraph** : gestion de l'état et de la mémoire des agents.
- **Ollama** : accès aux modèles de langage.
- **Chroma / InMemoryVectorStore** : stockage et recherche vectorielle.
- **PostgreSQL** : persistance de la mémoire des conversations.
- **Tavily / DuckDuckGo** : recherche sur le Web.
- **Python REPL** : exécution de code Python.
- **Pydantic** : définition des réponses structurées.

## Contenu du notebook

### 1. Création d'un agent simple
- Initialisation d'un modèle avec `ChatOllama`.
- Création d'un agent avec `create_agent`.
- Interaction avec l'agent à travers des messages.

### 2. Configuration et sélection dynamique du modèle
- Configuration du modèle et activation du mode debug.
- Sélection dynamique du modèle selon le contexte d'exécution avec `@wrap_model_call`.

### 3. Mémoire de l'agent
- Utilisation de `InMemorySaver` pour conserver l'historique des conversations.
- Utilisation de `PostgresSaver` pour assurer une persistance dans PostgreSQL.
- Gestion des conversations avec `thread_id`.

### 4. Utilisation des outils (Tools)
- Création d'outils personnalisés avec `@tool`.
- Intégration de la recherche Web avec DuckDuckGo et Tavily.
- Utilisation d'outils pour récupérer des informations.
- Appel des outils par l'agent selon la demande.

### 5. Exécution de code Python
- Utilisation de `PythonREPL` et `PythonREPLTool`.
- Création d'un agent capable de générer et d'exécuter du code Python.
- Utilisation de bibliothèques comme SymPy ou NumPy pour effectuer des calculs.

### 6. Gestion des erreurs des outils
- Création d'un middleware avec `@wrap_tool_call`.
- Interception des erreurs pendant l'exécution des outils.

### 7. Contrôle du System Prompt
- Utilisation de `@dynamic_prompt`.
- Adaptation des instructions selon le rôle de l'utilisateur (expert ou débutant).

### 8. Réponses structurées
- Définition d'un format de sortie avec Pydantic.
- Utilisation de `ToolStrategy` pour extraire des informations structurées.

### 9. Middleware personnalisé
- Création d'un middleware avec `AgentMiddleware`.
- Utilisation des hooks :
  - `before_agent`
  - `before_model`
  - `after_model`
  - `after_agent`

### 10. RAG comme outil d'un agent
- Création d'un magasin vectoriel avec `InMemoryVectorStore`.
- Génération des embeddings avec `OpenAIEmbeddings`.
- Recherche de similarité dans une base de connaissances.
- Création d'un outil de récupération avec `create_retriever_tool`.
- Intégration de cet outil dans un agent.

### 11. Guardrails (Garde-fous)
- Présentation des garde-fous déterministes et basés sur des modèles.
- Détection et traitement des informations personnelles (PII) avec `PIIMiddleware`.
- Stratégies de protection : `redact`, `mask`, `hash` et `block`.
- Intervention humaine avant l'exécution d'opérations sensibles avec `HumanInTheLoopMiddleware`.
- Création de garde-fous personnalisés avant et après l'exécution de l'agent.

### 12. LangGraph
- Section introduite dans le notebook.

## Installation

Les dépendances principales peuvent être installées avec `uv` :

```bash
uv add langchain langchain-ollama langgraph langgraph-checkpoint-postgres "psycopg[binary,pool]" python-dotenv ddgs langchain-tavily langchain-experimental sympy
```

La partie RAG utilise également `langchain-openai` :

```bash
uv add langchain-openai
```

## Configuration

Créer un fichier `.env` à la racine du projet :

```env
OLLAMA_API_KEY=your_ollama_api_key
TAVILY_API_KEY=your_tavily_api_key
OPENROUTER_API_KEY=your_openrouter_api_key

PGUSER=your_postgres_user
PGPASSWORD=your_postgres_password
```

- `OLLAMA_API_KEY` : accès aux modèles Ollama Cloud.
- `TAVILY_API_KEY` : nécessaire pour les recherches avec Tavily.
- `OPENROUTER_API_KEY` : nécessaire pour les embeddings de la partie RAG.
- `PGUSER` et `PGPASSWORD` : identifiants PostgreSQL pour la mémoire persistante.

Les cellules utilisant DuckDuckGo ne nécessitent pas de clé API.

## Exécution

Ouvrir le notebook `AI_Agentic.ipynb` dans Jupyter Notebook ou VS Code, configurer les variables d'environnement nécessaires, puis exécuter les cellules dans l'ordre.
