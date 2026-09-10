import React from "react";
import { ChevronRight, CloudRain } from "lucide-react";
import { DIAGNOSES, HISTORY, TONE_CLASSES } from "../data.js";
import { Eyebrow, SectionHeading, Card, Page, PrimaryButton, GhostButton } from "../components/UI.jsx";

export default function Accueil({ producer, goTo }) {
  const lastDiag = DIAGNOSES.find((d) => d.id === HISTORY[0].result);
  const lastTone = TONE_CLASSES[lastDiag.tone];
  const firstName = producer.name.split(" ")[0];

  return (
    <Page>
      <div className="inline-flex items-center gap-2 rounded-full px-3 py-1 mb-5 bg-green/15">
        <span className="w-1.5 h-1.5 rounded-full bg-green" />
        <span className="text-[12px] font-medium text-green">
          Assistant agricole · {producer.region}
        </span>
      </div>

      <SectionHeading
        title={`Bonjour, ${firstName}.`}
        accent="Prenez la photo."
        subtitle={`${producer.region} — parcelles de ${producer.culture.label.toLowerCase()}. Détection des symptômes, conseils simples, météo et prix des marchés voisins.`}
      />

      <div className="flex flex-col gap-3 max-w-sm mb-8">
        <PrimaryButton onClick={() => goTo("diagnostic")}>Diagnostiquer une photo</PrimaryButton>
        <GhostButton onClick={() => goTo("marches")}>Voir les marchés</GhostButton>
      </div>

      <Card onClick={() => goTo("meteo")} className="p-4 mb-5 flex items-start gap-3.5">
        <div className="w-11 h-11 rounded-full flex items-center justify-center shrink-0 bg-sky/15">
          <CloudRain size={18} className="text-sky" />
        </div>
        <div className="flex-1 min-w-0">
          <p className="text-[14px] font-semibold text-cream">Fortes pluies attendues mercredi</p>
          <p className="text-[13px] mt-1 text-muted leading-relaxed">
            Évitez d'arroser le feuillage d'ici là.
          </p>
        </div>
        <ChevronRight size={16} className="text-faint shrink-0 mt-2" />
      </Card>

      <div className="mb-6">
        <Eyebrow>Ce mois-ci</Eyebrow>
        <div className="grid grid-cols-3 gap-4">
          <div>
            <p className="font-serif text-[28px] font-bold tracking-[-0.03em] text-cream">4</p>
            <p className="text-[12px] mt-1 text-muted leading-snug">diagnostics</p>
          </div>
          <div>
            <p className="font-serif text-[28px] font-bold tracking-[-0.03em] text-cream">1</p>
            <p className="text-[12px] mt-1 text-muted leading-snug">alerte maladie</p>
          </div>
          <div>
            <p className="font-serif text-[28px] font-bold tracking-[-0.03em] text-cream">+14%</p>
            <p className="text-[12px] mt-1 text-muted leading-snug">prix tomate</p>
          </div>
        </div>
      </div>

      <Card onClick={() => goTo("historique")} className="p-4 flex items-center gap-3.5">
        <div className={`w-11 h-11 rounded-full flex items-center justify-center shrink-0 ${lastTone.bg}`}>
          <lastDiag.icon size={18} className={lastTone.fg} strokeWidth={2.25} />
        </div>
        <div className="flex-1 min-w-0">
          <p className="text-[13.5px] font-semibold truncate text-cream">
            Dernier diagnostic · {HISTORY[0].date}
          </p>
          <p className="text-[12.5px] truncate text-muted mt-0.5">{lastDiag.label}</p>
        </div>
        <ChevronRight size={16} className="text-faint" />
      </Card>
    </Page>
  );
}
