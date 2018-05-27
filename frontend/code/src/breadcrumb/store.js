const Contests = (commit, vue) => {
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

const Questions = (commit, vue) => {
  Contests(commit, vue)

  commit(
    'addCrumb',
    {
      text: 'Questions',
      to: {
        name: 'Questions',
        params: {
          contest_id: vue.$route.params.contest_id
        }
      }
    }
  )
}

const Answers = (commit, vue) => {
  Questions(commit, vue)

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

const Games = (commit, vue) => {
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

const HostView = (commit, vue) => {
  Games(commit, vue)

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

const HostQuestionView = (commit, vue) => {
  HostView(commit, vue)

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
    Contests: ({commit}, vue) => Contests(commit, vue),
    Questions: ({commit}, vue) => Questions(commit, vue),
    Answers: ({commit}, vue) => Answers(commit, vue),
    Games: ({commit}, vue) => Games(commit, vue),
    HostView: ({commit}, vue) => HostView(commit, vue),
    HostQuestionView: ({commit}, vue) => HostQuestionView(commit, vue)
  }
}
