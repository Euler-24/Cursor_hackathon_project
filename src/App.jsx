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

export default function App() {
  const [view, setView] = useState("accueil");
  const [producer, setProducer] = useState({
    name: "Kouadio Aya",
    region: "Bouaflé, Côte d'Ivoire",
    culture: CULTURES[0],
  });

  const goTo = (v) => setView(v);

  return (
    <div className="w-full min-h-screen flex bg-paper font-sans">
      <Sidebar view={view} goTo={goTo} producer={producer} />

      <div className="flex-1 min-w-0 flex flex-col">
        <TopBar producer={producer} onProfile={() => goTo("profil")} />

        <div className="flex-1 w-full max-w-6xl mx-auto lg:px-8 lg:py-4">
          {view === "accueil" && <Accueil producer={producer} goTo={goTo} />}
          {view === "diagnostic" && <Diagnostic />}
          {view === "meteo" && <Meteo producer={producer} />}
          {view === "marches" && <Marches producer={producer} />}
          {view === "historique" && <Historique />}
          {view === "profil" && (
            <Profil producer={producer} setProducer={setProducer} close={() => goTo("accueil")} />
          )}
        </div>

        {view !== "profil" && <BottomNav view={view} goTo={goTo} />}
      </div>
    </div>
  );
}
