import React from "react";
import { Home, Camera, CloudSun, TrendingUp, History, User } from "lucide-react";
import { LogoMark } from "./UI.jsx";

const ITEMS = [
  { id: "accueil", label: "Accueil", icon: Home },
  { id: "diagnostic", label: "Diagnostic", icon: Camera },
  { id: "meteo", label: "Météo", icon: CloudSun },
  { id: "marches", label: "Marchés", icon: TrendingUp },
  { id: "historique", label: "Historique", icon: History },
];

export default function Sidebar({ view, goTo, producer }) {
  return (
    <aside className="hidden lg:flex w-[272px] shrink-0 flex-col bg-bg/80 border-r border-lineSoft h-screen sticky top-0">
      <div className="flex items-center gap-3 px-6 py-7">
        <LogoMark />
        <div className="min-w-0">
          <p className="font-serif text-[18px] font-semibold leading-none tracking-[-0.02em] text-cream">
            AgriSense
          </p>
          <p className="text-[10px] font-semibold tracking-[0.16em] mt-1.5 text-orange truncate">
            {producer.culture.label.toUpperCase()} EDITION
          </p>
        </div>
      </div>

      <nav className="flex-1 px-3 py-2 flex flex-col gap-1" aria-label="Navigation principale">
        {ITEMS.map((it) => {
          const active = view === it.id;
          return (
            <button
              key={it.id}
              onClick={() => goTo(it.id)}
              className={`relative flex items-center gap-3 px-3.5 py-2.5 rounded-xl text-[13.5px] font-medium transition-colors ${
                active
                  ? "bg-orange/15 text-orange"
                  : "text-faint hover:bg-surfaceRaised hover:text-cream"
              }`}
            >
              {active && (
                <span className="absolute left-0 top-1/2 -translate-y-1/2 w-[3px] h-5 rounded-full bg-orange" />
              )}
              <it.icon size={17} strokeWidth={active ? 2.4 : 2} />
              {it.label}
            </button>
          );
        })}
      </nav>

      <button
        onClick={() => goTo("profil")}
        className="mx-3 mb-6 flex items-center gap-3 px-3 py-3 rounded-2xl bg-surfaceRaised border border-lineSoft text-left card-hover"
      >
        <div className="w-9 h-9 rounded-full flex items-center justify-center bg-orange/15 shrink-0">
          <User size={15} className="text-orange" />
        </div>
        <div className="min-w-0">
          <p className="text-[13px] font-semibold truncate text-cream">{producer.name}</p>
          <p className="text-[11.5px] truncate text-faint">Voir le profil</p>
        </div>
      </button>
    </aside>
  );
}
