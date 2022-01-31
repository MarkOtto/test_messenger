import Vue from 'vue'
import VueRouter from 'vue-router'
// import Home from '../views/Home.vue'
import middleware from '../middleware'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    meta: {layout: 'empty'},
    redirect: "/login",
    component: () => import("../App"),
    children: [
      {
        path: '/login',
        meta: {layout: 'empty'},
        component: () => import(/* webpackChunkName: "login" */ '../views/Login.vue')
      }
    ],

  },
  {
    path: '/inbox',
    name: 'Inbox',
    beforeEnter: middleware,
    meta: {layout: 'main'},
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/Messages.vue')
  }
]

const router = new VueRouter({
  mode: "history",
  routes
})

export default router
