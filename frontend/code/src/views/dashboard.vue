<template>
  <div class="row justify-content-md-center">
    <div class="col-lg-12">
      <h1>List of wallets <walletCreateDialog @onSuccess="refresh"></walletCreateDialog></h1>
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
  </div>
</template>

<script>
  import AjaxView from '../models/ajax'
  import walletCreateDialog from '@/dialogs/wallets/create'

  export default {
    data () {
      return {
        wallets: [],
        showModal: false
      }
    },
    created: function () {
      this.refresh()
    },
    methods: {
      refresh () {
        var self = this
        new AjaxView(function (response) {
          self.wallets = response.data.elements
        }).run('/api/wallets').then(self.fillWidget)
      }
    },
    components: {
      walletCreateDialog
    }
  }
</script>

