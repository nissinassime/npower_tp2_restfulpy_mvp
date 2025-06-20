# npower_tp2_restfulpy_mvp
npower_tp2_restfulpy_mvp
with forks and pull requests

fastapi run  --port 8765 --host 0.0.0.0 --reload

Tp2_analyse_panier/
│
├── data/
│ ├── produits.csv
 # Liste des produits disponibles (id, nom, prix)
│ └── paniers.json
 # Données des paniers clients (nom du client, articles
achetés)
│
├── functions/
│ ├── gestion_produits.py
 # Fonctions pour gérer les produits (ajout,
recherche, affichage)
│ ├── gestion_paniers.py
 # Fonctions pour ajouter des produits aux paniers,
supprimer, etc.
│ └── analyse_achats.py
 # Fonctions d’analyse : total par client, produit le
plus acheté, etc.
│
├── main.py
 # Script principal pour interagir avec le système
├── README.md
 # Présentation, consignes, exemples d'utilisation
└── requirements.txt
 # (Optionnel) Bibliothèques utilisées si nécessaires


# Architecture generale de l'app
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── dependencies.py
│   └── routers
│   │   ├── __init__.py
│   │   ├── carts.py
│   │   └── users.py
│   │   └── clients.py
│   │   └── orders.py
│   │   └── products.py
│   │   └── requetes.py
│   │   └── statistiques.py
│   │   └── rawdb.py
│   └── internal
│       ├── __init__.py
│       └── admin.py

