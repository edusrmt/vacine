import { createWebHistory, createRouter } from 'vue-router';
import Home from '@/views/Home.vue';
import SignUp from '@/views/SignUp.vue';
import SignIn from '@/views/SignIn.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/cadastro',
    name: 'Sign Up',
    component: SignUp
  },
  {
    path: '/entrar',
    name: 'Sign In',
    component: SignIn
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
