<template>
  <div>
    <b-nav-item v-if="isAuthenticated" v-on:click="logout">Logout</b-nav-item>
  </div>
</template>

<script>
  export default {
    computed: {
      isAuthenticated () {
        return this.$store.getters.isAuthenticated
      }
    },
    methods: {
      logout (event) {
        this.$store.commit('logOut')
        this.$router.push({name: 'NotLoggedIn'})
        event.preventDefault()
      }
    }
  }
</script>
