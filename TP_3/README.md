# Classification de sentiment avec Ollama

## 1. Présentation du travail

L’objectif de ce TP est de réaliser une **classification de sentiment à partir de critiques de films**, en utilisant un grand modèle de langage (LLM).

Pour chaque critique, le modèle doit déterminer si le sentiment exprimé est :

- `positive` : critique positive.
- `negative` : critique négative.

Le but est de comparer trois stratégies de prompting afin d’identifier celle qui donne les meilleurs résultats, sans entraîner un classifieur à partir de zéro.

## 2. Dataset utilisé

Le travail utilise un jeu de données contenant des critiques de films accompagnées de leurs étiquettes de sentiment.

Les données sont organisées en trois sous-ensembles :

- `train` : utilisé pour préparer les exemples de prompting.
- `test` : réservé à l’évaluation dans la structure initiale du dataset.
- `unsupervised` : données sans étiquettes.

Le travail se concentre sur les données étiquetées. Une partie sert à construire des exemples pour le prompting, tandis qu’une autre contient les réponses de référence (*gold examples*), utilisées pour comparer les prédictions du modèle aux sentiments attendus.

**Remarque :** le nom exact et la source du dataset ne sont pas confirmés dans les informations disponibles.

## 3. Méthodes utilisées

Trois stratégies sont comparées.

### 3.1. Zero-shot

Le modèle reçoit une instruction lui demandant de classifier la critique comme `positive` ou `negative`, sans recevoir d’exemples de classification.

### 3.2. Few-shot

Le modèle reçoit quelques exemples de critiques avec leurs sentiments avant de réaliser la classification.

Les exemples sont sélectionnés à partir des données d’apprentissage, avec des exemples positifs et négatifs.

### 3.3. Chain-of-Thought (CoT)

Cette méthode reprend le principe du Few-shot, mais ajoute des instructions demandant au modèle d’examiner soigneusement la critique avant de choisir le sentiment.

L’objectif est de vérifier si ces instructions supplémentaires améliorent la qualité de la classification.

## 4. Mise en œuvre

Le travail est réalisé en Python dans le notebook `Sentiment_Classification_Ollama(3).ipynb`.

Les principales étapes sont :

1. **Préparer les données :** sélectionner les textes et leurs étiquettes de sentiment.
2. **Construire les exemples :** séparer les exemples de prompting des exemples de référence.
3. **Créer les prompts :** préparer les instructions correspondant aux méthodes Zero-shot, Few-shot et CoT.
4. **Interroger le modèle :** utiliser Ollama pour obtenir une prédiction pour chaque critique.
5. **Évaluer les prédictions :** comparer les sentiments prédits aux étiquettes de référence et calculer le score micro-F1.

L’évaluation rapportée a été effectuée sur **100 exemples** pour chacune des trois méthodes.

## 5. Résultats obtenus

Les scores micro-F1 obtenus sont les suivants :

| Méthode | Score micro-F1 |
|---|---:|
| Zero-shot | 0,95 |
| Few-shot | **0,96** |
| Chain-of-Thought (CoT) | 0,9293 |

### Interprétation

- **Few-shot obtient le meilleur résultat**, avec un score de 0,96.
- Zero-shot obtient un score très proche, de 0,95, même sans exemples fournis au modèle.
- CoT obtient un score d’environ 0,9293. Les instructions supplémentaires de raisonnement n’ont donc pas amélioré les résultats dans cet essai.

## 6. Problème rencontré

Pendant l’évaluation, une erreur est apparue :

`Server disconnected without sending a response.`

Cette erreur indique qu’une requête au serveur n’a pas reçu de réponse. Le code ignore les exemples qui déclenchent une exception et poursuit l’évaluation.

Il faut donc vérifier le nombre d’exemples effectivement évalués pour chaque méthode. Si certains exemples ont été ignorés, les scores ne reposent pas nécessairement sur le même nombre de prédictions.

## 7. Conclusion

Cette expérimentation montre que la stratégie **Few-shot est la plus performante parmi les trois méthodes testées**, avec un micro-F1 de 0,96 sur l’évaluation réalisée.

Zero-shot reste néanmoins très performant, tandis que CoT n’apporte pas d’amélioration dans cette expérience.

Ces résultats restent préliminaires : ils portent sur 100 exemples et doivent être interprétés en tenant compte des erreurs de requête éventuelles. Une comparaison plus fiable nécessite de vérifier que chaque méthode est évaluée sur les mêmes exemples valides.
