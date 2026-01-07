# 🛡️ Secure Password Generator & Analyzer

Un outil en ligne de commande (CLI) écrit en Python pour générer des mots de passe cryptographiquement sûrs et analyser leur force en temps réel.

## ✨ Fonctionnalités

- **Génération Sécurisée** : Utilise le module `secrets` de Python pour un hasard de niveau cryptographique (CSPRNG)
- **Validation des Entrées** : Système de vérification pour s'assurer que l'utilisateur saisit un nombre valide et une longueur minimale (8+ caractères)
- **Analyseur de Force** : Calcul d'un score basé sur 4 critères essentiels
- **Visualisation Graphique** : Affichage d'une barre de progression et d'un pourcentage directement dans la console

## 📊 Barème de Sécurité

L'analyseur vérifie les critères suivants :

1. Longueur (12+ caractères)
2. Majuscules (A-Z)
3. Chiffres (0-9)
4. Caractères spéciaux (!, @, #, $, etc.)

## 🚀 Installation et Usage

### Cloner le projet
```bash
git clone https://github.com/ton-pseudo/password-generator.git
cd password-generator
```

### Lancer l'outil
```bash
py passwordGenerator.py
```

### Exemple d'utilisation
```
Entrez la longueur du mot de passe : 16
Your password is: 4&kL9#pQ2!mN5@xR
Force : [██████████] 4/4
```

## 🔒 Sécurité

Ce projet a été conçu avec les meilleures pratiques de **Security Engineering** :

- ✅ Utilisation exclusive de `secrets` (CSPRNG) - rejet de `random` non sécurisé
- ✅ Validation stricte des entrées pour prévenir les crashs
- ✅ Longueur minimale de 8 caractères (12+ recommandé)
- ✅ Aucun stockage des mots de passe générés

## 📝 Licence

MIT License

## 👤 Auteur

**Enzo Abdi**  
GitHub: [@zoaavela](https://github.com/zoaavela)
