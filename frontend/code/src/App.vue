<template>
  <div>
    <b-navbar toggleable="md" type="dark">
      <b-navbar-brand href="#">Cash Flow</b-navbar-brand>
      <b-collapse is-nav id="nav_collapse">

        <b-navbar-nav>
          <b-nav-item v-if="isAuthenticated" href="#/dashboard">Wallets</b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <login></login>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>

    <div class="container" id="content_container">
      <div class="row">
        <div class="col-lg-12 align-self-center" id="content">
          <router-view></router-view>
        </div>
      </div>
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
