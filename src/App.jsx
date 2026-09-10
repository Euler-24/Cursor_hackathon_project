import React, { useState } from "react";
import Sidebar from "./components/Sidebar.jsx";
import TopBar from "./components/TopBar.jsx";
import BottomNav from "./components/BottomNav.jsx";
import Accueil from "./pages/Accueil.jsx";
import Diagnostic from "./pages/Diagnostic.jsx";
import Meteo from "./pages/Meteo.jsx";
import Marches from "./pages/Marches.jsx";
import Historique from "./pages/Historique.jsx";
import Profil from "./pages/Profil.jsx";
import { CULTURES } from "./data.js";

const todayLabel = new Date().toLocaleDateString("fr-FR", {
  weekday: "long",
  day: "numeric",
  month: "long",
});

export default function App() {
  const [view, setView] = useState("accueil");
  const [producer, setProducer] = useState({
    name: "Kouadio Aya",
    region: "Bouaflé, Côte d'Ivoire",
    culture: CULTURES[0],
  });

  const goTo = (v) => setView(v);

  return (
    <div className="w-full min-h-dvh flex bg-bg font-sans text-ink">
      <Sidebar view={view} goTo={goTo} producer={producer} />

      <div className="flex-1 min-w-0 flex flex-col min-h-dvh">
        <TopBar producer={producer} onProfile={() => goTo("profil")} />

        <header className="hidden lg:flex items-center justify-between px-10 py-5 border-b border-lineSoft bg-bg/70 backdrop-blur-md sticky top-0 z-10">
          <p className="text-[13px] capitalize text-muted">{todayLabel}</p>
          <button
            onClick={() => goTo("profil")}
            className="text-[13px] font-medium text-cream px-3.5 py-1.5 rounded-full bg-surfaceRaised border border-line hover:border-orange/40 transition-colors"
          >
            {producer.name}
          </button>
        </header>

        <main className="flex-1 w-full max-w-6xl mx-auto lg:px-10 lg:py-8 safe-bottom">
          {view === "accueil" && <Accueil producer={producer} goTo={goTo} />}
          {view === "diagnostic" && <Diagnostic />}
          {view === "meteo" && <Meteo producer={producer} />}
          {view === "marches" && <Marches producer={producer} />}
          {view === "historique" && <Historique />}
          {view === "profil" && (
            <Profil producer={producer} setProducer={setProducer} close={() => goTo("accueil")} />
          )}
        </main>

        {view !== "profil" && <BottomNav view={view} goTo={goTo} />}
      </div>
    </div>
  );
}
