# Architecture

## Arborescence du projet

```
anpr-project/
├─ docs/                      # Documentation (spécifs, schémas, rapports)
├─ venv/                      # Environnement virtuel
│
├─ data/                      # Données, ne pas commiter. Check la doc.
│  ├─ raw/                    # Images brutes
│  ├─ processed/              # Images prétraitées/crops
│  ├─ annotations/            # COCO/YOLO (bbox plaques)
│  └─ splits/                 # train/val/test (listes de fichiers)
│
├─ models/                    # Checkpoints des models. Models sauvegardés
│  ├─ detection/              # YOLO
│  └─ ocr/                    # CRNN
│
├─ src/                       # Code source
│  ├─ detection/              # YOLO
│  ├─ ocr/                    # OCR
│  └─ pipeline/               # Fichiers utilitaires de la pipeline end to end
│     ├─ preprocess.py        # Rescaling, CLAHE, perspective, etc.
│     ├─ postprocess.py       # Regex, corrections (O↔0, B↔8)
│     ├─ cropper.py           # Extraction de plaques depuis bboxes
│     └─ run_end2end.py       # Image -> YOLO -> OCR -> JSON
│
├─ notebooks/                 # Explorations & EDA
│  ├─ 00_data_exploration.ipynb
│  ├─ 10_yolo_training.ipynb
│  └─ 20_ocr_training.ipynb
│
├─ configs/                   # YAML/JSON de config
│  ├─ yolo_train.yaml         # chemins, hyperparams, image_size
│  ├─ ocr_train.yaml
│
├─ .gitignore                 # Ignorer venv/, data/raw, models/, etc.
├─ pyproject.toml             # (ou requirements.txt + setup.cfg)
├─ requirements.txt           # Dépendences
├─ README.md                  # Guide d’installation, usage, démo
└─ LICENSE                    # Licence du projet
```
