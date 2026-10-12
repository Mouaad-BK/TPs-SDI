# TP 1 — Bases de Python

## Introduction

Ce premier TP du module **Système Distribué Agentique** est consacré à la pratique des bases du langage Python.  
Les exercices permettent de travailler progressivement les notions fondamentales nécessaires pour la suite du module, notamment les conversions de types, les structures conditionnelles, les boucles, les fonctions et les structures de données.

## Exercices réalisés

### 1. Opérations de conversion

Manipulation des conversions de types avec `int()`, `float()` et `str()`.

**Exercice : Système de notation pondérée**
- Saisie des informations d'un étudiant.
- Conversion des notes et des coefficients.
- Calcul d'une moyenne pondérée.
- Affichage du résultat final.

### 2. Structures conditionnelles

Utilisation de `if`, `elif` et `else` pour contrôler le comportement d'un programme.

**Exercice : Analyse d'une équation du second degré**
- Saisie des coefficients `a`, `b` et `c`.
- Identification du type d'équation.
- Calcul du discriminant `Δ`.
- Détermination du nombre de solutions réelles.

### 3. Boucles `for` et `while`

Mise en pratique des boucles et de la fonction `range()`.

**Exercice : Contrôle de saisie**
- Vérification qu'un nombre saisi est un entier impair avec `while`.
- Affichage des nombres de `0` jusqu'au nombre saisi avec `for`.

### 4. Fonctions

Utilisation des fonctions, des paramètres par défaut et de l'immuabilité des types de base.

**Exercice : Traitement des notes**
- Création de la fonction `ajouter_bonus()`.
- Utilisation d'un paramètre par défaut.
- Manipulation de `map()` et `zip()`.

### 5. Listes et calcul de la médiane

Manipulation des listes et des indices.

**Exercice : Saisie ordonnée et calcul de la médiane**
- Saisie d'un ensemble de notes dans un ordre croissant.
- Contrôle de l'ordre avec `while`.
- Détermination du nombre pair ou impair de notes.
- Calcul de la médiane.

### 6. Structures de données pour l'IA agentique

Mise en pratique des structures `list`, `tuple` et `dict` dans un contexte lié aux systèmes multi-agents.

**Problème pratique : Configuration d'un système multi-agents**

Création d'une configuration centralisée contenant :
- un dictionnaire pour la configuration d'un agent ;
- une liste d'outils ;
- des tuples représentant les outils et leurs versions ;
- une modification dynamique de la température de l'agent ;
- l'accès à une donnée imbriquée pour extraire le nom d'un outil.

## Conclusion

Ce TP a permis de consolider les bases de Python à travers plusieurs exercices pratiques, allant des opérations simples sur les données jusqu'à la manipulation de structures imbriquées dans un contexte d'IA agentique.