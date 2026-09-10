/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,jsx}"],
  theme: {
    extend: {
      colors: {
        bg: "#1A130F",
        surface: "#241A14",
        surfaceAlt: "#2C211A",
        surfaceRaised: "#32261E",
        line: "#43362C",
        lineSoft: "#32281F",
        cream: "#F3E6D4",
        ink: "#EDE0CE",
        muted: "#B8A894",
        faint: "#8C7D6C",
        orange: {
          DEFAULT: "#D4865A",
          deep: "#C4733F",
        },
        green: "#8FB37A",
        clay: "#C1583C",
        sun: "#D6A53C",
        sky: "#5C93A8",
      },
      fontFamily: {
        serif: ["Playfair Display", "Georgia", "serif"],
        sans: ["Inter", "system-ui", "sans-serif"],
      },
      borderRadius: {
        "2xl": "1.15rem",
        "3xl": "1.5rem",
      },
      boxShadow: {
        card: "0 1px 0 rgba(243, 230, 212, 0.04), 0 18px 40px -24px rgba(0, 0, 0, 0.55)",
        glow: "0 10px 28px -10px rgba(212, 134, 90, 0.4)",
        nav: "0 -12px 32px -16px rgba(0, 0, 0, 0.55)",
      },
      keyframes: {
        fadeUp: {
          from: { opacity: "0", transform: "translateY(10px)" },
          to: { opacity: "1", transform: "translateY(0)" },
        },
        pulseSoft: {
          "0%, 100%": { opacity: "1" },
          "50%": { opacity: "0.55" },
        },
      },
      animation: {
        "fade-up": "fadeUp 0.45s ease-out both",
        "pulse-soft": "pulseSoft 1.4s ease-in-out infinite",
      },
    },
  },
  plugins: [],
};
