import React from "react";
import { User } from "lucide-react";

export default function TopBar({ producer, onProfile }) {
  return (
    <div className="lg:hidden sticky top-0 z-20 flex items-center justify-between px-5 py-4 bg-bg border-b border-lineSoft">
      <div className="flex items-center gap-3">
        <div className="w-9 h-9 rounded-full flex items-center justify-center text-[15px] font-serif font-semibold bg-orange text-bg">
          A
        </div>
        <div>
          <p className="font-serif text-[15px] font-semibold leading-none text-cream">AgriSense</p>
          <p className="text-[10px] font-semibold tracking-[0.14em] mt-1 text-orange">
            {producer.culture.label.toUpperCase()} EDITION
          </p>
        </div>
      </div>
      <button
        onClick={onProfile}
        className="w-9 h-9 rounded-full flex items-center justify-center active:scale-95 transition-transform bg-surfaceRaised border border-line"
      >
        <User size={16} className="text-muted" strokeWidth={2} />
      </button>
    </div>
  );
}
