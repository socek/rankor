export default (vue) => {
  return vue.$resource('host{/game_uuid}', {}, {
    list_questions: {method: 'GET', url: 'host{/game_uuid}/questions'},
    get_question: {method: 'GET', url: 'host{/game_uuid}/questions{/question_uuid}'},
    save_answer: {method: 'POST', url: 'host{/game_uuid}/questions{/question_uuid}'},
    change_view: {method: 'POST', url: 'game{/game_uuid}'},
    get_highscore: {method: 'GET', url: 'game{/game_uuid}/highscore'}
  })
}
