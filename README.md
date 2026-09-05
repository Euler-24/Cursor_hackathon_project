# AgriSense — Espace producteur

Interface React (Vite + Tailwind CSS) pour l'espace producteur et les interfaces
de consultation (diagnostic, météo, marchés, historique, profil) du projet AgriSense.

## Lancer le projet en local

Prérequis : [Node.js](https://nodejs.org) 18 ou plus récent.

```bash
cd agrisense-frontend
npm install
npm run dev
```

Ouvrez ensuite l'URL affichée dans le terminal (en général `http://localhost:5173`).

## Structure du projet

```
agrisense-frontend/
├── index.html                  point d'entrée HTML, charge les polices
├── tailwind.config.js          jetons de couleur et typographies personnalisés
├── src/
│   ├── main.jsx                point d'entrée React
│   ├── App.jsx                 état de navigation + assemblage des pages
│   ├── index.css               directives Tailwind
│   ├── data.js                 données de démonstration (diagnostics, marchés, météo)
│   ├── components/
│   │   ├── TopBar.jsx
│   │   ├── BottomNav.jsx
│   │   ├── LeafSwatch.jsx      vignettes SVG des cas de démonstration
│   │   └── UI.jsx              Eyebrow, SectionHeading, Pill, PrimaryButton
│   └── pages/
│       ├── Accueil.jsx
│       ├── Diagnostic.jsx
│       ├── Meteo.jsx
│       ├── Marches.jsx
│       ├── Historique.jsx
│       └── Profil.jsx
```

## Prochaines étapes suggérées

- Remplacer les données de `src/data.js` par des appels à l'API Flask (`api_routes.py`)
- Remplacer le tirage aléatoire dans `Diagnostic.jsx` par un vrai appel au service de diagnostic
- Ajouter `react-router-dom` si le projet grandit au-delà d'un état de navigation simple
