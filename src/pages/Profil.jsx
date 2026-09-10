import React, { useState } from "react";
import { ChevronLeft, User } from "lucide-react";
import { CULTURES } from "../data.js";
import { PrimaryButton, Page } from "../components/UI.jsx";

export default function Profil({ producer, setProducer, close }) {
  const [draft, setDraft] = useState(producer);

  const save = () => {
    setProducer(draft);
    close();
  };

  const fieldClass =
    "w-full rounded-2xl px-4 py-3.5 text-[14px] mb-5 outline-none bg-surface text-cream border border-line focus:border-orange/60 transition-colors";

  return (
    <Page narrow>
      <div className="flex items-center gap-3 mb-8">
        <button
          onClick={close}
          aria-label="Retour"
          className="w-10 h-10 -ml-1 rounded-full flex items-center justify-center text-muted border border-line bg-transparent"
        >
          <ChevronLeft size={19} strokeWidth={2.25} />
        </button>
        <p className="font-serif text-[28px] font-bold tracking-[-0.02em] text-cream">Mon profil</p>
      </div>

      <div className="flex flex-col items-center mb-8">
        <div className="w-16 h-16 rounded-full flex items-center justify-center bg-orange/15 border border-orange/30 mb-3">
          <User size={26} className="text-orange" />
        </div>
        <p className="font-serif text-[18px] font-semibold text-cream">{draft.name}</p>
        <p className="text-[13px] text-muted mt-1">{draft.region}</p>
      </div>

      <label className="text-[11px] font-semibold tracking-[0.14em] block mb-2 text-faint">NOM</label>
      <input
        value={draft.name}
        onChange={(e) => setDraft({ ...draft, name: e.target.value })}
        className={fieldClass}
      />

      <label className="text-[11px] font-semibold tracking-[0.14em] block mb-2 text-faint">RÉGION</label>
      <input
        value={draft.region}
        onChange={(e) => setDraft({ ...draft, region: e.target.value })}
        className={fieldClass}
      />

      <label className="text-[11px] font-semibold tracking-[0.14em] block mb-2 text-faint">
        CULTURE PRINCIPALE
      </label>
      <div className="grid grid-cols-2 sm:grid-cols-3 gap-2 mb-8">
        {CULTURES.map((c) => {
          const active = draft.culture.id === c.id;
          return (
            <button
              key={c.id}
              onClick={() => setDraft({ ...draft, culture: c })}
              className={`rounded-xl py-3 text-[13px] font-semibold transition-transform active:scale-95 border ${
                active ? "bg-orange/15 border-orange text-orange" : "bg-surface border-line text-muted"
              }`}
            >
              {c.label}
            </button>
          );
        })}
      </div>

      <PrimaryButton onClick={save}>Enregistrer</PrimaryButton>
    </Page>
  );
}
