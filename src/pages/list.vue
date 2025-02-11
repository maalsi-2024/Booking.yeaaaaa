<template>
  <div>
    <h1>Liste des Hôtels</h1>
    <ul v-if="hotels">
      <li v-for="hotel in hotels" :key="hotel.name">
        <h3>{{ hotel.name }}</h3>
        <p>Localisation : {{ hotel.location }}</p>
        <p>Note : {{ hotel.rating }}</p>
        <p>Prix par nuit : {{ hotel.price_per_night }}€</p>
      </li>
    </ul>
    <p v-else>Chargement des hôtels...</p>

    <h1>Liste des Restaurants</h1>
    <ul v-if="restaurants">
      <li v-for="restaurant in restaurants" :key="restaurant.name">
        <h3>{{ restaurant.name }}</h3>
        <p>Localisation : {{ restaurant.location }}</p>
        <p>Cuisine : {{ restaurant.cuisine }}</p>
        <p>Note : {{ restaurant.rating }}</p>
      </li>
    </ul>
    <p v-else>Chargement des restaurants...</p>

    <h1>Liste des Transports</h1>
    <ul v-if="transports">
      <li v-for="transport in transports" :key="transport.company">
        <h3>{{ transport.type }} - {{ transport.company }}</h3>
        <p>Itinéraires : {{ transport.routes?.join(', ') || transport.locations_served.join(', ') }}</p>
        <p>Prix moyen : {{ transport.average_cost_per_km || transport.average_ticket_cost }}€</p>
      </li>
    </ul>
    <p v-else>Chargement des transports...</p>
  </div>
</template>

<script setup>
// import hotels from "~/public/bdd/hotels.json";
// import restaurants from "~/public/bdd/restaurants.json";
// import transports from "~/public/bdd/transports.json";

const { data: restaurants } = await useFetch('/api/restaurants');
/* const { data: hotels } = await useFetch('/api/hotels'); */
const { data: transports } = await useFetch('/api/transports');

const { data: hotels, pending, error } = useAsyncData("hotels", () =>
  $fetch("/api/hotels")
);

console.log("restaurants", restaurants.value)
console.log("hotels", hotels.value)
console.log("transports", transports.value)
</script>

<style>
h1 {
  margin-top: 20px;
  font-size: 24px;
  color: #333;
}
ul {
  list-style: none;
  padding: 0;
}
li {
  margin-bottom: 15px;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
}
</style>
