<template>
  <div>
    <b-nav-item v-if="isAuthenticated" v-on:click="logout">Logout</b-nav-item>
  </div>
</template>

<script>
  export default {
    computed: {
      isAuthenticated () {
        return this.$store.getters['auth/isAuthenticated']
      }
    },
    methods: {
      logout (event) {
        this.$store.commit('auth/logOut')
        this.$router.push({name: 'NotLoggedIn'})
        event.preventDefault()
      }
    }
  }
</script>
