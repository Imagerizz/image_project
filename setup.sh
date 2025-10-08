#!/usr/bin/env bash

set -e

echo "=== Création de l'environnement virtuel ==="
python3 -m venv venv

echo "=== Activation de l'environnement virtuel ==="
# Détection automatique du système
case "$(uname -s)" in
    Linux|Darwin)
        source venv/bin/activate
        ;;
    MINGW*|MSYS*|CYGWIN*)
        source venv/Scripts/activate
        ;;
    *)
        echo "Système non reconnu. Activez l'environnement manuellement."
        ;;
esac

echo "=== Installation des dépendances ==="
if [ -f "requirements.txt" ]; then
    pip install --upgrade pip
    pip install -r requirements.txt
    echo "✅ Installation terminée."
else
    echo "⚠️  Fichier requirements.txt introuvable."
fi
