<template>
  <div>
    <b-btn @click="showModal" variant="primary" size="small">
      Create
    </b-btn>

    <b-modal id="createContestModal" ref="createContestModal" title="Create Contest" hide-footer>
      <form @submit.prevent="onSave">
        <b-form-invalid-feedback  v-for="error in form.errors._schema"
                                  :key="error"
                                  :force-show="true" >
          {{ error }}
        </b-form-invalid-feedback>

        <b-form-group id="nameFieldGroup"
                            label="Name:"
                            label-for="nameField">
          <b-form-input id="nameField"
                        v-model.trim="form.fields.name"
                        type="text"
                        :state="form.errors.name.length == 0 ? null : false"
                        placeholder="Contest name"></b-form-input>
          <b-form-invalid-feedback  v-for="error in form.errors.name"
                                    class="modal-invalid-feedback"
                                    :key="error">
            {{ error }}
          </b-form-invalid-feedback>
        </b-form-group>

        <input type="submit" value="Save" class="btn btn-primary">
        <b-btn variant="danger" @click="hideModal">Cancel</b-btn>
      </form>
    </b-modal>
  </div>
</template>

<script>
  import contestResource from '@/contests/resource'
  import baseForm from '@/forms'

  export default {
    extends: baseForm,
    data () {
      return {
        form: this.prepareForm({
          name: ''
        }),
        resource: contestResource(this)
      }
    },
    methods: {
      showModal () {
        this._showModal(this.$refs.createContestModal)
      },
      hideModal () {
        this._hideModal(this.$refs.createContestModal)
      }
    }
  }
</script>
