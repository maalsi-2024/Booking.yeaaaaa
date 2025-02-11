// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true },
  srcDir: 'src/',
  modules: ['@nuxtjs/tailwindcss'],
  runtimeConfig: {
    MONGO_URI: process.env.MONGO_URI,
    DB_NAME: process.env.DB_NAME,
  }
})
