<template>
  <dialogform
    title="Create Team"
    :form="form"
    @onSave="onSave"
    @onRefresh="refreshForm"
    ref="dialog">

    <template slot="anhor">
      <icon name="plus"></icon>
    </template>

    <template slot="content">
      <b-form-group
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
      <input type="hidden"
    </template>
  </dialogform>
</template>

<script>
  import teamResource from '@/team/resource'
  import baseForm from '@/forms'
  import dialogform from '@/common/dialogForm'

  export default {
    props: ['game_id'],
    extends: baseForm,
    data () {
      return {
        form: this.prepareForm({
          name: '',
          game_id: this.game_id
        }),
        resource: teamResource(this)
      }
    },
    methods: {
      saveCall () {
        return this.resource.save({game_id: this.game_id}, this.form.fields)
      }
    },
    components: {
      dialogform
    }
  }
</script>
