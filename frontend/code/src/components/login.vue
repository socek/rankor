<template>
  <div>
    <b-nav-item v-if="is_authenticated" v-on:click="logout">Logout</b-nav-item>
    <loginDialog :is_authenticated="is_authenticated"></loginDialog>
  </div>
</template>

<script>
  import AjaxView from '@/models/ajax'
  import User from '@/models/user'
  import loginDialog from '@/components/login_dialog'

  export default {
    data () {
      return {
        is_authenticated: false
      }
    },
    created: function () {
      var self = this
      new AjaxView(function (response) {
        self.is_authenticated = response.data.is_authenticated
        User.setUserData(response.data)
      }).run('/api/auth').then(self.fillWidget)
    },
    methods: {
      login: function (event) {
        event.preventDefault()
        new AjaxView(this.after).run('/api/auth/login')
      },
      logout: function (event) {
        event.preventDefault()
        User.logOut()
        new AjaxView(this.after).run('/api/auth/logout')
      },
      after: function (event) {
        location.reload()
      }
    },
    components: {
      loginDialog
    }
  }
</script>
