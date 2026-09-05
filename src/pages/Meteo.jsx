import React from "react";
import { AlertTriangle, Droplets, Wind, Sun as SunIcon } from "lucide-react";
import { FORECAST } from "../data.js";
import { Eyebrow, SectionHeading } from "../components/UI.jsx";

export default function Meteo({ producer }) {
  return (
    <div className="px-5 pt-6 pb-4 lg:px-0 lg:pt-6 lg:pb-10">
      <Eyebrow>Météo locale</Eyebrow>
      <SectionHeading title="Météo" subtitle={producer.region} />

      <div className="lg:grid lg:grid-cols-2 lg:gap-6 lg:items-start">
        <div className="rounded-2xl p-5 mb-4 lg:mb-0 bg-surface border border-line">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-[12px] text-faint">Aujourd'hui</p>
              <p className="font-serif text-[40px] font-bold leading-none mt-1.5 text-ink">31°C</p>
              <p className="text-[12.5px] mt-2 text-muted">Ensoleillé, léger vent</p>
            </div>
            <SunIcon size={42} className="text-sun" strokeWidth={1.5} />
          </div>
          <div className="flex items-center gap-4 mt-4 pt-4 border-t border-line">
            <div className="flex items-center gap-1.5">
              <Droplets size={13} className="text-faint" />
              <span className="text-[12px] text-muted">Pluie 5%</span>
            </div>
            <div className="flex items-center gap-1.5">
              <Wind size={13} className="text-faint" />
              <span className="text-[12px] text-muted">12 km/h</span>
            </div>
          </div>

          <div className="rounded-xl p-4 mt-4 flex items-start gap-3 bg-sky/10">
            <AlertTriangle size={17} className="text-sky shrink-0 mt-0.5" />
            <div>
              <p className="text-[13px] font-medium text-sky">Alerte pluie mercredi</p>
              <p className="text-[12px] mt-1 text-muted">
                80% de risque de pluie forte. Terminez les traitements avant mardi soir.
              </p>
            </div>
          </div>
        </div>

        <div>
          <Eyebrow>Les 5 prochains jours</Eyebrow>
          <div className="rounded-2xl overflow-hidden bg-surface border border-line">
            {FORECAST.map((f, i) => (
              <div
                key={f.day}
                className={`flex items-center justify-between px-4 py-3.5 ${i > 0 ? "border-t border-line" : ""}`}
              >
                <span className="text-[13px] w-24 text-ink">{f.day}</span>
                <f.icon size={16} className={f.rain > 50 ? "text-sky" : "text-sun"} />
                <span className="text-[12px] w-16 text-right text-muted">{f.rain}% pluie</span>
                <span className="text-[13.5px] font-semibold w-10 text-right text-ink">{f.temp}°</span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
