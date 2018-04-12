export default {
  namespaced: true,
  state: {
    jwt: null
  },
  getters: {
    isAuthenticated (state) {
      return state.jwt !== null && state.jwt !== 'null'
    },
    jwt (state) {
      return state.jwt
    }
  },
  mutations: {
    logIn (state, jwt) {
      state.jwt = jwt
      localStorage.setItem('jwt', jwt)
    },
    logOut (state) {
      state.jwt = null
      localStorage.setItem('jwt', null)
    }
  },
  actions: {
    tryAutoLogin ({state, commit}) {
      const jwt = localStorage.getItem('jwt')
      if (jwt) {
        commit('logIn', jwt)
      }
    }
  }
}
