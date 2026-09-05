import React, { useState } from "react";
import { ChevronLeft } from "lucide-react";
import { CULTURES } from "../data.js";
import { PrimaryButton } from "../components/UI.jsx";

export default function Profil({ producer, setProducer, close }) {
  const [draft, setDraft] = useState(producer);

  const save = () => {
    setProducer(draft);
    close();
  };

  const fieldClass =
    "w-full rounded-xl px-4 py-3 text-[13.5px] mb-4 outline-none bg-surface text-ink border border-line";

  return (
    <div className="px-5 pt-6 pb-4 lg:px-0 lg:pt-6 lg:pb-10 lg:max-w-md">
      <div className="flex items-center gap-3 mb-6">
        <button onClick={close} className="w-8 h-8 -ml-1 rounded-full flex items-center justify-center text-muted">
          <ChevronLeft size={19} strokeWidth={2.25} />
        </button>
        <p className="font-serif text-[15px] font-semibold text-ink">Mon profil</p>
      </div>

      <label className="text-[11px] font-semibold tracking-[0.1em] block mb-2 text-faint">NOM</label>
      <input
        value={draft.name}
        onChange={(e) => setDraft({ ...draft, name: e.target.value })}
        className={fieldClass}
      />

      <label className="text-[11px] font-semibold tracking-[0.1em] block mb-2 text-faint">RÉGION</label>
      <input
        value={draft.region}
        onChange={(e) => setDraft({ ...draft, region: e.target.value })}
        className={fieldClass}
      />

      <label className="text-[11px] font-semibold tracking-[0.1em] block mb-2 text-faint">CULTURE PRINCIPALE</label>
      <div className="grid grid-cols-3 gap-2 mb-6">
        {CULTURES.map((c) => {
          const active = draft.culture.id === c.id;
          return (
            <button
              key={c.id}
              onClick={() => setDraft({ ...draft, culture: c })}
              className={`rounded-xl py-3 text-[12px] font-medium transition-transform active:scale-95 border ${
                active ? "bg-orange/15 border-orange text-orange" : "bg-surface border-line text-muted"
              }`}
            >
              {c.label}
            </button>
          );
        })}
      </div>

      <PrimaryButton onClick={save}>Enregistrer</PrimaryButton>
    </div>
  );
}
