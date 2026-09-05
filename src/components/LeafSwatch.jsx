import React from "react";

const SWATCH_CONFIG = {
  sain: { base: "#3E5C2E", vein: "#6B8F52", spots: [] },
  fongique: {
    base: "#4A5C2E",
    vein: "#6B8F52",
    spots: [
      ["38%", "34%", 6, "#C1583C"],
      ["58%", "56%", 4, "#8A3A26"],
    ],
  },
  hydrique: { base: "#37542F", vein: "#5E8250", drops: true },
  carence: { base: "#8A7A2E", vein: "#B8A23E", spots: [] },
};

export default function LeafSwatch({ type, size = 56 }) {
  const cfg = SWATCH_CONFIG[type] ?? SWATCH_CONFIG.sain;

  return (
    <svg width={size} height={size} viewBox="0 0 56 56" className="rounded-xl block">
      <rect width="56" height="56" rx="14" fill="#F1ECE0" />
      <path d="M28 12c9 2 15 9 15 18 0 6-6 10-15 10s-15-4-15-10c0-9 6-16 15-18z" fill={cfg.base} />
      <path d="M28 14v24" stroke={cfg.vein} strokeWidth="1.4" strokeLinecap="round" />
      <path
        d="M28 20l-6 5M28 20l6 5M28 27l-6 5M28 27l6 5"
        stroke={cfg.vein}
        strokeWidth="1"
        strokeLinecap="round"
      />
      {cfg.spots?.map(([x, y, r, c], i) => (
        <circle key={i} cx={x} cy={y} r={r} fill={c} opacity="0.85" />
      ))}
      {cfg.drops && (
        <>
          <circle cx="22" cy="24" r="2" fill="#9FD3E0" opacity="0.85" />
          <circle cx="33" cy="30" r="1.6" fill="#9FD3E0" opacity="0.85" />
          <circle cx="27" cy="36" r="1.8" fill="#9FD3E0" opacity="0.85" />
        </>
      )}
    </svg>
  );
}
