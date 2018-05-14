export default (vue) => {
  return vue.$resource(
    'admin/contests/{contest_id}/questions{/question_id}/answers{/answer_id}',
    {
      contest_id: vue.$route.params.contest_id,
      question_id: vue.$route.params.question_id
    },
    {
      list: {method: 'GET'},
      get: {method: 'GET'},
      update: {method: 'PATCH'}
    }
  )
}
