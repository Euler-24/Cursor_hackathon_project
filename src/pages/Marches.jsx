import React from "react";
import { MapPin, ArrowUp, ArrowDown, Sun as SunIcon } from "lucide-react";
import { MARKETS } from "../data.js";
import { Eyebrow, SectionHeading, Page, Pill } from "../components/UI.jsx";

export default function Marches({ producer }) {
  const bestPrice = Math.max(...MARKETS.map((m) => m.price));

  return (
    <Page>
      <Eyebrow>Prix des marchés voisins</Eyebrow>
      <SectionHeading
        title="Prix du marché"
        subtitle={`${producer.culture.label} — FCFA par kilogramme`}
      />

      <div className="flex flex-col gap-3 lg:grid lg:grid-cols-2">
        {MARKETS.map((m) => {
          const isBest = m.price === bestPrice;
          return (
            <div
              key={m.name}
              className={`rounded-2xl p-4 flex items-center gap-3.5 bg-surface border shadow-card ${
                isBest ? "border-orange/50" : "border-line"
              }`}
            >
              <div className="w-11 h-11 rounded-full flex items-center justify-center shrink-0 bg-orange/15">
                <MapPin size={16} className="text-orange" />
              </div>
              <div className="flex-1 min-w-0">
                <div className="flex items-center gap-2 min-w-0">
                  <p className="text-[14px] font-semibold truncate text-cream">{m.name}</p>
                  {isBest && <Pill tone="sun">meilleur</Pill>}
                </div>
                <p className="text-[12px] text-faint mt-0.5">
                  {m.distance} · mis à jour {m.updated}
                </p>
              </div>
              <div className="text-right shrink-0">
                <p className="font-serif text-[20px] font-semibold tracking-[-0.03em] text-cream">
                  {m.price}
                </p>
                <div className="flex items-center gap-0.5 justify-end mt-0.5">
                  {m.trend === "up" && <ArrowUp size={11} className="text-green" />}
                  {m.trend === "down" && <ArrowDown size={11} className="text-clay" />}
                  <span
                    className={`text-[11.5px] font-medium ${
                      m.trend === "up" ? "text-green" : m.trend === "down" ? "text-clay" : "text-faint"
                    }`}
                  >
                    {m.trend === "flat" ? "stable" : m.trend === "up" ? "en hausse" : "en baisse"}
                  </span>
                </div>
              </div>
            </div>
          );
        })}
      </div>

      <div className="rounded-2xl p-4 flex items-start gap-3 mt-5 bg-sun/15">
        <SunIcon size={15} className="text-sun shrink-0 mt-0.5" />
        <p className="text-[12.5px] leading-relaxed text-muted">
          Ces prix sont indicatifs. Confirmez toujours sur place avant de vendre.
        </p>
      </div>
    </Page>
  );
}
