import React from "react";
import { User } from "lucide-react";
import { LogoMark } from "./UI.jsx";

export default function TopBar({ producer, onProfile }) {
  return (
    <header className="lg:hidden sticky top-0 z-20 flex items-center justify-between px-5 py-3.5 bg-bg/85 backdrop-blur-md border-b border-lineSoft">
      <div className="flex items-center gap-3 min-w-0">
        <LogoMark size="sm" />
        <div className="min-w-0">
          <p className="font-serif text-[16px] font-semibold leading-none tracking-[-0.02em] text-cream">
            AgriSense
          </p>
          <p className="text-[10px] font-semibold tracking-[0.16em] mt-1.5 text-orange truncate">
            {producer.culture.label.toUpperCase()} EDITION
          </p>
        </div>
      </div>
      <button
        onClick={onProfile}
        aria-label="Ouvrir le profil"
        className="w-10 h-10 rounded-full flex items-center justify-center active:scale-95 transition-transform border border-line bg-transparent shrink-0"
      >
        <User size={16} className="text-muted" strokeWidth={2} />
      </button>
    </header>
  );
}
