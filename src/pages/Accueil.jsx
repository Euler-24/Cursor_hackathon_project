import React from "react";
import { ChevronRight, CloudRain, Camera, TrendingUp } from "lucide-react";
import { DIAGNOSES, HISTORY, TONE_CLASSES } from "../data.js";
import { Eyebrow, SectionHeading } from "../components/UI.jsx";

export default function Accueil({ producer, goTo }) {
  const lastDiag = DIAGNOSES.find((d) => d.id === HISTORY[0].result);
  const lastTone = TONE_CLASSES[lastDiag.tone];

  return (
    <div className="px-5 pt-6 pb-4 lg:px-0 lg:pt-6 lg:pb-10">
      <Eyebrow>Espace producteur</Eyebrow>
      <SectionHeading
        title={`Bonjour, ${producer.name.split(" ")[0]}`}
        subtitle={`${producer.region} — parcelles de ${producer.culture.label.toLowerCase()}.`}
      />

      <button
        onClick={() => goTo("meteo")}
        className="w-full text-left rounded-2xl p-4 mb-4 flex items-start gap-3 active:scale-[0.99] transition-transform bg-surface border border-line"
      >
        <div className="w-9 h-9 rounded-full flex items-center justify-center shrink-0 bg-sky/15">
          <CloudRain size={16} className="text-sky" />
        </div>
        <div className="flex-1">
          <p className="text-[13.5px] font-medium text-ink">Fortes pluies attendues mercredi</p>
          <p className="text-[12px] mt-1 text-muted">Évitez d'arroser le feuillage d'ici là.</p>
        </div>
        <ChevronRight size={16} className="text-faint shrink-0 mt-1" />
      </button>

      <div className="grid grid-cols-2 gap-3 mb-5">
        <button
          onClick={() => goTo("diagnostic")}
          className="rounded-2xl p-4 flex flex-col items-start gap-4 active:scale-[0.98] transition-transform bg-orange"
        >
          <Camera size={18} className="text-white" strokeWidth={2.25} />
          <span className="text-[13.5px] font-semibold text-left text-white">Diagnostiquer une plante</span>
        </button>

        <button
          onClick={() => goTo("marches")}
          className="rounded-2xl p-4 flex flex-col items-start gap-4 active:scale-[0.98] transition-transform bg-surface border border-line"
        >
          <TrendingUp size={18} className="text-sun" strokeWidth={2.25} />
          <span className="text-[13.5px] font-semibold text-left text-ink">Prix du marché</span>
        </button>
      </div>

      <div className="rounded-2xl p-4 mb-5 bg-surface border border-line">
        <Eyebrow>Ce mois-ci</Eyebrow>
        <div className="grid grid-cols-3 gap-2">
          <div>
            <p className="font-serif text-[22px] font-bold text-ink">4</p>
            <p className="text-[11px] text-muted">diagnostics</p>
          </div>
          <div>
            <p className="font-serif text-[22px] font-bold text-clay">1</p>
            <p className="text-[11px] text-muted">alerte maladie</p>
          </div>
          <div>
            <p className="font-serif text-[22px] font-bold text-green">+14%</p>
            <p className="text-[11px] text-muted">prix tomate</p>
          </div>
        </div>
      </div>

      <button
        onClick={() => goTo("historique")}
        className="w-full text-left rounded-2xl p-4 flex items-center gap-3 active:scale-[0.99] transition-transform bg-surfaceAlt"
      >
        <div className={`w-10 h-10 rounded-full flex items-center justify-center shrink-0 ${lastTone.bg}`}>
          <lastDiag.icon size={17} className={lastTone.fg} strokeWidth={2.25} />
        </div>
        <div className="flex-1 min-w-0">
          <p className="text-[13px] font-medium truncate text-ink">Dernier diagnostic · {HISTORY[0].date}</p>
          <p className="text-[12px] truncate text-muted">{lastDiag.label}</p>
        </div>
        <ChevronRight size={16} className="text-faint" />
      </button>
    </div>
  );
}
