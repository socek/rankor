import Vue from 'vue'
import Vuex from 'vuex'

import auth from '@/auth/store'
import screen from '@/screen/store'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    auth,
    screen
  }
})
