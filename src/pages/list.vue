<template>
  <div>
    <h1>Liste des Hôtels</h1>
    <ul>
      <li v-for="hotel in hotels" :key="hotel.name">
        <h3>{{ hotel.name }}</h3>
        <p>Localisation : {{ hotel.location }}</p>
        <p>Note : {{ hotel.rating }}</p>
        <p>Prix par nuit : {{ hotel.price_per_night }}€</p>
      </li>
    </ul>

    <h1>Liste des Restaurants</h1>
    <ul>
      <li v-for="restaurant in restaurants" :key="restaurant.name">
        <h3>{{ restaurant.name }}</h3>
        <p>Localisation : {{ restaurant.location }}</p>
        <p>Cuisine : {{ restaurant.cuisine }}</p>
        <p>Note : {{ restaurant.rating }}</p>
      </li>
    </ul>

    <h1>Liste des Transports</h1>
    <ul>
      <li v-for="transport in transports" :key="transport.company">
        <h3>{{ transport.type }} - {{ transport.company }}</h3>
        <p>Itinéraires : {{ transport.routes?.join(', ') || transport.locations_served.join(', ') }}</p>
        <p>Prix moyen : {{ transport.average_cost_per_km || transport.average_ticket_cost }}€</p>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      hotels: [],
      restaurants: [],
      transports: []
    };
  },
  created() {
    // Charger les données des JSON
    this.loadData();
  },
  methods: {
    async loadData() {
      try {
        const hotelsResponse = await fetch("/path/to/hotels.json");
        this.hotels = await hotelsResponse.json();

        const restaurantsResponse = await fetch("/path/to/restaurants.json");
        this.restaurants = await restaurantsResponse.json();

        const transportsResponse = await fetch("/path/to/transports.json");
        this.transports = await transportsResponse.json();
      } catch (error) {
        console.error("Erreur lors du chargement des données :", error);
      }
    }
  }
};
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
