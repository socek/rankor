<template>
  <div>
    <b-btn @click="showModal" variant="primary" size="small">
      Create Wallet
    </b-btn>
    <b-modal id="createWalletModal" ref="createWalletModal" title="Using Component Methods">
      <div class="d-block text-center">
        <h3>Create Wallet</h3>
      </div>
      <b-btn class="mt-3" variant="outline-danger" block @click="hideModal">Close Me</b-btn>
    </b-modal>
  </div>
</template>

<script>
  export default {
    methods: {
      showModal () {
        this.$refs.createWalletModal.show()
      },
      hideModal () {
        this.$refs.createWalletModal.hide()
      }
    }
  }
</script>
