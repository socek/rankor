export default {
  namespaced: true,
  state: {
    view: 'connecting',
    question: null,
    team: null,
    answer: null,
    isCorrect: null
  },
  getters: {
  },
  mutations: {
    setView: (state, payload) => {
      state.view = payload
    },
    setQuestion: (state, payload) => {
      state.question = payload
    },
    setTeam: (state, payload) => {
      state.team = payload
    },
    setAnswer: (state, payload) => {
      state.answer = payload
    },
    setIsCorrect: (state, payload) => {
      state.isCorrect = payload
    }
  },
  actions: {
    parseData: ({commit}, payload) => {
      let methods = {
        change_view: (payload) => {
          commit('setView', payload.view)
        },
        init: (payload) => {
          commit('setView', payload.view)
          commit('setQuestion', payload.question)
          commit('setTeam', payload.team)
          commit('setAnswer', payload.answer)
          commit('setIsCorrect', payload.is_correct)
        },
        ping: (payload) => {},
        show_question: (payload) => {
          commit('setView', payload.view)
          commit('setQuestion', payload.question)
          commit('setTeam', payload.team)
          commit('setAnswer', payload.answer)
          commit('setIsCorrect', payload.is_correct)
        },
        attach_team: (payload) => {
          commit('setTeam', payload.team)
        },
        select_answer: (payload) => {
          commit('setAnswer', payload.answer)
        },
        veryfi_answer: (payload) => {
          commit('setIsCorrect', payload.is_correct)
        }
      }
      methods[payload['name']](payload)
    }
  }
}
