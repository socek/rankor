<template>
  <div>
    <h1>List of wallets</h1>
    <table class="table table-striped">
      <thead class="thead-dark">
        <tr>
          <th scope="col">#</th>
          <th scope="col">Name</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(wallet, index) in wallets">
          <td scope="row">{{index + 1}}</td>
          <td>{{wallet.name}}</td>
        </tr>
      </tbody>
    </table>

  </div>
</template>

<script>
  import AjaxView from '../models/ajax'

  export default {
    data () {
      return {
        wallets: []
      }
    },
    created: function () {
      var self = this
      new AjaxView(function (response) {
        self.wallets = response.data.elements
      }).run('/api/wallets').then(self.fillWidget)
    }
  }
</script>
