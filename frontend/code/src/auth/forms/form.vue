<template>
  <form v-on:submit.prevent="onSubmit">
    <div class="form-group has-error" v-if="form.error">
      <label class="control-label">{{ form.error }}</label>
    </div>

    <slot></slot>

    <input type="submit" name="login" class="login loginmodal-submit" value="Login">
  </form>
</template>

<script>
  export default {
      data () {
        return {
          form: {
            error: null,
            fields: {
              email: {
                error: null,
                value: ''
              },
              password: {
                error: null,
                value: ''
              }
            }
          }
        }
      },
      methods: {
        onSubmit: function (event) {
          var self = this
          axios.post(
            '/api/auth/login',
            this.form.fields,
            {
              responseType: 'json'
            }
          )
          .then(function (response) {
            var data = response.data
            if (data.form.validated) {
              location.reload()
            } else {
              self.form = data.form
            }
          })
        }
      }
    }
</script>
