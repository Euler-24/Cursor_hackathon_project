import React from "react";
import { DIAGNOSES, HISTORY, TONE_CLASSES } from "../data.js";
import { Eyebrow, SectionHeading, Pill, Page } from "../components/UI.jsx";

export default function Historique() {
  return (
    <Page>
      <Eyebrow>Suivi de vos parcelles</Eyebrow>
      <SectionHeading title="Historique" subtitle="Vos diagnostics passés, du plus récent au plus ancien." />

      <div className="flex flex-col gap-3 lg:grid lg:grid-cols-2">
        {HISTORY.map((h, i) => {
          const d = DIAGNOSES.find((x) => x.id === h.result);
          const tone = TONE_CLASSES[d.tone];
          return (
            <div
              key={i}
              className="rounded-2xl p-4 flex items-center gap-3.5 bg-surface border border-line shadow-card"
            >
              <div className={`w-11 h-11 rounded-2xl flex items-center justify-center shrink-0 ${tone.bg}`}>
                <d.icon size={17} className={tone.fg} strokeWidth={2.25} />
              </div>
              <div className="flex-1 min-w-0">
                <p className="text-[14px] font-semibold truncate text-cream">{d.label}</p>
                <p className="text-[12px] text-faint mt-0.5">
                  {h.date} · {h.parcelle}
                </p>
              </div>
              <Pill tone={d.tone}>{h.culture}</Pill>
            </div>
          );
        })}
      </div>
    </Page>
  );
}
