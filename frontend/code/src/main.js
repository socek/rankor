// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue'
import VueResource from 'vue-resource'

import App from '@/App'
import router from '@/routing'
import store from '@/store'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.config.productionTip = true
Vue.use(BootstrapVue)
Vue.use(VueResource)

Vue.http.options.root = '/api'

Vue.http.interceptors.push((request, next) => {
  if (store.state.jwt) {
    request.headers.set('JWT', store.state.jwt)
  }
  next()
})

store.dispatch('tryAutoLogin')

/* eslint-disable no-new */
export default new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: { App }
})
