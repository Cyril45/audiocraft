# AudioCraft CLI – MusicGen

Cette CLI fournit une interface générique et réutilisable pour générer de la musique avec MusicGen (AudioCraft).

Elle est conçue pour être utilisée principalement via Docker, afin de pouvoir être intégrée facilement dans d’autres applications, pipelines ou services, sans dépendance directe au code Python interne.

La CLI est volontairement une couche minimale au-dessus d’AudioCraft, sans modifier le comportement interne des modèles.

--------------------------------------------------
PRINCIPE
--------------------------------------------------

- La CLI encapsule MusicGen dans une interface stable
- L’image Docker est l’artefact principal de distribution
- La génération audio est pilotée uniquement par des paramètres explicites
- Aucun état persistant interne (hors cache des modèles HuggingFace)
- Le projet est pensé comme un générateur de musique réutilisable

--------------------------------------------------
PRÉREQUIS
--------------------------------------------------

- Docker
- GPU NVIDIA avec support CUDA recommandé
- Support CPU possible mais lent

--------------------------------------------------
UTILISATION VIA DOCKER
--------------------------------------------------

Image buildée localement (tag par défaut : audiocraft:latest).

### Windows (PowerShell)

docker run --rm --gpus all -v ${PWD}:/out audiocraft:latest --model facebook/musicgen-small --prompt "orchestral cinematic score" --duration 60 --output /out/orchestral.wav

### Linux / macOS (Bash)

docker run --rm --gpus all -v $(pwd):/out audiocraft:latest --model facebook/musicgen-small --prompt "orchestral cinematic score" --duration 60 --output /out/orchestral.wav

Notes :
- PowerShell : utiliser ${PWD}
- Bash / Linux / macOS : utiliser $(pwd)
- Le fichier généré est écrit dans le dossier monté (/out)

--------------------------------------------------
LISTE COMPLÈTE DES MODÈLES MUSICGEN
--------------------------------------------------

Tous les modèles MusicGen sont chargés dynamiquement via HuggingFace.
La CLI accepte n’importe quel identifiant MusicGen valide.

Text → Music (mono) :
- facebook/musicgen-small
- facebook/musicgen-medium
- facebook/musicgen-large

Text → Music (stéréo) :
- facebook/musicgen-small-stereo
- facebook/musicgen-medium-stereo
- facebook/musicgen-large-stereo

Text + Melody → Music :
- facebook/musicgen-melody
- facebook/musicgen-melody-stereo

Notes :
- small : rapide, faible consommation GPU
- medium : compromis qualité / vitesse
- large : qualité maximale, GPU requis
- stereo : sortie stéréo, plus coûteuse
- melody : nécessite un fichier audio d’entrée (support CLI à venir)

--------------------------------------------------
PARAMÈTRES DISPONIBLES (ACTUELS)
--------------------------------------------------

--model  
Identifiant HuggingFace du modèle MusicGen.

--prompt (obligatoire)  
Texte décrivant la musique à générer.

--duration  
Durée de la musique générée en secondes.

--output (obligatoire)  
Chemin du fichier WAV de sortie (dans un volume monté).

Le fichier généré :
- format WAV
- fréquence 32 kHz
- compatible avec tout logiciel audio / vidéo

--------------------------------------------------
EXEMPLES
--------------------------------------------------

Génération simple :
--model facebook/musicgen-small --prompt "ambient cinematic music" --duration 20 --output output.wav

Qualité maximale :
--model facebook/musicgen-large --prompt "orchestral cinematic score" --duration 60 --output orchestral.wav

--------------------------------------------------
BUILD DE L’IMAGE DOCKER
--------------------------------------------------

À partir du fork :

git clone https://github.com/Cyril45/audiocraft.git
cd audiocraft
docker build -t audiocraft .

L’image produite est :
- audiocraft:latest

--------------------------------------------------
PHILOSOPHIE
--------------------------------------------------

- la CLI est une interface, pas une logique métier
- AudioCraft reste inchangé
- la stabilité prime sur les nouveautés
- l’image Docker est pensée comme un composant réutilisable
- aucune promesse de fonctionnalités non implémentées

--------------------------------------------------
ARCHITECTURE
--------------------------------------------------

audiocraft_cli/cli.py  
audiocraft_cli/engine.py  
audiocraft_cli/audio.py  
audiocraft_cli/models.py  
audiocraft_cli/config.py  
audiocraft_cli/exceptions.py  
