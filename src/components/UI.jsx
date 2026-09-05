import React from "react";
import { TONE_CLASSES } from "../data.js";

export function Eyebrow({ children }) {
  return (
    <p className="text-[10.5px] font-semibold tracking-[0.14em] mb-3 text-faint">
      {children.toUpperCase()}
    </p>
  );
}

export function SectionHeading({ title, subtitle }) {
  return (
    <div className="mb-6">
      <h1 className="font-serif text-[30px] font-bold leading-[1.08] text-ink">{title}</h1>
      {subtitle && <p className="text-[13.5px] mt-3 leading-relaxed text-muted">{subtitle}</p>}
    </div>
  );
}

export function Pill({ children, tone = "green" }) {
  const s = TONE_CLASSES[tone];
  return (
    <span className={`inline-flex items-center gap-1 text-[11px] font-medium px-2.5 py-1 rounded-full ${s.bg} ${s.fg}`}>
      {children}
    </span>
  );
}

export function PrimaryButton({ children, onClick, disabled }) {
  return (
    <button
      onClick={onClick}
      disabled={disabled}
      className="w-full rounded-full py-3.5 text-[14px] font-semibold text-white bg-orange transition-transform active:scale-[0.99] disabled:opacity-40 hover:bg-orange-deep"
    >
      {children}
    </button>
  );
}
