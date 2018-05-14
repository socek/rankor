export default (vue) => {
  return vue.$resource('host{/game_id}', {}, {
    list_questions: {method: 'GET', url: 'host{/game_id}/questions'},
    get_question: {method: 'GET', url: 'host{/game_id}/questions{/question_id}'},
    save_answer: {method: 'POST', url: 'host{/game_id}/questions{/question_id}'},
    change_view: {method: 'POST', url: 'game{/game_id}'},
    get_highscore: {method: 'GET', url: 'game{/game_id}/highscore'}
  })
}
