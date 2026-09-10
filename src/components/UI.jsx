import React from "react";
import { TONE_CLASSES } from "../data.js";

export function LogoMark({ size = "md" }) {
  const box = size === "sm" ? "w-9 h-9 text-[15px]" : "w-10 h-10 text-[17px]";
  return (
    <div
      className={`${box} rounded-full flex items-center justify-center font-serif font-semibold bg-orange text-bg shrink-0`}
    >
      A
    </div>
  );
}

export function Page({ children, narrow }) {
  return (
    <div
      className={`page-enter px-5 pt-6 pb-2 lg:px-0 lg:pt-2 lg:pb-6 ${narrow ? "lg:max-w-xl" : ""}`}
    >
      {children}
    </div>
  );
}

export function Eyebrow({ children }) {
  return (
    <p className="text-[11px] font-semibold tracking-[0.18em] mb-3 text-orange">
      {children.toUpperCase()}
    </p>
  );
}

export function SectionHeading({ title, subtitle, accent }) {
  return (
    <div className="mb-7">
      <h1 className="font-serif text-[clamp(2.15rem,6vw,3.15rem)] font-bold leading-[1.08] tracking-[-0.02em] text-cream">
        <span className="block">{title}</span>
        {accent && <span className="block text-orange">{accent}</span>}
      </h1>
      {subtitle && (
        <p className="text-[16px] mt-4 leading-[1.65] text-muted max-w-xl">{subtitle}</p>
      )}
    </div>
  );
}

export function Pill({ children, tone = "green" }) {
  const s = TONE_CLASSES[tone];
  return (
    <span
      className={`inline-flex items-center gap-1.5 text-[12px] font-medium px-3 py-1 rounded-full ${s.bg} ${s.fg}`}
    >
      {children}
    </span>
  );
}

export function PrimaryButton({ children, onClick, disabled }) {
  return (
    <button
      onClick={onClick}
      disabled={disabled}
      className="w-full rounded-full py-3.5 px-6 text-[15px] font-semibold text-bg bg-orange transition-all duration-200 active:scale-[0.98] disabled:opacity-40 hover:bg-orange-deep"
    >
      {children}
    </button>
  );
}

export function GhostButton({ children, onClick }) {
  return (
    <button
      onClick={onClick}
      className="w-full rounded-full py-3.5 px-6 text-[15px] font-semibold text-cream border border-line bg-transparent transition-all duration-200 active:scale-[0.98] hover:bg-surfaceRaised"
    >
      {children}
    </button>
  );
}

export function Card({ children, className = "", onClick }) {
  const Tag = onClick ? "button" : "div";
  return (
    <Tag
      onClick={onClick}
      className={`rounded-2xl bg-surface border border-line ${
        onClick
          ? "w-full text-left card-hover active:scale-[0.99] transition-transform"
          : ""
      } ${className}`}
    >
      {children}
    </Tag>
  );
}
