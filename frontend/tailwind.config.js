/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        themePrimary: 'var(--color-primary, #3b82f6)',
        themeSecondary: 'var(--color-secondary, #8b5cf6)',
        themeBg: 'var(--bg-main, #f8fafc)',
        themeCard: 'var(--bg-card, #ffffff)',
        themeText: 'var(--text-main, #0f172a)',
        themeMuted: 'var(--text-muted, #64748b)'
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        rounded: ['Quicksand', 'Nunito', 'sans-serif'],
        dyslexic: ['OpenDyslexic', 'Comic Sans MS', 'sans-serif']
      }
    },
  },
  plugins: [],
}
