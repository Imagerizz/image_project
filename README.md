# image_project

**Un projet Python pour le traitement ou la gestion d'images.**

---

## Prérequis

- **Python 3.13** (obligatoire)
- Git (optionnel, pour cloner le dépôt)
- Un terminal (PowerShell, Terminal, Bash, etc.)

---

## Installation

### 1. Cloner le dépôt (optionnel)

```bash
git clone <url-du-depot>
cd image_project
```

### 2. Mettre en place le projet

Exécuter le fichier `./setup.sh`

---

## Structure du projet

```
image_project/
│
├── venv/                  # Environnement virtuel (Python 3.13)
├── requirements.txt       # Liste des dépendances
├── src/                   # Code source
│   └── main.py            # Point d'entrée du projet
├── models/                # Liste des modèles post-entrainement
├── data/                  # Contient toutes les données d'entrainement du modèle
│
├── venv/                  # Environnement virtuel (Python 3.13)
└── README.md              # Ce fichier
```

---

## Mise à jour des dépendances

Si tu ajoutes/modifies des dépendances :

```bash
pip freeze > requirements.txt
```

---

## Exécution du projet

1. Activer le venv (voir instructions ci-dessus).
2. Lancer le script principal :
   ```bash
   python src/main.py
   ```

---

## Règles de bonnes pratiques :

- Utilisation des conventions Angular pour les commits.
  `format : type(scope): description`
  https://www.conventionalcommits.org/en/v1.0.0-beta.4/

  - Linter : Ruff

---

## Licence

[MIT](LICENSE)
