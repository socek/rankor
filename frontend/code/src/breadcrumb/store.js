const Contests = (commit, rootGetters, vue) => {
  commit('clear')
  commit(
    'addCrumb',
    {
      text: 'Contests',
      to: {
        name: 'Contests'
      }
    }
  )
}

const Questions = (commit, rootGetters, vue) => {
  Contests(commit, rootGetters, vue)

  commit(
    'addCrumb',
    {
      textMethod: () => rootGetters['contest/name'],
      to: {
        name: 'Questions',
        params: {
          contest_id: vue.$route.params.contest_id
        }
      }
    }
  )
}

const Answers = (commit, rootGetters, vue) => {
  Questions(commit, rootGetters, vue)

  commit(
    'addCrumb',
    {
      text: 'Answers',
      to: {
        name: 'Answers',
        params: {
          contest_id: vue.$route.params.contest_id,
          question_id: vue.$route.params.question_id
        }
      }
    }
  )
}

const Games = (commit, rootGetters, vue) => {
  commit('clear')
  commit(
    'addCrumb',
    {
      text: 'Games',
      to: {
        name: 'Games',
        params: {
          contest_id: vue.$route.params.contest_id,
          question_id: vue.$route.params.question_id
        }
      }
    }
  )
}

const HostView = (commit, rootGetters, vue) => {
  Games(commit, rootGetters, vue)

  commit(
    'addCrumb',
    {
      text: 'Host View',
      to: {
        name: 'HostView',
        params: {
          game_id: vue.$route.params.game_id
        }
      }
    }
  )
}

const HostQuestionView = (commit, rootGetters, vue) => {
  HostView(commit, rootGetters, vue)

  commit(
    'addCrumb',
    {
      text: 'Question',
      to: {
        name: 'HostQuestionView',
        params: {
          game_id: vue.$route.params.game_id,
          screen_id: vue.$route.params.screen_id
        }
      }
    }
  )
}

export default {
  namespaced: true,
  state: {
    crumbs: []
  },
  getters: {
  },
  mutations: {
    clear: (state) => {
      state.crumbs = []
    },
    addCrumb: (state, payload) => {
      state.crumbs.push(payload)
    }
  },
  actions: {
    Contests: ({commit, rootGetters}, vue) => Contests(commit, rootGetters, vue),
    Questions: ({commit, rootGetters}, vue) => Questions(commit, rootGetters, vue),
    Answers: ({commit, rootGetters}, vue) => Answers(commit, rootGetters, vue),
    Games: ({commit, rootGetters}, vue) => Games(commit, rootGetters, vue),
    HostView: ({commit, rootGetters}, vue) => HostView(commit, rootGetters, vue),
    HostQuestionView: ({commit, rootGetters}, vue) => HostQuestionView(commit, rootGetters, vue)
  }
}
