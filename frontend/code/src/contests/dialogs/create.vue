<template>
  <div>
    <b-btn @click="showModal" variant="primary" size="small">
      Create Contest
    </b-btn>

    <b-modal id="createContestModal" ref="createContestModal" title="Create Contest" hide-footer>
      <form @submit.prevent="onSave">
        <b-form-invalid-feedback  v-for="error in errors._form"
                                  :key="error"
                                  :force-show="true" >
          {{ errors._form }}
        </b-form-invalid-feedback>

        <b-form-group id="nameFieldGroup"
                            label="Name:"
                            label-for="nameField">
          <b-form-input id="nameField"
                        v-model.trim="fields.name"
                        type="text"
                        :state="errors.name.length == 0 ? null : false"
                        placeholder="Contest name"></b-form-input>
          <b-form-invalid-feedback  v-for="error in errors.name"
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

  export default {
    data () {
      return {
        ...{
          fields: {
            name: ''
          },
          errors: {
            _form: [],
            name: []
          }
        },
        resource: contestResource(this)
      }
    },
    methods: {
      refresh () {
        for (let name in this.fields) {
          this.fields[name] = ''
          this.errors[name] = ''
        }
        this.errors._form = ''
      },
      showModal () {
        this.refresh()
        this.$refs.createContestModal.show()
      },
      hideModal () {
        this.$refs.createContestModal.hide()
      },
      onSave () {
        this.resource.save({}, this.fields).then((response) => {
          this.hideModal()
          this.$emit('onSuccess')
        }).catch((response) => {
          this.errors = response.body
        })
      }
    }
  }
</script>
