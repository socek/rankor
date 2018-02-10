class UserInterface {

  constructor () {
    this.key = 'user'
  }

  logIn () {
    this.setUserData({
      groups: ['authenticated']
    })
  }

  logOut () {
    localStorage.removeItem(this.key)
  }

  isAuthenticated () {
    return this.getUserData().groups.includes('authenticated')
  }

  setUserData (data) {
    localStorage.setItem(this.key, JSON.stringify(data))
  }

  getUserData () {
    if (localStorage[this.key]) {
      return JSON.parse(localStorage.getItem(this.key))
    } else {
      return {
        groups: []
      }
    }
  }

}

export default new UserInterface()
