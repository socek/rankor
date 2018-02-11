<template>
  <div>
    <b-navbar toggleable="md" type="dark">
      <b-navbar-brand href="#">Cash Flow</b-navbar-brand>
      <b-collapse is-nav id="nav_collapse">

        <b-navbar-nav>
          <b-nav-item href="#/dashboard">Wallets</b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <login></login>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>

    <div class="container-fluid">
      <div class="row">
        <sidebar></sidebar>
        <div class="col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2 main"></div>
        <div id="content">
          <router-view></router-view>
          <b-btn v-b-modal.modal1>Launch demo modal</b-btn>

          <!-- Modal Component -->
          <b-modal id="modal1" title="Bootstrap-Vue">
            <p class="my-4">Hello from modal!</p>
          </b-modal>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
  import './assets/dashboard.css'

  import sidebar from './components/sidebar'
  import login from './components/login'

  export default {
    name: 'app',
    components: {
      sidebar,
      login
    }
  }
</script>
