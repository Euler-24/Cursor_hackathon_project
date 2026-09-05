import React, { useState, useRef } from "react";
import { Upload, Phone } from "lucide-react";
import { DIAGNOSES, TONE_CLASSES } from "../data.js";
import { Eyebrow, SectionHeading, PrimaryButton } from "../components/UI.jsx";
import LeafSwatch from "../components/LeafSwatch.jsx";

export default function Diagnostic() {
  const [step, setStep] = useState(1); // 1 = choix, 2 = analyse, 3 = résultat
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
    <div className="px-5 pt-6 pb-4 lg:px-0 lg:pt-6 lg:pb-10 lg:max-w-xl">
      <Eyebrow>Diagnostic par photo</Eyebrow>
      <SectionHeading
        title="Diagnostic par photo"
        subtitle="Importez une photo nette d'une feuille ou d'un fruit, ou choisissez un cas de démonstration."
      />

      {step === 1 && (
        <>
          <div
            onClick={() => fileRef.current?.click()}
            className="rounded-2xl flex flex-col items-center justify-center gap-3 cursor-pointer active:scale-[0.99] transition-transform mb-5 h-[150px] border border-dashed border-line overflow-hidden"
          >
            {image ? (
              <img src={image} alt="Photo importée" className="w-full h-full object-cover rounded-2xl" />
            ) : (
              <>
                <Upload size={18} className="text-orange" strokeWidth={2.25} />
                <p className="text-[13.5px] font-medium text-orange">Importer une photo</p>
              </>
            )}
          </div>
          <input ref={fileRef} type="file" accept="image/*" onChange={handleFile} className="hidden" />

          <Eyebrow>Cas de démonstration</Eyebrow>
          <div className="grid grid-cols-4 gap-2.5 mb-6">
            {DIAGNOSES.map((d) => (
              <button
                key={d.id}
                onClick={() => pickDemo(d)}
                className={`rounded-xl overflow-hidden transition-transform active:scale-95 outline outline-2 outline-offset-2 ${
                  selectedDemo === d.id ? "outline-orange" : "outline-transparent"
                }`}
              >
                <LeafSwatch type={d.id} size={72} />
              </button>
            ))}
          </div>

          <PrimaryButton onClick={analyze} disabled={!image && !selectedDemo}>
            Analyser la photo
          </PrimaryButton>
        </>
      )}

      {step === 2 && (
        <div className="rounded-2xl flex flex-col items-center justify-center gap-3 py-16 bg-surface border border-line">
          <div className="w-9 h-9 rounded-full animate-spin border-[3px] border-line border-t-orange" />
          <p className="text-[13px] font-medium text-ink">Analyse de la photo…</p>
        </div>
      )}

      {step === 3 && result && (
        <ResultCard result={result} image={image} onReset={reset} />
      )}
    </div>
  );
}

function ResultCard({ result, image, onReset }) {
  const tone = TONE_CLASSES[result.tone];
  return (
    <div>
      <div className="rounded-2xl overflow-hidden mb-5 border border-line">
        {image ? (
          <img src={image} alt="Feuille analysée" className="w-full h-32 object-cover" />
        ) : (
          <div className="w-full h-32 flex items-center justify-center bg-surfaceAlt">
            <LeafSwatch type={result.id} size={64} />
          </div>
        )}
        <div className={`p-4 ${tone.bg}`}>
          <div className="flex items-center gap-2 mb-1.5">
            <result.icon size={17} className={tone.fg} strokeWidth={2.25} />
            <p className={`text-[13.5px] font-semibold ${tone.fg}`}>{result.label}</p>
          </div>
          <p className="text-[12.5px] text-muted">{result.summary}</p>
        </div>
      </div>

      <Eyebrow>Ce que vous pouvez faire</Eyebrow>
      <div className="flex flex-col gap-2 mb-5">
        {result.advice.map((a, i) => (
          <div key={i} className="flex items-start gap-2.5 rounded-xl p-3 bg-surface border border-line">
            <div className="w-1.5 h-1.5 rounded-full mt-1.5 shrink-0 bg-orange" />
            <p className="text-[12.5px] leading-snug text-ink">{a}</p>
          </div>
        ))}
      </div>

      <div className="rounded-xl p-3.5 flex items-center gap-3 mb-4 bg-orange/15">
        <Phone size={15} className="text-orange shrink-0" />
        <p className="text-[11.5px] text-muted">
          Première orientation, pas un diagnostic médical. En cas de doute, contactez un agent agricole.
        </p>
      </div>

      <PrimaryButton onClick={onReset}>Nouveau diagnostic</PrimaryButton>
    </div>
  );
}
