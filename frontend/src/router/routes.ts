import HomeView from '@/views/HomeView.vue'
import VisualizeView from '@/views/VisualizeView.vue'
import RecordView from '@/views/RecordView.vue'

import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  { path: '/', component: HomeView },
  { path: '/processes/visualize', component: VisualizeView },
  { path: '/processes/record', component: RecordView }
]

/* For router: see https://router.vuejs.org/guide/ */
/* For meta.env: see https://vitejs.dev/guide/env-and-mode#env-variables */
export const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: routes
})
