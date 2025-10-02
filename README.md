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

---

## Création de l'environnement virtuel

### Avec un terminal (Windows/macOS/Linux)

#### Créer le venv
```bash
python3.13 -m venv venv
```

#### Activer le venv
- **Windows (PowerShell/Cmd):**
  ```powershell
  .\venv\Scripts\activate
  ```
- **macOS/Linux (Bash/Zsh):**
  ```bash
  source venv/bin/activate
  ```

#### Installer les dépendances
```bash
pip install -r requirements.txt
```

#### Désactiver le venv
```bash
deactivate
```

---

## Utilisation avec PyCharm Professionnel

1. Ouvrir le projet dans PyCharm.
2. Aller dans `File > Settings > Project > Python Interpreter`.
3. Cliquer sur `Add Interpreter` > `Add Local Interpreter`.
4. Sélectionner `Virtualenv Environment` > `Existing environment`.
5. Choisir le dossier `venv` (ou le créer via PyCharm en spécifiant Python 3.13).
6. Valider : PyCharm installera automatiquement les dépendances depuis `requirements.txt`.

---

## Utilisation avec VSCode

1. Ouvrir le projet dans VSCode.
2. Ouvrir un terminal intégré (`Ctrl + \`` ou `Terminal > New Terminal`).
3. Activer le venv (voir instructions ci-dessus).
4. Installer les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
5. Sélectionner l'interpréteur Python :
   - `Ctrl + Shift + P` > `Python: Select Interpreter` > Choisir le venv (`venv/Scripts/python` ou `venv/bin/python`).

---

## Utilisation avec Vim

1. Ouvrir un terminal dans le dossier du projet.
2. Activer le venv (voir instructions ci-dessus).
3. Installer les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
4. Utiliser Vim pour éditer les fichiers :
   ```bash
   vim src/main.py
   ```
5. Exécuter le code depuis le terminal activé :
   ```bash
   python src/main.py
   ```

---

## Structure du projet

```
image_project/
│
├── venv/                  # Environnement virtuel (Python 3.13)
├── requirements.txt       # Liste des dépendances
├── src/                   # Code source
│   └── main.py            # Point d'entrée du projet
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

## Licence

[MIT](LICENSE)
