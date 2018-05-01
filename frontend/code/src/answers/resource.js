export default (vue) => {
  return vue.$resource(
    'admin/contests/{contest_uuid}/questions{/question_uuid}/answers',
    {
      contest_uuid: vue.$route.params.contest_uuid,
      question_uuid: vue.$route.params.question_uuid
    },
    {
      list: {method: 'GET'},
      update: {method: 'PATCH'}
    }
  )
}
