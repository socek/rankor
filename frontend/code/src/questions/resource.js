export default (vue) => {
  return vue.$resource(
    'admin/contests{/contest_uuid}/questions',
    {
      contest_uuid: vue.$route.params.contest_uuid
    },
    {
      list: {method: 'GET'},
      get: {method: 'GET'},
      update: {method: 'PATCH'}
    }
  )
}
