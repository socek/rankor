export default (vue) => {
  return vue.$resource('admin/contests/:contest_uuid/questions')
}
