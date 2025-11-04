import { createRouter, createWebHistory } from '@ionic/vue-router';
import HomeView from '@/views/HomePage.vue';
// import PartyList from '@/views/PartyList.vue'; // create later
// import ProductList from '@/views/ProductList.vue'; // create later
// import InventoryList from '@/views/InventoryList.vue'; // create later

const routes = [
  { path: '/', component: HomeView },
  // { path: '/parties', component: PartyList },
  // { path: '/products', component: ProductList },
  // { path: '/inventory', component: InventoryList },
  // add billing route later
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;
