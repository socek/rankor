export default (vue) => {
  return vue.$resource('admin/contests{/contest_uuid}', {}, {
    list: {method: 'GET'},
    get: {method: 'GET'},
    update: {method: 'PATCH'}
  })
}
