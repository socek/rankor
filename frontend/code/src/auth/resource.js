export default (vue) => {
  return {
    auth: vue.$resource('auth'),
    login: vue.$resource('auth/login'),
    logout: vue.$resource('auth/logout')
  }
}
