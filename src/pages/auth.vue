<template>
    <div class="flex items-center justify-center min-h-screen bg-gray-100">
      <div class="bg-white shadow-lg rounded-lg w-full max-w-md p-8">
        <h1 class="text-2xl font-semibold text-center mb-6">
          {{ isLogin ? 'Login' : 'Register' }}
        </h1>
        
        <component :is="isLogin ? 'Login' : 'Register'" @switch="toggleAuthMode" />
  
        <p class="mt-4 text-sm text-center text-gray-600">
          {{ isLogin ? "Don't have an account?" : 'Already have an account?' }}
          <button
            @click="toggleAuthMode"
            class="text-blue-600 hover:underline font-medium"
          >
            {{ isLogin ? 'Register' : 'Login' }}
          </button>
        </p>
      </div>
    </div>
  </template>
  
  <script>
  import Login from '~/components/Login.vue';
  import Register from '~/components/Register.vue';
  
  export default {
    components: {
      Login,
      Register,
    },
    setup() {
      const isLogin = ref(true);
  
      function toggleAuthMode() {
        isLogin.value = !isLogin.value;
      }
  
      return { isLogin, toggleAuthMode };
    },
  };
  </script>
  