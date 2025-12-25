# AudioCraft MusicGen – Documentation API

Cette API permet de générer de la musique à partir d’un prompt texte en utilisant
les modèles MusicGen (AudioCraft – Meta).

L’API est conçue pour être :
- stateless
- utilisable via Docker
- intégrable dans n’importe quelle application (backend, script, service)

Le résultat est retourné directement sous forme de fichier audio WAV.

--------------------------------------------------
URL DE BASE
--------------------------------------------------

Par défaut (Docker en local) :

http://localhost:8000

--------------------------------------------------
ENDPOINTS
--------------------------------------------------

========================================
GET /
========================================

Description :
- Retourne l’interface web de génération
- Interface simple pour usage humain

Réponse :
- HTML

Exemple :
Ouvrir dans un navigateur :
http://localhost:8000

--------------------------------------------------

========================================
POST /generate
========================================

Description :
- Génère une musique à partir d’un prompt texte
- Retourne directement un fichier WAV
- Aucun fichier n’est conservé sur le serveur après la réponse

Headers requis :
Content-Type: application/json

Body (JSON) :

{
  "model": "facebook/musicgen-medium",
  "prompt": "orchestral cinematic score, emotional build-up",
  "duration": 60
}

--------------------------------------------------
PARAMÈTRES
--------------------------------------------------

model (string, obligatoire)
- Identifiant HuggingFace du modèle MusicGen

Modèles courants :

Text → Music (mono)
- facebook/musicgen-small
- facebook/musicgen-medium
- facebook/musicgen-large

Text → Music (stéréo)
- facebook/musicgen-small-stereo
- facebook/musicgen-medium-stereo
- facebook/musicgen-large-stereo

prompt (string, obligatoire)
- Description textuelle de la musique à générer
- Plus le prompt est descriptif, meilleur est le résultat

Exemples de mots-clés efficaces :
- cinematic
- orchestral
- ambient
- emotional
- dark
- epic
- viral
- loopable

duration (integer, optionnel)
- Durée de la musique en secondes
- Valeur par défaut : 30
- Valeur recommandée : 8 à 60

--------------------------------------------------
RÉPONSE
--------------------------------------------------

Succès :
- Code HTTP : 200
- Type : audio/wav
- Contenu : fichier WAV 32 kHz

Le fichier est :
- généré temporairement
- envoyé au client
- supprimé automatiquement côté serveur

Aucune donnée n’est conservée.

--------------------------------------------------
ERREURS
--------------------------------------------------

400 / 422
- Paramètres manquants ou invalides

500
- Erreur interne lors du chargement du modèle ou de la génération

La réponse contient un message d’erreur explicite.

--------------------------------------------------
EXEMPLES D’UTILISATION
--------------------------------------------------

========================================
curl
========================================

curl -X POST http://localhost:8000/generate ^
  -H "Content-Type: application/json" ^
  -d "{ \"model\": \"facebook/musicgen-medium\", \"prompt\": \"orchestral cinematic score\", \"duration\": 30 }" ^
  --output music.wav

--------------------------------------------------

========================================
Python
========================================

import requests

url = "http://localhost:8000/generate"

payload = {
    "model": "facebook/musicgen-medium",
    "prompt": "orchestral cinematic score",
    "duration": 30,
}

response = requests.post(url, json=payload)

with open("music.wav", "wb") as f:
    f.write(response.content)

--------------------------------------------------
REMARQUES IMPORTANTES
--------------------------------------------------

- Le premier appel avec un modèle est plus lent (chargement)
- Les appels suivants sont plus rapides (modèle en cache mémoire)
- GPU fortement recommandé
- CPU possible mais très lent

--------------------------------------------------
PHILOSOPHIE
--------------------------------------------------

- L’API est une couche fine au-dessus d’AudioCraft
- Aucun état persistant
- Docker est l’unité de déploiement
- Le serveur peut être intégré dans n’importe quel pipeline

--------------------------------------------------
