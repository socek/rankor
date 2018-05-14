<template>
  <dialogform
    title="Edit Contest"
    variant="link"
    :form="form"
    :fetchContent="fetchContent"
    @onSave="onSave"
    @onRefresh="refreshForm"
    ref="dialog">

    <template slot="anhor">
      <icon name="edit"></icon>
    </template>

    <template slot="content">
      <b-form-group
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

      <b-form-group
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

      <b-form-group
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
    </template>

  </dialogform>
</template>



<script>
  import questionResource from '@/questions/resource'
  import dialogform from '@/common/dialogForm'
  import baseForm from '@/forms'

  export default {
    props: ['question_id'],
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
      fetchContent () {
        return this.resource.get({
          contest_id: this.$route.params.contest_id,
          question_id: this.question_id})
      },
      saveCall () {
        return this.resource.update(
          {question_id: this.question_id},
          this.form.fields)
      }
    },
    components: {
      dialogform
    }
  }
</script>
