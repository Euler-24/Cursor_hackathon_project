import React from "react";
import { Home, Camera, CloudSun, TrendingUp, History } from "lucide-react";

const ITEMS = [
  { id: "accueil", label: "Accueil", icon: Home },
  { id: "diagnostic", label: "Diagnostic", icon: Camera },
  { id: "meteo", label: "Météo", icon: CloudSun },
  { id: "marches", label: "Marchés", icon: TrendingUp },
  { id: "historique", label: "Historique", icon: History },
];

export default function BottomNav({ view, goTo }) {
  return (
    <div className="lg:hidden sticky bottom-0 flex items-center justify-around px-2 pt-2 pb-3 bg-surfaceRaised border-t border-lineSoft">
      {ITEMS.map((it) => {
        const active = view === it.id;
        return (
          <button
            key={it.id}
            onClick={() => goTo(it.id)}
            className="flex flex-col items-center gap-1.5 px-2 py-1 flex-1"
          >
            <it.icon size={18} strokeWidth={active ? 2.4 : 2} className={active ? "text-orange" : "text-faint"} />
            <span className={`text-[10px] font-medium ${active ? "text-orange" : "text-faint"}`}>{it.label}</span>
          </button>
        );
      })}
    </div>
  );
}
