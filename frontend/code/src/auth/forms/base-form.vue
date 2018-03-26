<template>
  <b-form @submit.prevent="onSubmit">
    <b-form-invalid-feedback>
      {{ form.error }}
    </b-form-invalid-feedback>

    <slot></slot>
  </b-form>
</template>

<script>
  import axios from 'axios'

  export default {
    props: ['form', 'url'],
    init (fields) {
      this.fields = fields
      let form = {
        error: null,
        fields: {}
      }
      for (let fieldName of fields) {
        form.fields[fieldName] = {
          error: null,
          value: ''
        }
      }
      return form
    },
    reset (form) {
      for (let name of Object.keys(form.fields)) {
        let field = form.fields[name]
        field.error = ''
        field.value = ''
      }
    },
    methods: {
      onSubmit (event) {
        var self = this
        let data = this.form.fields
        axios.post(
          this.url,
          data,
          {
            responseType: 'json',
            headers: {
              'Content-Type': 'application/json'
            }
          }
        )
        .then(function (response) {
          self.$emit('onSuccess', data)
        })
        .catch(function (error) {
          if (error.response.status === 400) {
            var data = error.response.data
            console.log(data)
            self.$emit('onFail', data)
          } else {
            throw error
          }
        })
      }
    }
  }
</script>
