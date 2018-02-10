<template>
  <div>
    <nav class="navbar navbar-inverse navbar-fixed-top">
      <div class="container-fluid">
        <div class="navbar-header">
          <a class="navbar-brand" href="#">Cash Flow</a>
        </div>
        <login></login>
      </div>
    </nav>

    <div class="container-fluid">
      <div class="row">
        <sidebar></sidebar>
        <div class="col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2 main"></div>
        <div id="content">
          <router-view></router-view>
        </div>
      </div>
    </div>

    <loginDialog></loginDialog>
  </div>
</template>

<style>
  #content {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
</style>

<script>
  import './assets/dashboard.css'

  import sidebar from './components/sidebar'
  import login from './components/login'
  import loginDialog from './components/login_dialog'

  export default {
    name: 'app',
    components: {
      sidebar,
      login,
      loginDialog
    }
  }
</script>
