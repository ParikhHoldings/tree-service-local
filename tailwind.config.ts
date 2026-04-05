import type { Config } from 'tailwindcss'

const config: Config = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        'pool-blue': '#0EA5E9',
        'pool-dark': '#0C4A6E',
        'pool-teal': '#0D9488',
      },
    },
  },
  plugins: [],
}
export default config
