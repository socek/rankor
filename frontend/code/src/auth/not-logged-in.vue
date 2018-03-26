<template>
  <div class="row justify-content-md-center">
    <div class="col-lg-4">
      <h1>Please log in</h1>
        <b-form @submit="form.onSubmit($event, onSuccess)">
          <b-form-invalid-feedback :force-show="true">{{form.data.error}}</b-form-invalid-feedback>
          <b-form-group id="form_email_label"
                        label="Email address:"
                        label-for="form_email"
                        description="We'll never share your email with anyone else.">
            <b-form-input id="form_email"
                          type="email"
                          v-model="form.data.fields.email.value"
                          required
                          placeholder="Enter email">
            </b-form-input>
          </b-form-group>

          <b-form-group id="form_password_label"
                        label="Password:"
                        label-for="form_password">
            <b-form-input id="form_password"
                          type="password"
                          v-model="form.data.fields.password.value"
                          required
                          placeholder="Enter password">
            </b-form-input>
          </b-form-group>
          <b-button type="submit" variant="primary">Login</b-button>
        </b-form>
    </div>
  </div>
</template>

<script>
import User from '@/models/user'
import FormSerializer from '@/auth/serializer'

export default {
  props: ['is_authenticated'],
  data () {
    return {
      form: new FormSerializer('/api/auth/login', ['email', 'password'])
    }
  },
  methods: {
    onSuccess () {
      User.logIn()
      this.$router.push({name: 'Dashboard'})
      location.reload()
    }
  }
}
</script>
