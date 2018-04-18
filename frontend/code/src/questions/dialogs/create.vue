<template>
    <b-btn @click="showModal" variant="primary" size="small">
      <icon name="plus"></icon>

      <b-modal id="createQuestionModal" ref="createQuestionModal" title="Create Question" hide-footer :lazy=true>
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
                          placeholder="name"></b-form-input>
            <b-form-invalid-feedback  v-for="error in form.errors.name"
                                      class="modal-invalid-feedback"
                                      :key="error">
              {{ error }}
            </b-form-invalid-feedback>
          </b-form-group>

          <b-form-group id="descriptionFieldGroup"
                              label="Description:"
                              label-for="descriptionField">
            <b-form-input id="descriptionField"
                          v-model.trim="form.fields.description"
                          type="text"
                          :state="form.errors.description.length == 0 ? null : false"
                          placeholder="description"></b-form-input>
            <b-form-invalid-feedback  v-for="error in form.errors.description"
                                      class="modal-invalid-feedback"
                                      :key="error">
              {{ error }}
            </b-form-invalid-feedback>
          </b-form-group>

          <b-form-group id="categoryFieldGroup"
                              label="Category:"
                              label-for="categoryField">
            <b-form-input id="categoryField"
                          v-model.trim="form.fields.category"
                          type="text"
                          :state="form.errors.category.length == 0 ? null : false"
                          placeholder="category"></b-form-input>
            <b-form-invalid-feedback  v-for="error in form.errors.category"
                                      class="modal-invalid-feedback"
                                      :key="error">
              {{ error }}
            </b-form-invalid-feedback>
          </b-form-group>

          <input type="submit" value="Save" class="btn btn-primary">
          <b-btn variant="danger" @click="hideModal">Cancel</b-btn>
        </form>
      </b-modal>
    </b-btn>

</template>

<script>
  import questionResource from '@/questions/resource'
  import baseForm from '@/forms'

  export default {
    extends: baseForm,
    data () {
      return {
        form: this.prepareForm({
          name: '',
          description: '',
          category: ''
        }),
        resource: questionResource(this)
      }
    },
    methods: {
      getFormModal () {
        return this.$refs.createQuestionModal
      }
    }
  }
</script>
