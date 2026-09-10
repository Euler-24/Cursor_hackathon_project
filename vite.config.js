import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  // Chemins relatifs : obligatoire pour GitHub Pages (sous-dossier /Cursor_hackathon_project/).
  base: "./",
  build: {
    outDir: "docs",
    emptyOutDir: true,
  },
  server: {
    port: 5173,
  },
});
