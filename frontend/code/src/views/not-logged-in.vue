<template>
  <div class="row justify-content-md-center">
    <div class="col-lg-4">
      <h1>Please log in</h1>
      <baseForm :form="form" @onSuccess="onSuccess" @onFail="onFail" url="/api/auth/login">
        <textInput :form="form" :field="form.fields.email" placeholder="Email"></textInput>
        <passwordInput :form="form" :field="form.fields.password" placeholder="Password"></passwordInput>
        <input type="submit" name="login" class="btn btn-primary" value="Login">
      </baseForm>
    </div>
  </div>
</template>

<script>
  import baseForm from '@/components/forms/base-form'
  import textInput from '@/components/forms/text-input'
  import passwordInput from '@/components/forms/password-input'
  import User from '@/models/user'

  export default {
    props: ['is_authenticated'],
    data () {
      return {
        form: baseForm.init(['email', 'password'])
      }
    },
    methods: {
      onSuccess (data) {
        User.logIn()
        this.$router.push({name: 'Dashboard'})
        location.reload()
      },
      onFail (data) {
        this.form = data.form
      }
    },
    components: {
      textInput,
      passwordInput,
      baseForm
    }
  }
</script>
