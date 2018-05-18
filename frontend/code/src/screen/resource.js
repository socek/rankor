export default (vue) => {
  return vue.$resource('host{/game_id}/screens{/screen_id}', {}, {
    listScreens: {method: 'GET'},
    createScreen: {method: 'POST'},
    deleteScreen: {method: 'DELETE'}
  })
}
