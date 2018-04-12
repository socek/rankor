<template>
  <div>
    <b-navbar toggleable="md" type="dark">
      <b-navbar-brand href="#">Rankor Admin Panel</b-navbar-brand>
      <b-collapse is-nav id="nav_collapse">

        <b-navbar-nav>
          <b-nav-item v-if="isAuthenticated" :to="{name: 'Dashboard'}">Dashboard</b-nav-item>
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
  import '@/contests/dashboard.css'

  import login from '@/auth/login'
  import register from '@/auth/register.vue'

  export default {
    computed: {
      isAuthenticated () {
        return this.$store.getters['auth/isAuthenticated']
      }
    },
    name: 'app',
    components: {
      login,
      register
    }
  }
</script>

<style>
  .modal-invalid-feedback {
    font-size: 30%;
  }
</style>
