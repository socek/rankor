export default (vue) => {
  return vue.$resource('host{/game_uuid}', {}, {
    list_questions: {method: 'GET', url: 'host{/game_uuid}/questions'}
  })
}
