export default (vue) => {
  return vue.$resource('admin/contests{/contest_id}', {}, {
    list: {method: 'GET'},
    get: {method: 'GET'},
    update: {method: 'PATCH'},
    delete: {method: 'DELETE'}
  })
}
