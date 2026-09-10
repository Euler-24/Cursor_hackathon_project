import React, { useState, useRef } from "react";
import { Upload, Phone } from "lucide-react";
import { DIAGNOSES, TONE_CLASSES } from "../data.js";
import { Eyebrow, SectionHeading, PrimaryButton, Page } from "../components/UI.jsx";
import LeafSwatch from "../components/LeafSwatch.jsx";

const SHORT_LABELS = {
  sain: "Saine",
  fongique: "Champignon",
  hydrique: "Humidité",
  carence: "Carence",
};

export default function Diagnostic() {
  const [step, setStep] = useState(1);
  const [image, setImage] = useState(null);
  const [selectedDemo, setSelectedDemo] = useState(null);
  const [result, setResult] = useState(null);
  const fileRef = useRef(null);

  const handleFile = (e) => {
    const file = e.target.files?.[0];
    if (!file) return;
    setSelectedDemo(null);
    setImage(URL.createObjectURL(file));
  };

  const pickDemo = (d) => {
    setImage(null);
    setSelectedDemo(d.id);
  };

  const analyze = () => {
    setStep(2);
    setTimeout(() => {
      const outcome = selectedDemo
        ? DIAGNOSES.find((d) => d.id === selectedDemo)
        : DIAGNOSES[Math.floor(Math.random() * DIAGNOSES.length)];
      setResult(outcome);
      setStep(3);
    }, 1200);
  };

  const reset = () => {
    setStep(1);
    setImage(null);
    setSelectedDemo(null);
    setResult(null);
  };

  return (
    <Page narrow>
      <Eyebrow>Diagnostic par photo</Eyebrow>
      <SectionHeading
        title="Diagnostic par photo"
        subtitle="Importez une photo nette d'une feuille ou d'un fruit, ou choisissez un cas de démonstration."
      />

      {step === 1 && (
        <>
          <button
            type="button"
            onClick={() => fileRef.current?.click()}
            className="w-full rounded-2xl flex flex-col items-center justify-center gap-3 cursor-pointer active:scale-[0.99] transition-transform mb-6 h-[168px] border border-dashed border-line bg-surface/60 overflow-hidden"
          >
            {image ? (
              <img src={image} alt="Photo importée" className="w-full h-full object-cover" />
            ) : (
              <>
                <span className="w-11 h-11 rounded-full bg-orange/15 flex items-center justify-center">
                  <Upload size={18} className="text-orange" strokeWidth={2.25} />
                </span>
                <div className="text-center px-4">
                  <p className="text-[14px] font-semibold text-orange">Importer une photo</p>
                  <p className="text-[12px] text-faint mt-1">JPG ou PNG, feuille bien cadrée</p>
                </div>
              </>
            )}
          </button>
          <input ref={fileRef} type="file" accept="image/*" onChange={handleFile} className="hidden" />

          <Eyebrow>Cas de démonstration</Eyebrow>
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 mb-7">
            {DIAGNOSES.map((d) => (
              <button
                key={d.id}
                onClick={() => pickDemo(d)}
                className={`rounded-2xl overflow-hidden p-1.5 bg-surface border transition-transform active:scale-95 ${
                  selectedDemo === d.id ? "border-orange" : "border-line"
                }`}
              >
                <LeafSwatch type={d.id} size={72} />
                <p className="text-[11px] font-medium text-center mt-1.5 mb-0.5 text-muted">
                  {SHORT_LABELS[d.id]}
                </p>
              </button>
            ))}
          </div>

          <PrimaryButton onClick={analyze} disabled={!image && !selectedDemo}>
            Analyser la photo
          </PrimaryButton>
        </>
      )}

      {step === 2 && (
        <div className="rounded-2xl flex flex-col items-center justify-center gap-4 py-20 bg-surface border border-line shadow-card">
          <div className="w-10 h-10 rounded-full animate-spin border-[3px] border-line border-t-orange" />
          <p className="text-[14px] font-medium text-cream animate-pulse-soft">Analyse de la photo…</p>
        </div>
      )}

      {step === 3 && result && <ResultCard result={result} image={image} onReset={reset} />}
    </Page>
  );
}

function ResultCard({ result, image, onReset }) {
  const tone = TONE_CLASSES[result.tone];
  return (
    <div>
      <div className="rounded-2xl overflow-hidden mb-6 border border-line shadow-card">
        {image ? (
          <img src={image} alt="Feuille analysée" className="w-full h-40 object-cover" />
        ) : (
          <div className="w-full h-40 flex items-center justify-center bg-surfaceAlt">
            <LeafSwatch type={result.id} size={72} />
          </div>
        )}
        <div className={`p-4 ${tone.bg}`}>
          <div className="flex items-center gap-2 mb-1.5">
            <result.icon size={17} className={tone.fg} strokeWidth={2.25} />
            <p className={`text-[15px] font-semibold ${tone.fg}`}>{result.label}</p>
          </div>
          <p className="text-[13px] leading-relaxed text-muted">{result.summary}</p>
        </div>
      </div>

      <Eyebrow>Ce que vous pouvez faire</Eyebrow>
      <div className="flex flex-col gap-2.5 mb-5">
        {result.advice.map((a, i) => (
          <div key={i} className="flex items-start gap-3 rounded-xl p-3.5 bg-surface border border-line">
            <div className="w-1.5 h-1.5 rounded-full mt-1.5 shrink-0 bg-orange" />
            <p className="text-[13px] leading-relaxed text-ink">{a}</p>
          </div>
        ))}
      </div>

      <div className="rounded-xl p-3.5 flex items-center gap-3 mb-5 bg-orange/15">
        <Phone size={15} className="text-orange shrink-0" />
        <p className="text-[12px] leading-relaxed text-muted">
          Première orientation, pas un diagnostic médical. En cas de doute, contactez un agent agricole.
        </p>
      </div>

      <PrimaryButton onClick={onReset}>Nouveau diagnostic</PrimaryButton>
    </div>
  );
}
