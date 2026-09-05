/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,jsx}"],
  theme: {
    extend: {
      colors: {
        bg: "#170F09",
        surface: "#221912",
        surfaceAlt: "#2A2016",
        surfaceRaised: "#2F2419",
        line: "#3C2F21",
        lineSoft: "#2E2418",
        cream: "#F4EAD9",
        ink: "#E3D7C4",
        muted: "#A99C87",
        faint: "#7C6F5C",
        orange: {
          DEFAULT: "#E2854F",
          deep: "#C96B39",
        },
        green: "#84A96E",
        clay: "#C1583C",
        sun: "#D6A53C",
        sky: "#5C93A8",
      },
      fontFamily: {
        serif: ["Lora", "serif"],
        sans: ["Inter", "sans-serif"],
      },
      borderRadius: {
        "2xl": "1rem",
      },
    },
  },
  plugins: [],
};
