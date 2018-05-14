export default (vue) => {
  return vue.$resource(
    'admin/contests/{contest_id}/questions{/question_id}',
    {
      contest_id: vue.$route.params.contest_id
    },
    {
      list: {method: 'GET'},
      get: {method: 'GET'},
      update: {method: 'PATCH'}
    }
  )
}
