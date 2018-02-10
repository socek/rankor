<template>
  <div>
    <div id="navbar" class="navbar-collapse collapse">
      <ul class="nav navbar-nav navbar-right">
        <li v-if="is_authenticated"><a v-on:click="logout" href="#">Logout</a></li>
        <li v-else><a href="#" data-toggle="modal" data-target="#login-modal">Login</a></li>
      </ul>
    </div>
  </div>
</template>

<script>
  import AjaxView from '../models/ajax'
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
    }
  }
</script>
