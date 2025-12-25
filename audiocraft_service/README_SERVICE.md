# AudioCraft Service – MusicGen (Docker, API & Web)

Ce dépôt est un fork du projet officiel AudioCraft.
Il fournit un service prêt à l’emploi basé sur MusicGen, exposé via :

- une API HTTP
- une interface web simple
- une image Docker unique, réutilisable dans d’autres applications

ATTENTION  
Le fichier README.md d’origine n’est pas modifié et reste la documentation officielle d’AudioCraft.  
Ce document décrit uniquement le service ajouté par ce fork.

--------------------------------------------------
OBJECTIF
--------------------------------------------------

- Fournir un générateur de musique MusicGen clé en main
- Utilisable :
  - depuis un navigateur
  - via API (backend, automation, autres apps)
- Sans dépendre d’une CLI locale
- Compatible GPU CUDA (CPU possible mais lent)

--------------------------------------------------
PRÉREQUIS
--------------------------------------------------

- Docker
- GPU NVIDIA avec CUDA recommandé
- Windows, Linux ou WSL2

--------------------------------------------------
IMAGE DOCKER
--------------------------------------------------

L’image Docker est l’artefact principal.

Build local :

git clone https://github.com/Cyril45/audiocraft.git  
cd audiocraft  
docker build -t audiocraft:latest .

--------------------------------------------------
LANCER LE SERVICE
--------------------------------------------------

WINDOWS (PowerShell)

docker run -d --rm --gpus all `
  -p 8001:8000 `
  -v ${PWD}\.cache:/app/cache `
  --name audiocraft `
  audiocraft:latest

LINUX / WSL

docker run -d --rm --gpus all \
  -p 8001:8000 \
  -v $(pwd)/.cache:/app/cache \
  --name audiocraft \
  audiocraft:latest

Une fois lancé :

- API : http://localhost:8001
- Interface web : http://localhost:8001

Le conteneur tourne en tâche de fond.

--------------------------------------------------
CACHE DES MODÈLES
--------------------------------------------------

Le dossier .cache est monté dans le conteneur.

Avantages :
- Les modèles HuggingFace ne sont téléchargés qu’une seule fois
- Les générations suivantes sont beaucoup plus rapides
- Le cache survit aux redémarrages du conteneur

--------------------------------------------------
MODÈLES MUSICGEN SUPPORTÉS
--------------------------------------------------

Tous les modèles MusicGen sont chargés dynamiquement via HuggingFace.

TEXT → MUSIC (mono)
- facebook/musicgen-small
- facebook/musicgen-medium
- facebook/musicgen-large

TEXT → MUSIC (stéréo)
- facebook/musicgen-small-stereo
- facebook/musicgen-medium-stereo
- facebook/musicgen-large-stereo

TEXT + MELODY → MUSIC (non exposé pour l’instant)
- facebook/musicgen-melody
- facebook/musicgen-melody-stereo

Notes :
- small : rapide, faible VRAM
- medium : compromis recommandé
- large : qualité maximale, GPU requis

--------------------------------------------------
INTERFACE WEB
--------------------------------------------------

L’interface web permet :

- saisir un prompt textuel
- choisir le modèle
- définir la durée
- lancer une génération
- télécharger le fichier WAV généré

Aucune donnée n’est conservée côté serveur.

--------------------------------------------------
API HTTP
--------------------------------------------------

L’API est conçue pour une intégration dans d’autres applications.

ENDPOINT PRINCIPAL

POST /generate

PAYLOAD JSON

{
  "model": "facebook/musicgen-medium",
  "prompt": "orchestral cinematic score",
  "duration": 60
}

RÉPONSE

- Le fichier WAV est renvoyé directement
- Aucun fichier n’est conservé sur le disque du serveur

--------------------------------------------------
FORMAT AUDIO
--------------------------------------------------

Les fichiers générés :

- format : WAV
- fréquence : 32 kHz
- compatible montage vidéo / DAW

--------------------------------------------------
ARCHITECTURE DU SERVICE
--------------------------------------------------

audiocraft_service/
│
├── app.py
├── engine.py
├── audio.py
├── models.py
├── config.py
├── exceptions.py
│
└── web/
    └── index.html

--------------------------------------------------
PHILOSOPHIE
--------------------------------------------------

- Pas de logique métier dans l’API
- AudioCraft reste inchangé
- Le service est une couche d’exposition
- Docker est le point d’entrée unique
- Simplicité avant complexité

--------------------------------------------------
LIMITES ACTUELLES
--------------------------------------------------

- Pas de génération batch
- Pas de seed explicite
- Pas de paramètres avancés (cfg, temperature, etc.)
- Pas de persistance des générations

Ces choix sont volontaires pour garantir stabilité et clarté.

--------------------------------------------------
LICENCE
--------------------------------------------------

Ce fork respecte la licence du projet AudioCraft original.
Les poids de modèles sont soumis aux licences HuggingFace correspondantes.
