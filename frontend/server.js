import { fileURLToPath } from 'node:url';
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

const __filename = fileURLToPath(import.meta.url);
const __dirname = new URL('.', import.meta.url).pathname;

export default defineConfig({
  root: 'src',
  base: './',
  plugins: [react()],
  server: {
    host: '0.0.0.0',
    port: process.env.FRONTEND_PORT ? Number(process.env.FRONTEND_PORT) : 3000,
    open: false,
    strictPort: true,
    allowedHosts: ['host.docker.internal', '0.0.0.0'],
  },
  build: {
    outDir: '../dist',
  },
});
