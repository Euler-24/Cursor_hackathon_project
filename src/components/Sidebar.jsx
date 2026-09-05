import React from "react";
import { Home, Camera, CloudSun, TrendingUp, History, User } from "lucide-react";

const ITEMS = [
  { id: "accueil", label: "Accueil", icon: Home },
  { id: "diagnostic", label: "Diagnostic", icon: Camera },
  { id: "meteo", label: "Météo", icon: CloudSun },
  { id: "marches", label: "Marchés", icon: TrendingUp },
  { id: "historique", label: "Historique", icon: History },
];

export default function Sidebar({ view, goTo, producer }) {
  return (
    <aside className="hidden lg:flex w-64 shrink-0 flex-col bg-bg border-r border-lineSoft h-screen sticky top-0">
      <div className="flex items-center gap-3 px-6 py-6 border-b border-lineSoft">
        <div className="w-10 h-10 rounded-full flex items-center justify-center text-[16px] font-serif font-semibold bg-orange-bright text-bg">
          A
        </div>
        <div className="min-w-0">
          <p className="font-serif text-[16px] font-semibold leading-none text-cream">AgriSense</p>
          <p className="text-[10px] font-semibold tracking-[0.14em] mt-1 text-orange-bright truncate">
            {producer.culture.label.toUpperCase()} EDITION
          </p>
        </div>
      </div>

      <nav className="flex-1 px-3 py-5 flex flex-col gap-1">
        {ITEMS.map((it) => {
          const active = view === it.id;
          return (
            <button
              key={it.id}
              onClick={() => goTo(it.id)}
              className={`flex items-center gap-3 px-3 py-2.5 rounded-xl text-[13.5px] font-medium transition-colors ${
                active ? "bg-orange-bright/15 text-orange-bright" : "text-faint hover:bg-surfaceRaised hover:text-cream"
              }`}
            >
              <it.icon size={17} strokeWidth={active ? 2.4 : 2} />
              {it.label}
            </button>
          );
        })}
      </nav>

      <button
        onClick={() => goTo("profil")}
        className="mx-3 mb-5 flex items-center gap-3 px-3 py-3 rounded-xl bg-surfaceRaised border border-lineSoft text-left"
      >
        <div className="w-8 h-8 rounded-full flex items-center justify-center bg-orange-bright/15 shrink-0">
          <User size={15} className="text-orange-bright" />
        </div>
        <div className="min-w-0">
          <p className="text-[12.5px] font-medium truncate text-cream">{producer.name}</p>
          <p className="text-[11px] truncate text-faint">Voir le profil</p>
        </div>
      </button>
    </aside>
  );
}
