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
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>

    <div class="container" id="content_container">
      <router-view></router-view>
    </div>

  </div>
</template>

<script>
  import './assets/dashboard.css'

  import login from './components/login'
  import User from '@/models/user'

  export default {
    data () {
      return {
        isAuthenticated: User.isAuthenticated()
      }
    },
    name: 'app',
    components: {
      login
    }
  }
</script>

<style>
  .invalid-feedback {
    font-size: 30%;
    text-align: left;
    padding-left: 15px;
  }
</style>
