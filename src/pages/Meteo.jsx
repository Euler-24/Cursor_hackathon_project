import React from "react";
import { AlertTriangle, Droplets, Wind, Sun as SunIcon } from "lucide-react";
import { FORECAST } from "../data.js";
import { Eyebrow, SectionHeading, Page } from "../components/UI.jsx";

export default function Meteo({ producer }) {
  return (
    <Page>
      <Eyebrow>Météo locale</Eyebrow>
      <SectionHeading title="Météo" subtitle={producer.region} />

      <div className="lg:grid lg:grid-cols-2 lg:gap-6 lg:items-start">
        <div className="rounded-3xl p-6 mb-5 lg:mb-0 bg-surface border border-line shadow-card">
          <div className="flex items-center justify-between gap-4">
            <div>
              <p className="text-[12px] font-medium tracking-[0.12em] uppercase text-faint">
                Aujourd'hui
              </p>
              <p className="font-serif text-[52px] font-bold leading-none mt-2 tracking-[-0.04em] text-cream">
                31°
              </p>
              <p className="text-[14px] mt-2.5 text-muted">Ensoleillé, léger vent</p>
            </div>
            <div className="w-16 h-16 rounded-full bg-sun/15 flex items-center justify-center shrink-0">
              <SunIcon size={36} className="text-sun" strokeWidth={1.5} />
            </div>
          </div>
          <div className="flex items-center gap-5 mt-5 pt-5 border-t border-line">
            <div className="flex items-center gap-1.5">
              <Droplets size={14} className="text-faint" />
              <span className="text-[13px] text-muted">Pluie 5%</span>
            </div>
            <div className="flex items-center gap-1.5">
              <Wind size={14} className="text-faint" />
              <span className="text-[13px] text-muted">12 km/h</span>
            </div>
          </div>

          <div className="rounded-2xl p-4 mt-5 flex items-start gap-3 bg-sky/10">
            <AlertTriangle size={18} className="text-sky shrink-0 mt-0.5" />
            <div>
              <p className="text-[14px] font-semibold text-sky">Alerte pluie mercredi</p>
              <p className="text-[13px] mt-1 leading-relaxed text-muted">
                80% de risque de pluie forte. Terminez les traitements avant mardi soir.
              </p>
            </div>
          </div>
        </div>

        <div>
          <Eyebrow>Les 5 prochains jours</Eyebrow>
          <div className="rounded-2xl overflow-hidden bg-surface border border-line shadow-card">
            {FORECAST.map((f, i) => (
              <div
                key={f.day}
                className={`flex items-center gap-3 px-4 py-3.5 ${i > 0 ? "border-t border-lineSoft" : ""}`}
              >
                <span className="text-[13.5px] w-[92px] font-medium text-cream">{f.day}</span>
                <f.icon size={17} className={f.rain > 50 ? "text-sky" : "text-sun"} />
                <div className="flex-1 h-1.5 rounded-full bg-line overflow-hidden">
                  <div
                    className="h-full rounded-full bg-sky"
                    style={{ width: `${Math.max(f.rain, 6)}%` }}
                  />
                </div>
                <span className="text-[12px] w-14 text-right text-muted">{f.rain}%</span>
                <span className="text-[15px] font-semibold w-10 text-right text-cream">{f.temp}°</span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </Page>
  );
}
