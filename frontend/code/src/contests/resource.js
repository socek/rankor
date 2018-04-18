export default (vue) => {
  return {
    contests: vue.$resource('admin/contests'),
    contest: vue.$resource('admin/contests{/contest_uuid}')
  }
}
