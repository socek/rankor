export default (vue) => {
  return vue.$resource('admin/games{/game_id}', {}, {
    list: {method: 'GET'},
    get: {method: 'GET'},
    update: {method: 'PATCH'}
  })
}
