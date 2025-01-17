<template>
    <div class="p-6 max-w-4xl mx-auto">
      <h1 class="text-2xl font-bold mb-6 text-center">Système de Réservation</h1>
      
      <!-- Formulaire de réservation -->
      <div class="mb-8">
        <h2 class="text-xl font-semibold mb-4">Faire une réservation</h2>
        <form @submit.prevent="addReservation" class="space-y-4">
          <div>
            <label class="block text-sm font-medium text-gray-700">Nom</label>
            <input
              type="text"
              v-model="newReservation.name"
              class="mt-1 w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
              placeholder="Entrez votre nom"
              required
            />
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700">Date</label>
            <input
              type="date"
              v-model="newReservation.date"
              class="mt-1 w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
              required
            />
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700">Heure</label>
            <input
              type="time"
              v-model="newReservation.time"
              class="mt-1 w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
              required
            />
          </div>
          <button
            type="submit"
            class="w-full py-2 px-4 bg-blue-600 text-white rounded-md hover:bg-blue-700 focus:outline-none"
          >
            Réserver
          </button>
        </form>
      </div>
  
      <!-- Liste des réservations -->
      <div>
        <h2 class="text-xl font-semibold mb-4">Vos réservations</h2>
        <div v-if="reservations.length > 0" class="space-y-4">
          <div
            v-for="(reservation, index) in reservations"
            :key="index"
            class="p-4 border border-gray-200 rounded-md shadow-sm flex justify-between items-center"
          >
            <div>
              <p class="font-medium text-gray-800">{{ reservation.name }}</p>
              <p class="text-sm text-gray-600">{{ reservation.date }} à {{ reservation.time }}</p>
            </div>
            <div class="flex space-x-2">
              <button
                @click="editReservation(index)"
                class="px-3 py-1 bg-yellow-500 text-white rounded-md hover:bg-yellow-600 focus:outline-none"
              >
                Modifier
              </button>
              <button
                @click="deleteReservation(index)"
                class="px-3 py-1 bg-red-600 text-white rounded-md hover:bg-red-700 focus:outline-none"
              >
                Supprimer
              </button>
            </div>
          </div>
        </div>
        <p v-else class="text-gray-600">Aucune réservation pour le moment.</p>
      </div>
    </div>
  </template>
  
<script>
  export default {
    data() {
      return {
        newReservation: {
          name: "",
          date: "",
          time: "",
        },
        reservations: [],
      };
    },
    methods: {
      addReservation() {
        this.reservations.push({ ...this.newReservation });
        this.newReservation = { name: "", date: "", time: "" };
      },
      deleteReservation(index) {
        this.reservations.splice(index, 1);
      },
      editReservation(index) {
        const reservation = this.reservations[index];
        this.newReservation = { ...reservation };
        this.reservations.splice(index, 1);
      },
    },
  };
</script>