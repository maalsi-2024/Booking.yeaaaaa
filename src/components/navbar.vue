<template>
    <div class="absolute top-0 z-10 right-0 left-0">
      <nav class="relative px-4 py-4 flex justify-between items-center">
        <a class="text-3xl font-bold leading-none" href="#">
          <svg class="h-10" alt="logo" viewBox="0 0 10240 10240">
            <path
              xmlns="http://www.w3.org/2000/svg"
              d="M8284 9162 c-2 -207 -55 -427 -161 -667 ..."
            />
          </svg>
        </a>
        <button class="lg:hidden navbar-burger flex items-center text-blue-600 p-3" @click="toggleMobileMenu">
          <svg class="block h-4 w-4 fill-current" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
            <title>Mobile menu</title>
            <path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z"></path>
          </svg>
        </button>
        <ul
          :class="['absolute top-1/2 left-1/2 transform -translate-y-1/2 -translate-x-1/2 lg:flex lg:items-center lg:w-auto lg:space-x-6', { hidden: !isMobileMenuOpen }]"
          class="hidden lg:flex lg:mx-auto"
        >
          <li><a class="text-sm text-gray-400 hover:text-gray-500" href="#">Home</a></li>
          <li class="text-gray-300">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" stroke="currentColor" class="w-4 h-4 current-fill" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 5v0m0 7v0m0 7v0m0-13a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2z" />
            </svg>
          </li>
          <li><a class="text-sm text-blue-600 font-bold" href="#">About Us</a></li>
          <li><a class="text-sm text-gray-400 hover:text-gray-500" href="#">Services</a></li>
          <li><a class="text-sm text-gray-400 hover:text-gray-500" href="#">Pricing</a></li>
          <li><a class="text-sm text-gray-400 hover:text-gray-500" href="#">Contact</a></li>
        </ul>
        <div class="hidden lg:flex items-center space-x-3">
          <a class="py-2 px-6 bg-gray-50 hover:bg-gray-100 text-sm text-gray-900 font-bold rounded-xl transition duration-200" href="#">Sign In</a>
          <a class="py-2 px-6 bg-blue-500 hover:bg-blue-600 text-sm text-white font-bold rounded-xl transition duration-200" href="#">Sign Up</a>
        </div>
      </nav>
  
      <!-- Mobile menu -->
      <div v-if="isMobileMenuOpen" class="navbar-menu relative z-50">
        <div class="navbar-backdrop fixed inset-0 bg-gray-800 opacity-25" @click="toggleMobileMenu"></div>
        <nav class="fixed top-0 left-0 bottom-0 flex flex-col w-5/6 max-w-sm py-6 px-6 border-r overflow-y-auto">
          <ul>
            <li><a class="block py-2 px-4 text-sm text-gray-700 hover:bg-gray-100" href="#">Home</a></li>
            <li><a class="block py-2 px-4 text-sm text-gray-700 hover:bg-gray-100" href="#">About Us</a></li>
            <li><a class="block py-2 px-4 text-sm text-gray-700 hover:bg-gray-100" href="#">Services</a></li>
            <li><a class="block py-2 px-4 text-sm text-gray-700 hover:bg-gray-100" href="#">Pricing</a></li>
            <li><a class="block py-2 px-4 text-sm text-gray-700 hover:bg-gray-100" href="#">Contact</a></li>
          </ul>
        </nav>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        isMobileMenuOpen: false,
      };
    },
    methods: {
      toggleMobileMenu() {
        this.isMobileMenuOpen = !this.isMobileMenuOpen;
      },
    },
  };
  </script>
  
  