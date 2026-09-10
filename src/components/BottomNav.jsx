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
    <nav
      aria-label="Navigation mobile"
      className="lg:hidden fixed bottom-0 inset-x-0 z-20 px-3 pb-[max(0.6rem,env(safe-area-inset-bottom))] pt-2 pointer-events-none"
    >
      <div className="pointer-events-auto flex items-center justify-around px-1.5 py-1.5 rounded-2xl bg-surfaceRaised/95 backdrop-blur-md border border-line shadow-nav">
        {ITEMS.map((it) => {
          const active = view === it.id;
          return (
            <button
              key={it.id}
              onClick={() => goTo(it.id)}
              className={`flex flex-col items-center gap-1 px-2 py-2 flex-1 rounded-xl transition-colors ${
                active ? "bg-orange/15" : ""
              }`}
            >
              <it.icon
                size={18}
                strokeWidth={active ? 2.4 : 2}
                className={active ? "text-orange" : "text-faint"}
              />
              <span
                className={`text-[10px] font-semibold tracking-[-0.01em] ${
                  active ? "text-orange" : "text-faint"
                }`}
              >
                {it.label}
              </span>
            </button>
          );
        })}
      </div>
    </nav>
  );
}
