import resource from '@/contests/resource'

export default {
  namespaced: true,
  state: {
    id: null,
    name: null,
    vue: null
  },
  getters: {
    resource (state, getters, rootState, rootGetters) {
      return resource(rootGetters.vue)
    },
    name (state) {
      return state.name
    }
  },
  mutations: {
    clear: (state) => {
      state.id = null
      state.name = null
    },
    fill: (state, contest) => {
      state.id = contest.id
      state.name = contest.name
    }
  },
  actions: {
    fetchContest: ({commit, getters, state, rootGetters}) => {
      let params = {
        contest_id: rootGetters.$route.params.contest_id
      }
      getters.resource.get(params).then((response) => {
        commit('fill', response.body)
      })
    }
  }
}
