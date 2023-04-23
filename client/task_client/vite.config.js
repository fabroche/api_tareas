import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import cors from 'cors'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    middleware: {
      // enable cors
      async handle(req, res, next) {
        res.setHeader("Access-Control-Allow-Origin", "*");
        res.setHeader("Access-Control-Allow-Methods", "*");
        res.setHeader("Access-Control-Allow-Headers", "*");
        await cors()(req, res, next);
      },
    },
  },
});
