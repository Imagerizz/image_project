"""
This Python module aims to preprocess images for YOLO to improve its results.
"""

import shutil
from pathlib import Path

import kagglehub


def download_dataset():
    # Download latest version
    path = kagglehub.dataset_download("fareselmenshawii/large-license-plate-dataset")

    print("Path to dataset files:", path)


def copy_kaggle_dataset_to_raw(dataset_name: str, destination_dir: str = "data/raw") -> None:
    """
    Copie un dataset Kaggle depuis ~/.cache/kaggle/datasets/ vers data/raw.

    Args:
        dataset_name (str): Nom du dossier du dataset (ex: "fareselmenshawii").
        destination_dir (str): Dossier de destination (par défaut: "data/raw").
    """
    # Chemin relatif au cache Kaggle (compatible Windows/Linux)

    cache_dir = Path.home() / ".cache" / "kagglehub" / "datasets"
    source_path = cache_dir / dataset_name

    # Vérification
    if not source_path.exists():
        raise FileNotFoundError(
            f"Dataset '{dataset_name}' introuvable dans {cache_dir}. "
            f"Contenu actuel : {list(cache_dir.glob('*'))}"
        )

    # Création du dossier de destination
    dest_path = Path(destination_dir) / dataset_name
    dest_path.mkdir(parents=True, exist_ok=True)

    shutil.copytree(source_path, dest_path, dirs_exist_ok=True)
    print(f"Dataset copié de {source_path} vers {dest_path}")
