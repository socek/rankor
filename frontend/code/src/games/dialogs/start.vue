<template>
  <dialogform
    title="Start a Contest"
    variant="link"
    :form="form"
    @onSave="onSave"
    @onRefresh="refreshForm"
    ref="dialog">

    <template slot="anhor">
      <icon name="play-circle"></icon>
    </template>

    <template slot="content">
      <b-form-group
                          label="Name:"
                          label-for="nameField">
        <b-form-input id="nameField"
                      v-model.trim="form.fields.name"
                      type="text"
                      :state="form.errors.name.length == 0 ? null : false"
                      placeholder="Game name"></b-form-input>
        <b-form-invalid-feedback  v-for="error in form.errors.name"
                                  class="modal-invalid-feedback"
                                  :key="error">
          {{ error }}
        </b-form-invalid-feedback>
      </b-form-group>

      <b-form-group id="welcomeMessageFieldGroup"
                          label="Welcome message:"
                          label-for="welcomeMessageField">
        <b-form-textarea id="welcomeMessageField"
                      v-model.trim="form.fields.welcome_message"
                      type="text"
                      :state="form.errors.welcome_message.length == 0 ? null : false"
                      :rows="3"
                      :max-rows="6"
                      placeholder="welcome message"></b-form-textarea>
        <b-form-invalid-feedback  v-for="error in form.errors.welcome_message"
                                  class="modal-invalid-feedback"
                                  :key="error">
          {{ error }}
        </b-form-invalid-feedback>
      </b-form-group>

      <input type="hidden" v.model.trim="form.fields.contest_id">
    </template>
  </dialogform>
</template>

<script>
  import gameResource from '@/games/resource'
  import baseForm from '@/forms'
  import dialogform from '@/common/dialogForm'

  export default {
    props: ['contest_id'],
    extends: baseForm,
    data () {
      return {
        form: this.prepareForm({
          name: '',
          welcome_message: '',
          contest_id: this.contest_id
        }),
        resource: gameResource(this)
      }
    },
    components: {
      dialogform
    }
  }
</script>
