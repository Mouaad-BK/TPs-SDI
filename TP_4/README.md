
# TP4 — Implémentation d’un système RAG

## 1. Objectif du TP

L’objectif de ce TP est de construire un système RAG (*Retrieval-Augmented Generation*) capable de répondre à des questions à partir d’un document fourni.

Le système recherche d’abord les passages pertinents dans le document, puis utilise un modèle de langage (LLM) pour générer une réponse fondée sur ces passages.

Le cas d’étude final consiste à utiliser un CV comme source documentaire et à poser la question :

**« Présente mon profil professionnel. »**

Le système doit présenter le profil à partir du CV, sans inventer d’informations absentes du document.

## 2. Technologies et modèles utilisés

- **Python** : langage de programmation.
- **Jupyter Notebook** : environnement de développement.
- **LangChain** : orchestration des différentes étapes du RAG.
- **PyPDFLoader** : chargement et extraction du texte du PDF.
- **RecursiveCharacterTextSplitter** : découpage du document en chunks.
- **HuggingFaceEmbeddings** : génération des embeddings.
- **BAAI/bge-m3** : modèle d’embeddings utilisé.
- **ChromaDB** : stockage vectoriel et recherche par similarité.
- **ChatOllama** : connexion au modèle de génération.
- **Gemma 4 31B** : LLM utilisé pour générer les réponses.
- **python-dotenv** : chargement des variables d’environnement.
- **uv** : gestion de l’environnement Python et des dépendances.

## 3. Fonctionnement du système RAG

Le pipeline est composé des étapes suivantes :

1. Chargement du document PDF.
2. Extraction du texte.
3. Découpage du texte en chunks.
4. Transformation des chunks en vecteurs avec le modèle d’embeddings.
5. Stockage des vecteurs dans ChromaDB.
6. Recherche des passages pertinents à partir de la question.
7. Construction du prompt avec le contexte récupéré.
8. Génération de la réponse par le LLM.
9. Évaluation de la fidélité de la réponse au contexte.

## 4. Préparation du document

Le document est chargé avec `PyPDFLoader`.

Le texte est ensuite découpé avec `RecursiveCharacterTextSplitter` selon les paramètres suivants :

- Taille d’un chunk : **300 tokens**.
- Chevauchement entre les chunks : **20 tokens**.
- Encodage : `o200k_base`.

Le chevauchement permet de conserver une partie du contexte entre deux chunks successifs.

## 5. Embeddings et stockage vectoriel

Le modèle `BAAI/bge-m3` transforme chaque chunk en un vecteur numérique représentant son contenu sémantique.

Les vecteurs sont ensuite enregistrés dans ChromaDB afin de permettre la recherche des passages les plus proches d’une question.

La collection utilisée est `cv_v1`, avec le répertoire de persistance `./store`.

## 6. Recherche des passages pertinents

Le retriever utilise une recherche par similarité :

- Type de recherche : `similarity`.
- Nombre maximal de passages recherchés : `k = 5`.

Lorsqu’une question est posée, le système récupère les chunks les plus pertinents du CV pour construire le contexte transmis au LLM.

## 7. Génération de la réponse

Le modèle `Gemma 4 31B`, appelé via Ollama, reçoit un prompt contenant :

- Le contexte extrait du CV.
- La question de l’utilisateur.
- Les règles de génération.

Le prompt impose les règles suivantes :

- Utiliser uniquement les informations présentes dans le contexte.
- Ne pas inventer de compétences, d’expériences, de dates ou de réalisations.
- Répondre « Je ne sais pas ! » si l’information demandée est absente.
- Répondre dans la langue utilisée par l’utilisateur.
- Produire une réponse directe et naturelle.

La température est fixée à `0` afin de limiter la variabilité des réponses.

## 8. Fonction RAG

La fonction `RAG()` regroupe les principales étapes du système :

1. Récupération des passages pertinents.
2. Construction du contexte.
3. Insertion du contexte et de la question dans le prompt.
4. Appel du modèle de génération.
5. Retour de la réponse.

Cette fonction permet de poser différentes questions sur le document sans répéter manuellement toutes les étapes du pipeline.

## 9. Étude de cas : présentation du profil professionnel

### Question utilisée

**« Présente mon profil professionnel. »**

### Déroulement du test

1. Le système reçoit la question.
2. Le retriever recherche les passages pertinents dans le CV.
3. Les passages récupérés sont regroupés dans un contexte.
4. Le LLM utilise ce contexte pour présenter le profil professionnel.
5. La réponse est affichée dans le notebook.

Le système peut notamment exploiter les informations du CV concernant la formation, les compétences techniques, les projets et les expériences professionnelles, dans la mesure où ces informations figurent dans les passages récupérés.

La qualité de la réponse dépend donc de la pertinence des chunks retrouvés et des informations qu’ils contiennent.

## 10. Évaluation de la fidélité au contexte

Le notebook prévoit une évaluation avec un modèle juge, appelé `groundness_checker`.

Son objectif est de vérifier si la réponse est fondée uniquement sur les informations présentes dans le contexte fourni.

L’évaluation utilise une échelle de 1 à 5 :

- **1/5** : réponse incorrecte, hors sujet ou contenant des informations inventées.
- **2/5** : réponse contenant des extrapolations non justifiées.
- **3/5** : réponse partiellement fondée sur le contexte.
- **4/5** : réponse largement fondée sur le contexte, avec quelques imprécisions possibles.
- **5/5** : réponse entièrement fondée sur les informations du contexte.

Le notebook contient le code nécessaire à cette évaluation, mais aucun score final précis n’est confirmé dans les résultats enregistrés.

## 11. Architecture générale

```text
Document PDF (CV)
       |
       v
Chargement avec PyPDFLoader
       |
       v
Découpage en chunks
       |
       v
Embeddings avec BAAI/bge-m3
       |
       v
Stockage dans ChromaDB
       |
Question de l’utilisateur
       |
       v
Recherche par similarité
       |
       v
Récupération des passages pertinents
       |
       v
Construction du prompt
       |
       v
Génération avec Gemma 4 31B via Ollama
       |
       v
Réponse fondée sur le contexte
       |
       v
Évaluation de la fidélité
```

## 12. Conclusion

Ce TP a permis de mettre en œuvre les principales étapes d’un système RAG : chargement d’un document, découpage en chunks, création d’embeddings, stockage vectoriel, recherche sémantique et génération de réponses à l’aide d’un LLM.

L’étude de cas sur le CV illustre l’utilisation du RAG pour interroger un document personnel et présenter un profil professionnel à partir de son contenu.

Le principal intérêt de cette approche est de fournir au modèle un contexte documentaire pertinent afin de mieux fonder ses réponses sur une source précise. Cependant, la fidélité doit être vérifiée, car le prompt et la recherche vectorielle ne garantissent pas à eux seuls l’absence totale d’erreurs ou d’hallucinations.
