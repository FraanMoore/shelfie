/** @type {import('tailwindcss').Config} */
export default {
  content: [".index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        shelfie: {
          dark: "#02333b",
          darkest: "#012a33",
          medium: "#174D4D",
          mediumDark: "#38838a",
          mediumLight: "#69aeb3",
          mediumLightest: "#a7d6d9",
          white: "#FFFFFF",
          light: "#F8F9F9",
        },
      },
    },
  },
  plugins: [],
};
