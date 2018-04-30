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
      fetchContent () {
        return this.resource.get({contest_uuid: this.contest_uuid})
      },
      onSave () {
        this.resource.update({contest_uuid: this.contest_uuid}, this.form.fields).then((response) => {
          this.$refs.dialog.hideModal()
          this.$emit('onSuccess')
        }).catch(this.onError)
      }
    },
    components: {
      dialogform
    }
  }
</script>

<style>
  .modal-spiner {
    text-align: center;
  }
</style>
