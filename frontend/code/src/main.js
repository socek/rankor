// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router/index'
import BootstrapVue from 'bootstrap-vue'
import VueResource from 'vue-resource'

Vue.config.productionTip = true
Vue.use(BootstrapVue)
Vue.use(VueResource)

Vue.http.options.root = '/api'

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
