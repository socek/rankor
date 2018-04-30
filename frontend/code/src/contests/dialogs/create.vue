<template>
  <dialogform
    title="Create Contest"
    :form="form"
    @onSave="onSave"
    @onRefresh="refreshForm"
    ref="dialog">

    <template slot="anhor">
      <icon name="plus"></icon>
    </template>

    <template slot="content">
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
    </template>
  </dialogform>
</template>

<script>
  import contestResource from '@/contests/resource'
  import baseForm from '@/forms'
  import dialogform from '@/common/dialogForm'

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
    components: {
      dialogform
    }
  }
</script>
