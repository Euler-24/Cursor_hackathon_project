import React from "react";
import { MapPin, ArrowUp, ArrowDown, Sun as SunIcon } from "lucide-react";
import { MARKETS } from "../data.js";
import { Eyebrow, SectionHeading } from "../components/UI.jsx";

export default function Marches({ producer }) {
  return (
    <div className="px-5 pt-6 pb-4 lg:px-0 lg:pt-6 lg:pb-10">
      <Eyebrow>Prix des marchés voisins</Eyebrow>
      <SectionHeading title="Prix du marché" subtitle={`${producer.culture.label} — FCFA par kilogramme`} />

      <div className="flex flex-col gap-2.5 lg:grid lg:grid-cols-2 lg:gap-3">
        {MARKETS.map((m) => (
          <div key={m.name} className="rounded-2xl p-4 flex items-center gap-3 bg-surface border border-line">
            <div className="w-10 h-10 rounded-full flex items-center justify-center shrink-0 bg-orange/15">
              <MapPin size={15} className="text-orange" />
            </div>
            <div className="flex-1 min-w-0">
              <p className="text-[13px] font-medium truncate text-ink">{m.name}</p>
              <p className="text-[11.5px] text-faint">{m.distance} · mis à jour {m.updated}</p>
            </div>
            <div className="text-right shrink-0">
              <p className="font-serif text-[16px] font-bold text-ink">{m.price}</p>
              <div className="flex items-center gap-0.5 justify-end">
                {m.trend === "up" && <ArrowUp size={11} className="text-green" />}
                {m.trend === "down" && <ArrowDown size={11} className="text-clay" />}
                <span
                  className={`text-[11px] ${
                    m.trend === "up" ? "text-green" : m.trend === "down" ? "text-clay" : "text-faint"
                  }`}
                >
                  {m.trend === "flat" ? "stable" : m.trend === "up" ? "en hausse" : "en baisse"}
                </span>
              </div>
            </div>
          </div>
        ))}
      </div>

      <div className="rounded-xl p-3.5 flex items-start gap-2.5 mt-4 bg-sun/15">
        <SunIcon size={14} className="text-sun shrink-0 mt-0.5" />
        <p className="text-[11.5px] text-muted">
          Ces prix sont indicatifs. Confirmez toujours sur place avant de vendre.
        </p>
      </div>
    </div>
  );
}
