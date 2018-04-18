<template>
  <b-button size="sm" variant="link" @click="showModal">
    <icon name="edit"></icon>

    <b-modal id="editContestModal" ref="editContestModal" title="Edit Contest" hide-footer>
      <form @submit.prevent="onSave" v-show="!is_loading">
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
      <div v-show="is_loading" class="modal-spiner">
        <icon name="sync" scale="2" spin></icon>
      </div>
    </b-modal>
  </b-button>
</template>

<script>
  import contestResource from '@/contests/resource'
  import baseForm from '@/forms'

  export default {
    props: ['contest_uuid'],
    extends: baseForm,
    data () {
      return {
        is_loading: true,
        form: this.prepareForm({
          name: ''
        }),
        resource: contestResource(this)
      }
    },
    methods: {
      showModal (modal) {
        this.moveModalToTopOfTheDOM()
        this.is_loading = true
        this.getFormModal().show()
        this.resource.get({contest_uuid: this.contest_uuid}).then((response) => {
          this.form.defaults = response.body
          this.is_loading = false
          this.refreshForm(true)
        })
      },
      getFormModal () {
        return this.$refs.editContestModal
      },
      onSave () {
        this.resource.update({contest_uuid: this.contest_uuid}, this.form.fields).then((response) => {
          this.hideModal()
          this.$emit('onSuccess')
        }).catch(this.onError)
      }
    }
  }
</script>

<style>
  .modal-spiner {
    text-align: center;
  }
</style>
