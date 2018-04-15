<template>
  <div>
    <b-btn @click="showModal" variant="primary" size="small">
      Create
    </b-btn>

    <b-modal id="createQuestionModal" ref="createQuestionModal" title="Create Question" hide-footer>
      <form @submit.prevent="onSave">
        <b-form-invalid-feedback  v-for="error in errors._schema"
                                  :key="error"
                                  :force-show="true" >
          {{ errors._schema }}
        </b-form-invalid-feedback>

        <b-form-group id="nameFieldGroup"
                            label="Name:"
                            label-for="nameField">
          <b-form-input id="nameField"
                        v-model.trim="fields.name"
                        type="text"
                        :state="errors.name.length == 0 ? null : false"
                        placeholder="Question name"></b-form-input>
          <b-form-invalid-feedback  v-for="error in errors.name"
                                    class="modal-invalid-feedback"
                                    :key="error">
            {{ error }}
          </b-form-invalid-feedback>
        </b-form-group>

        <b-form-group id="descriptionFieldGroup"
                            label="Description:"
                            label-for="descriptionField">
          <b-form-input id="descriptionField"
                        v-model.trim="fields.description"
                        type="text"
                        :state="errors.description.length == 0 ? null : false"
                        placeholder="Question description"></b-form-input>
          <b-form-invalid-feedback  v-for="error in errors.description"
                                    class="modal-invalid-feedback"
                                    :key="error">
            {{ error }}
          </b-form-invalid-feedback>
        </b-form-group>

        <b-form-group id="indexFieldGroup"
                            label="Index:"
                            label-for="indexField">
          <b-form-input id="indexField"
                        v-model="fields.index"
                        type="text"
                        :state="errors.index.length == 0 ? null : false"
                        placeholder="Question index"></b-form-input>
          <b-form-invalid-feedback  v-for="error in errors.index"
                                    class="modal-invalid-feedback"
                                    :key="error">
            {{ error }}
          </b-form-invalid-feedback>
        </b-form-group>

        <b-form-group id="categoryFieldGroup"
                            label="Category:"
                            label-for="categoryField">
          <b-form-input id="categoryField"
                        v-model.trim="fields.category"
                        type="text"
                        :state="errors.category.length == 0 ? null : false"
                        placeholder="Question category"></b-form-input>
          <b-form-invalid-feedback  v-for="error in errors.category"
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
  import questionResource from '@/questions/resource'

  export default {
    data () {
      return {
        ...{
          fields: {
            name: '',
            description: '',
            index: '1',
            category: ''
          },
          errors: {
            _schema: [],
            name: [],
            description: [],
            index: [],
            category: []
          }
        },
        resource: questionResource(this)
      }
    },
    methods: {
      refresh () {
        for (let name in this.fields) {
          this.fields[name] = ''
          this.errors[name] = ''
        }
        this.errors._schema = ''
      },
      showModal () {
        this.refresh()
        this.$refs.createQuestionModal.show()
      },
      hideModal () {
        this.$refs.createQuestionModal.hide()
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
