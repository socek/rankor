<template>
  <form v-on:submit.prevent="onSubmit">
    <div class="form-group has-error" v-if="form.error">
      <label class="control-label">{{ form.error }}</label>
    </div>

    <slot></slot>
  </form>
</template>

<script>
  import axios from 'axios'

  export default {
    props: ['form', 'url'],
    init (fields) {
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
    methods: {
      onSubmit: function (event) {
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
          var data = response.data
          if (data.form.validated) {
            self.$emit('onSuccess', data)
          } else {
            self.$emit('onFail', data)
          }
        })
      }
    }
  }
</script>
