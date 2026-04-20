# Modzi Info Quiz Backend

Backend Flask pour le système de recommandation de destinations d'études.

## Déploiement sur Railway

1. **Créer un compte** sur [Railway.app](https://railway.app)
2. **Connecter GitHub** : Autoriser Railway à accéder à ton compte GitHub
3. **Créer un nouveau projet** :
   - Cliquer "New Project"
   - Sélectionner "Deploy from GitHub repo"
   - Chercher et sélectionner ton repo `modzi-info-backend`
4. **Configuration automatique** :
   - Railway détecte automatiquement Python/Flask
   - Le déploiement se lance automatiquement
5. **Obtenir l'URL** :
   - Dans le dashboard, cliquer sur ton projet
   - Copier l'URL générée (ex: `https://modzi-info-backend.up.railway.app`)

## Mise à jour du frontend

Modifier `quiz.html` pour pointer vers l'URL Railway :

```javascript
const API_URL = 'https://TON-PROJET.up.railway.app';
```

## API Endpoints

- `GET /health` - Vérification du statut
- `POST /api/quiz/submit` - Soumettre un quiz
- `GET /api/quiz/results/<user_id>` - Récupérer les résultats

## Base de données

Utilise SQLite avec stockage persistant sur Railway.