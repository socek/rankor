<template>
  <div>
    <b-navbar toggleable="md" type="dark" v-if="isNavbar">
      <b-navbar-brand href="#">Rankor Admin Panel</b-navbar-brand>
      <b-collapse is-nav id="nav_collapse">

        <b-navbar-nav>
          <b-nav-item v-if="isAuthenticated" :to="{name: 'Contests'}">Contests</b-nav-item>
          <b-nav-item v-if="isAuthenticated" :to="{name: 'Games'}">Games</b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <login></login>
          <register v-if="!isAuthenticated"></register>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>

    <div class="container" id="content_container">
      <router-view></router-view>
    </div>

  </div>
</template>

<script>
  import '@/contests/admin_list.css'

  import login from '@/auth/login'
  import register from '@/auth/register.vue'

  export default {
    computed: {
      isAuthenticated () {
        return this.$store.getters['auth/isAuthenticated']
      },
      isNavbar () {
        return this.$route.name !== 'GameScreen'
      }
    },
    name: 'app',
    components: {
      login,
      register
    }
  }
</script>
