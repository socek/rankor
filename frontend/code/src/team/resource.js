export default (vue) => {
  return vue.$resource('host/{game_uuid}/teams', {}, {
    list: {method: 'GET'},
    get: {method: 'GET'},
    update: {method: 'PATCH'}
  })
}
