import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import { BootstrapVue, IconsPlugin, BadgePlugin, BootstrapVueIcons, BIcon   } from 'bootstrap-vue'
import VueGoodTablePlugin from 'vue-good-table';

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
// import 'bootstrap-vue/src/icons.scss'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import './assets/main.scss'
import 'vue-good-table/dist/vue-good-table.css'



Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(VueGoodTablePlugin);
Vue.use(BadgePlugin)
Vue.use(BootstrapVueIcons)
Vue.component('BIcon', BIcon)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
