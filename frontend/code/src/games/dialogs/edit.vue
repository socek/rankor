<template>
  <dialogform
    title="Edit Game"
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
                      placeholder="Game name"></b-form-input>
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
  import gameResource from '@/games/resource'
  import baseForm from '@/forms'
  import dialogform from '@/common/dialogForm'

  export default {
    props: ['game_id'],
    extends: baseForm,
    data () {
      return {
        is_loading: true,
        form: this.prepareForm({
          name: ''
        }),
        resource: gameResource(this)
      }
    },
    methods: {
      fetchContent () {
        return this.resource.get({game_id: this.game_id})
      },
      saveCall () {
        return this.resource.update(
          {game_id: this.game_id},
          this.form.fields)
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
