<template>
  <div>
    <b-btn @click="showModal" variant="primary" size="small">
      Create Wallet
    </b-btn>
    <b-modal id="createWalletModal" ref="createWalletModal" title="Using Component Methods" hide-footer>
      <div class="d-block text-center">
        <h3>Create Wallet</h3>
        <baseForm :form="form" @onSuccess="onSuccess" @onFail="onFail" url="/api/wallets">
          <textInput :form="form" :field="form.fields.name" placeholder="Name"></textInput>
          <input type="submit" name="login" class="btn btn-primary" value="Save">
          <b-btn variant="danger" @click="hideModal">Cancel</b-btn>
        </baseForm>
      </div>
    </b-modal>
  </div>
</template>

<script>
  import baseForm from '@/components/forms/base-form'
  import textInput from '@/components/forms/text-input'

  export default {
    data () {
      return {
        form: baseForm.init(['name'])
      }
    },
    methods: {
      showModal () {
        this.$refs.createWalletModal.show()
      },
      hideModal () {
        this.$refs.createWalletModal.hide()
      },
      onSuccess () {
        baseForm.reset(this.form)
        this.hideModal()
        this.$emit('onSuccess')
      },
      onFail (data) {
        this.form = data.form
      }
    },
    components: {
      textInput,
      baseForm
    }
  }
</script>
