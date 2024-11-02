import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  // To deploy to GitHub Pages, chk https://www.linkedin.com/pulse/deploying-react-vite-application-mangesh-ahire-p6auf/
  // base: '/fitness_guru/',
  
  plugins: [react()],
  server: {
    proxy: {
      '/api': process.env.VITE_API_URL || "https://fitness-guru-igqa.onrender.com",  // Flask backend
    },
  },
});