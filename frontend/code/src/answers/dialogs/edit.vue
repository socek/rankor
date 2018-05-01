<template>
  <dialogform
    title="Edit Answer"
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

      <b-form-group>
        <b-form-checkbox
                         v-model="form.fields.is_correct"
                         :value="true"
                         :unchecked-value="false">
          Correct answer
        </b-form-checkbox>
      </b-form-group>
    </template>
  </dialogform>
</template>

<script>
  import answerResource from '@/answers/resource'
  import baseForm from '@/forms'
  import dialogform from '@/common/dialogForm'

  export default {
    props: ['answer_uuid'],
    extends: baseForm,
    data () {
      return {
        form: this.prepareForm({
          name: '',
          description: '',
          is_correct: false
        }),
        resource: answerResource(this)
      }
    },
    methods: {
      fetchContent () {
        return this.resource.get({
          contest_uuid: this.$route.params.contest_uuid,
          question_uuid: this.$route.params.question_uuid,
          answer_uuid: this.answer_uuid})
      },
      saveCall () {
        return this.resource.update(
          {answer_uuid: this.answer_uuid},
          this.form.fields)
      }
    },
    components: {
      dialogform
    }
  }
</script>
