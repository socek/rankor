export default (vue) => {
  return vue.$resource('host{/game_uuid}', {}, {
    list_questions: {method: 'GET', url: 'host{/game_uuid}/questions'},
    get_question: {method: 'GET', url: 'host{/game_uuid}/questions{/question_uuid}'},
    list_answers: {method: 'GET', url: 'host{/game_uuid}/questions{/question_uuid}/answers'},
    save_answer: {method: 'POST', url: 'host{/game_uuid}/questions{/question_uuid}/answers'},
    change_view: {method: 'POST', url: 'game{/game_uuid}'}
  })
}
