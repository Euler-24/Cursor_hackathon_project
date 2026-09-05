import {
  CheckCircle2,
  AlertTriangle,
  Droplets,
  Leaf,
  Sun as SunIcon,
  CloudSun,
  CloudRain,
} from "lucide-react";

export const CULTURES = [
  { id: "tomate", label: "Tomate" },
  { id: "mais", label: "Maïs" },
  { id: "manioc", label: "Manioc" },
  { id: "riz", label: "Riz" },
  { id: "cacao", label: "Cacao" },
];

export const DIAGNOSES = [
  {
    id: "sain",
    label: "Plante saine",
    tone: "green",
    icon: CheckCircle2,
    summary: "Aucun signe de maladie détecté sur cette feuille.",
    advice: [
      "Continuez l'arrosage habituel, sans excès sur le feuillage.",
      "Observez à nouveau la plante dans une semaine.",
      "Aucune intervention nécessaire pour le moment.",
    ],
  },
  {
    id: "fongique",
    label: "Maladie fongique probable",
    tone: "clay",
    icon: AlertTriangle,
    summary: "Taches brunes cerclées, fréquentes en période humide.",
    advice: [
      "Retirez et détruisez les feuilles très atteintes.",
      "Évitez de mouiller le feuillage lors de l'arrosage.",
      "Espacez un peu plus les plants pour aérer la parcelle.",
      "Contactez un agent agricole avant tout traitement.",
    ],
  },
  {
    id: "hydrique",
    label: "Excès d'humidité",
    tone: "sky",
    icon: Droplets,
    summary: "Traces d'humidité prolongée sur le feuillage, propice aux champignons.",
    advice: [
      "Espacez les arrosages et privilégiez le pied de la plante.",
      "Améliorez le drainage autour des racines.",
      "Surveillez l'apparition de taches dans les prochains jours.",
    ],
  },
  {
    id: "carence",
    label: "Carence en nutriments probable",
    tone: "sun",
    icon: Leaf,
    summary: "Jaunissement entre les nervures, typique d'un manque d'éléments nutritifs.",
    advice: [
      "Vérifiez l'apport en engrais adapté à la culture.",
      "Évitez de sur-arroser, cela peut aggraver le lessivage du sol.",
      "Si le jaunissement s'étend, signalez-le à l'agent agricole.",
    ],
  },
];

export const MARKETS = [
  { name: "Marché Central", distance: "2,4 km", price: 615, trend: "up", updated: "aujourd'hui" },
  { name: "Marché de Bouaflé", distance: "11 km", price: 540, trend: "down", updated: "hier" },
  { name: "Marché du Carrefour", distance: "6,8 km", price: 580, trend: "up", updated: "aujourd'hui" },
  { name: "Marché de Daloa", distance: "24 km", price: 560, trend: "flat", updated: "il y a 2 jours" },
];

export const FORECAST = [
  { day: "Aujourd'hui", icon: SunIcon, temp: 31, rain: 5 },
  { day: "Demain", icon: CloudSun, temp: 29, rain: 20 },
  { day: "Mercredi", icon: CloudRain, temp: 26, rain: 80 },
  { day: "Jeudi", icon: CloudRain, temp: 25, rain: 70 },
  { day: "Vendredi", icon: SunIcon, temp: 30, rain: 10 },
];

export const HISTORY = [
  { date: "28 août", culture: "Tomate", result: "fongique", parcelle: "Parcelle 2" },
  { date: "21 août", culture: "Tomate", result: "sain", parcelle: "Parcelle 1" },
  { date: "14 août", culture: "Tomate", result: "carence", parcelle: "Parcelle 2" },
  { date: "6 août", culture: "Tomate", result: "sain", parcelle: "Parcelle 1" },
];

// Static, literal class strings so Tailwind's JIT scanner picks them up.
export const TONE_CLASSES = {
  green: { bg: "bg-green/15", fg: "text-green" },
  clay: { bg: "bg-clay/15", fg: "text-clay" },
  sun: { bg: "bg-sun/15", fg: "text-sun" },
  sky: { bg: "bg-sky/15", fg: "text-sky" },
};
