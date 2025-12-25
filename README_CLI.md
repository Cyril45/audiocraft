# AudioCraft CLI – MusicGen

Cette CLI fournit une interface générique et réutilisable pour générer de la musique avec MusicGen (AudioCraft).
Elle est conçue pour être utilisée principalement via Docker, afin de pouvoir être intégrée facilement dans d’autres applications, pipelines ou services.

La CLI est volontairement une couche minimale au-dessus d’AudioCraft, sans modifier le comportement interne des modèles.

--------------------------------------------------
PRINCIPE
--------------------------------------------------

- La CLI encapsule MusicGen dans une interface stable
- L’image Docker est l’artefact principal de distribution
- La génération audio est pilotée uniquement par des paramètres explicites
- Aucun état persistant interne (hors cache modèles HuggingFace)

--------------------------------------------------
PRÉREQUIS
--------------------------------------------------

- Docker
- GPU NVIDIA avec CUDA recommandé
- Support CPU possible mais lent

--------------------------------------------------
UTILISATION VIA DOCKER
--------------------------------------------------

Image déjà buildée :

docker run --rm --gpus all -v $(pwd):/out audiocraft \
  --prompt "dark cinematic music" \
  --duration 30 \
  --output /out/output.wav

--------------------------------------------------
LISTE COMPLÈTE DES MODÈLES MUSICGEN
--------------------------------------------------

Tous les modèles MusicGen sont chargés via HuggingFace.
La CLI accepte n’importe quel identifiant valide.

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
- stereo : sortie stéréo, plus coûteux
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
Chemin du fichier WAV de sortie.

Le fichier généré :
- format WAV
- fréquence 32 kHz
- compatible avec tout logiciel audio / vidéo

--------------------------------------------------
EXEMPLES
--------------------------------------------------

Génération simple :
--model facebook/musicgen-small --prompt "ambient cinematic music" --duration 20 --output output.wav

Modèle plus qualitatif :
--model facebook/musicgen-large --prompt "orchestral cinematic score" --duration 60 --output orchestral.wav

--------------------------------------------------
BUILD DE L’IMAGE DOCKER
--------------------------------------------------

À partir du fork :

git clone https://github.com/Cyril45/audiocraft.git
cd audiocraft
docker build -t audiocraft .

--------------------------------------------------
PHILOSOPHIE
--------------------------------------------------

- la CLI est une interface, pas une logique métier
- AudioCraft reste inchangé
- la stabilité prime sur les nouveautés
- l’image Docker est pensée comme un composant réutilisable

--------------------------------------------------
ARCHITECTURE
--------------------------------------------------

audiocraft_cli/cli.py
audiocraft_cli/engine.py
audiocraft_cli/audio.py
audiocraft_cli/models.py
audiocraft_cli/config.py
audiocraft_cli/exceptions.py