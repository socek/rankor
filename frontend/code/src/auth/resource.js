export default (vue) => {
  return vue.$resource('auth', {}, {
    login: {method: 'POST', url: 'auth/login'},
    signUp: {method: 'POST', url: 'auth/signup'}
  })
}
