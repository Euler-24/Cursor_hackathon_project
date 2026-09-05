import React from "react";
import { DIAGNOSES, HISTORY, TONE_CLASSES } from "../data.js";
import { Eyebrow, SectionHeading, Pill } from "../components/UI.jsx";

export default function Historique() {
  return (
    <div className="px-5 pt-6 pb-4 lg:px-0 lg:pt-6 lg:pb-10">
      <Eyebrow>Suivi de vos parcelles</Eyebrow>
      <SectionHeading title="Historique" subtitle="Vos diagnostics passés, du plus récent au plus ancien." />

      <div className="flex flex-col gap-2.5 lg:grid lg:grid-cols-2 lg:gap-3">
        {HISTORY.map((h, i) => {
          const d = DIAGNOSES.find((x) => x.id === h.result);
          const tone = TONE_CLASSES[d.tone];
          return (
            <div key={i} className="rounded-2xl p-4 flex items-center gap-3 bg-surface border border-line">
              <div className={`w-10 h-10 rounded-full flex items-center justify-center shrink-0 ${tone.bg}`}>
                <d.icon size={16} className={tone.fg} strokeWidth={2.25} />
              </div>
              <div className="flex-1 min-w-0">
                <p className="text-[13px] font-medium truncate text-ink">{d.label}</p>
                <p className="text-[11.5px] text-faint">{h.date} · {h.parcelle}</p>
              </div>
              <Pill tone={d.tone}>{h.culture}</Pill>
            </div>
          );
        })}
      </div>
    </div>
  );
}
