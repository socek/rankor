<template>
  <div class="row justify-content-md-center">
    <div class="col-lg-4">
      <h1>Please log in</h1>
      <form @submit.prevent="onSubmit">
        <b-form-invalid-feedback  :force-show="true"
                                  v-for="error in errors._schema"
                                  :key="error">
          {{ error }}
        </b-form-invalid-feedback>

        <b-form-group id="emailFieldGroup"
                      label="Email:"
                      label-for="emailField">
          <b-form-input id="emailField"
                        type="text"
                        placeholder="Email"
                        v-model.trim="fields.email"
                        :state="errors.email.length == 0 ? null : false">
          </b-form-input>
          <b-form-invalid-feedback v-for="error in errors.email" :key="error">
            {{ error }}
          </b-form-invalid-feedback>
        </b-form-group>

        <b-form-group id="passwordFieldGroup"
                      label="Password:"
                      label-for="passwordField">
          <b-form-input id="passwordField"
                        type="password"
                        placeholder="Password"
                        :state="errors.password.length == 0 ? null : false"
                        v-model.trim="fields.password">
          </b-form-input>
          <b-form-invalid-feedback  v-for="error in errors.password"
                                    :key="error">
            {{ error }}
          </b-form-invalid-feedback>
        </b-form-group>
        <input type="submit" value="Login" class="btn btn-primary">
      </form>
    </div>
  </div>
</template>

<script>
import authResource from '@/auth/resource'

export default {
  data () {
    return {
      fields: {
        email: '',
        password: ''
      },
      errors: {
        _schema: [],
        email: [],
        password: []
      },
      resource: authResource(this).login
    }
  },
  methods: {
    onSubmit () {
      this.resource.save({}, this.fields).then((response) => {
        this.$store.commit('auth/logIn', response.body.jwt)
        this.$router.push({name: 'Dashboard'})
      }).catch((response) => {
        for (let item in this.errors) {
          this.errors[item] = []
        }
        for (let item in response.body) {
          this.errors[item] = response.body[item]
        }
      })
    }
  }
}
</script>
