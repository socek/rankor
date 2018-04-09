<template>
  <div>
    <b-nav-item v-if="is_authenticated" v-on:click="logout">Logout</b-nav-item>
  </div>
</template>

<script>
  import User from '@/models/user'

  export default {
    data () {
      return {
        is_authenticated: false
      }
    },
    created: function () {
      this.is_authenticated = User.isAuthenticated()
    },
    methods: {
      logout: function (event) {
        event.preventDefault()
        User.logOut()
        location.reload()
      }
    }
  }
</script>
