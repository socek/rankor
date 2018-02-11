<template>
  <div>
    <b-nav-item v-if="is_authenticated" v-on:click="logout">Logout</b-nav-item>
  </div>
</template>

<script>
  import AjaxView from '@/models/ajax'
  import User from '@/models/user'

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
      logout: function (event) {
        event.preventDefault()
        User.logOut()
        new AjaxView(this.after).run('/api/auth/logout')
      },
      after: function (event) {
        location.reload()
      }
    }
  }
</script>
