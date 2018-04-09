class UserInterface {

  constructor () {
    this.key = 'user'
  }

  logIn (jwt) {
    this.setUserData({
      jwt: jwt,
      groups: ['authenticated']
    })
  }

  logOut () {
    localStorage.removeItem(this.key)
  }

  isAuthenticated () {
    return this.getUserData().jwt
  }

  setUserData (data) {
    localStorage.setItem(this.key, JSON.stringify(data))
  }

  getUserData () {
    if (localStorage[this.key]) {
      return JSON.parse(localStorage.getItem(this.key))
    } else {
      return {
        jwt: null,
        groups: []
      }
    }
  }

}

export default new UserInterface()
