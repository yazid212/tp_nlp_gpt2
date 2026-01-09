# **📘 README.md - Rapport Complet du TP**


# TP NLP : Assistant Pédagogique avec GPT-2

## 📋 Table des Matières
1. [Introduction](#introduction)
2. [Objectifs du TP](#objectifs-du-tp)
3. [Structure du Projet](#structure-du-projet)
4. [Installation et Exécution](#installation-et-exécution)
5. [Implémentation des Questions](#implémentation-des-questions)
6. [Résultats et Analyse](#résultats-et-analyse)
7. [Limites et Perspectives](#limites-et-perspectives)
8. [Conclusion](#conclusion)

---

## 🎯 Introduction

Ce projet a pour objectif de développer un assistant pédagogique basé sur le modèle de langage GPT-2. L'assistant doit être capable de reformuler des contenus éducatifs, simplifier des notions complexes et générer des questions de compréhension sous forme de QCM.

**Contexte** : TP de NLP (Natural Language Processing) dans un cadre éducatif.

**Technologies utilisées** : Python, PyTorch, Transformers (Hugging Face), GPT-2

---

## 🎯 Objectifs du TP

### Questions à traiter :

1. **Conception globale du pipeline NLP**
2. **Prétraitement du texte pédagogique**
3. **Chargement du modèle GPT-2**
4. **Génération de texte pédagogique reformulé**
5. **Analyse de l'effet du prompt sur la génération**
6. **Génération d'un mini QCM**
7. **Analyse critique des limites**

---

## 📁 Structure du Projet

```
tp_nlp_gpt2/
│
├── assistant_pedagogique.py      # Code principal
├── test_simple.py                # Fichier de tests
├── requirements.txt              # Dépendances Python
├── README.md                     # Ce fichier
└── images/                       # Captures d'écran (optionnel)
```

### Fichiers principaux :

| Fichier | Description |
|---------|-------------|
| `assistant_pedagogique.py` | Implémente toutes les fonctions du TP |
| `test_simple.py` | Tests unitaires des différentes fonctionnalités |
| `requirements.txt` | Liste des packages nécessaires |

---

## ⚙️ Installation et Exécution

### Prérequis
- Python 3.8+
- pip (gestionnaire de packages Python)

### Installation

```bash
# Cloner le projet (si applicable)
git clone <url-du-projet>

# Naviguer vers le dossier
cd tp_nlp_gpt2

# Installer les dépendances
pip install -r requirements.txt
```

### Exécution

```bash
# Exécuter le programme principal
python assistant_pedagogique.py

# Exécuter les tests
python test_simple.py
```

### Dépendances principales
```txt
torch>=2.0.0
transformers>=4.30.0
```

---


============================================================
ASSISTANT PÉDAGOGIQUE GPT-2 - TP NLP
============================================================

📝 TEXTE ORIGINAL :
La photosynthèse est un processus utilisé par les plantes...

✅ TEXTE APRÈS PRÉTRAITEMENT :
La photosynthèse est un processus utilisé par les plantes...

📝 Résultat de la reformulation :
In this way it is easy to understand that if you take a leaf...

🔹 Reformulation simple :
To achieve this, a chemical is formed in the plant...

🔹 Reformulation avec exemple :
If you are able to convey a feeling of warmth...

📝 QCM généré :
Question 1: Is it possible to use only two different materials...
Question 2: Is there a way to create a new flower...
```

### Analyse des résultats

1. **Prétraitement** : Fonctionne correctement, élimine les caractères indésirables
2. **Reformulation** : GPT-2 génère du texte cohérent mais principalement en anglais
3. **Effet du prompt** : Les différents prompts produisent des variations dans les réponses
4. **QCM** : Structure correcte mais contenu parfois hors-sujet
5. **Limites** : Confirmées par l'analyse critique

---

## ⚠️ Limites et Perspectives

### Limites identifiées

| Limite | Impact | Exemple observé |
|--------|---------|-----------------|
| **Langue anglaise dominante** | Réponses souvent en anglais malgré prompts en français | "In this way it is easy to understand..." |
| **Précision scientifique limitée** | Risque d'inexactitudes | Explications simplifiées parfois incorrectes |
| **Manque de contextualisation** | Ne s'adapte pas au niveau de l'élève | Même type de réponse pour tous les niveaux |
| **Cohérence variable** | Contradictions possibles | Réponses parfois incohérentes sur des textes longs |
| **Biais des données** | Reproduction des biais d'entraînement | Perspectives limitées par le dataset original |

### Améliorations possibles

1. **Utiliser un modèle français** : Camembert ou Flaubert pour de meilleurs résultats en français
2. **Fine-tuning éducatif** : Entraîner le modèle sur des données pédagogiques
3. **Système de validation** : Ajouter une vérification factuelle des réponses
4. **Interface utilisateur** : Développer une interface web ou application
5. **Personnalisation** : Adapter les réponses au niveau scolaire

---

## 🎓 Conclusion

### Bilan du TP

✅ **Objectifs atteints** :
- Pipeline NLP complet implémenté
- Toutes les fonctions demandées opérationnelles
- Analyse critique pertinente des limites
- Code propre et documenté

⚠️ **Observations importantes** :
- GPT-2 montre ses limites pour un usage éducatif en français
- La qualité pédagogique nécessite une supervision humaine
- Le modèle est plus adapté à la génération de texte qu'à l'enseignement

### Compétences développées

1. **Traitement du Langage Naturel** : Prétraitement, génération de texte
2. **Utilisation de modèles pré-entraînés** : GPT-2 via Hugging Face
3. **Analyse critique** : Évaluation des limites d'un modèle d'IA
4. **Développement Python** : Structuration de code, gestion des dépendances

### Perspectives professionnelles

Ce TP illustre les enjeux actuels de l'IA en éducation :
- Potentiel pour l'assistance pédagogique
- Nécessité de validation humaine
- Importance des modèles multilingues
- Éthique et biais dans l'IA éducative
```
