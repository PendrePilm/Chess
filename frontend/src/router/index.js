import { createRouter, createWebHistory } from "vue-router";
import Login from "../components/LoginChess.vue";
import Signup from "../components/SignupChess.vue";
import Menu from "../components/MenuChess.vue";
import Parametres from "../components/ParametresChess.vue";

const routes = [
  { path: "/login", component: Login },
  { path: "/signup", component: Signup },
  { path: "/menu", component: Menu },
  { path: "/parametres", component: Parametres }, 
  
  { path: "/", redirect: "/login" }, // Redirige vers la page de connexion par défaut
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
