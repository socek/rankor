<template>
  <div>
    <b-btn @click="showModal" v-if="!isAuthenticated" variant="primary" size="small">
      Sign Up
    </b-btn>

    <b-modal id="signUpModal" ref="signUpModal" title="Sign Up" hide-footer>
      <form @submit.prevent="onSubmit">
        <b-form-invalid-feedback  :force-show="true"
                                  v-for="error in errors._schema"
                                  :key="error">
          {{ error }}
        </b-form-invalid-feedback>

        <b-form-group id="registrationEmailFieldGroup"
                      label="Email:"
                      label-for="registrationEmailField">
          <b-form-input id="registrationEmailField"
                        type="text"
                        placeholder="email"
                        v-model.trim="fields.email"
                        :state="errors.email.length == 0 ? null : false">
          </b-form-input>
          <b-form-invalid-feedback v-for="error in errors.email" :key="error">
            {{ error }}
          </b-form-invalid-feedback>
        </b-form-group>

        <b-form-group id="registrationPasswordFieldGroup"
                      label="Password:"
                      label-for="registrationPasswordField">
          <b-form-input id="registrationPasswordField"
                        type="password"
                        placeholder="password"
                        :state="errors.password.length == 0 ? null : false"
                        v-model.trim="fields.password">
          </b-form-input>
          <b-form-invalid-feedback  v-for="error in errors.password"
                                    :key="error">
            {{ error }}
          </b-form-invalid-feedback>
        </b-form-group>
        <b-form-group id="registrationConfirmPasswordFieldGroup"
                      label="Confirm Password:"
                      label-for="registrationConfirmPasswordField">
          <b-form-input id="registrationConfirmPasswordField"
                        type="password"
                        placeholder="password"
                        :state="errors.confirmPassword.length == 0 ? null : false"
                        v-model.trim="fields.confirmPassword">
          </b-form-input>
          <b-form-invalid-feedback  v-for="error in errors.confirmPassword"
                                    :key="error">
            {{ error }}
          </b-form-invalid-feedback>
        </b-form-group>
        <input type="submit" value="Sign Up" class="btn btn-primary">
        <b-btn variant="danger" @click="hideModal">Cancel</b-btn>
      </form>
    </b-modal>
  </div>
</template>

<script>
import authResource from '@/auth/resource'

export default {
  data () {
    return {
      fields: {
        email: '',
        password: '',
        confirmPassword: ''
      },
      errors: {
        _schema: [],
        email: [],
        password: [],
        confirmPassword: []
      },
      resource: authResource(this).signUp
    }
  },
  methods: {
    refresh () {
      for (let name in this.fields) {
        this.fields[name] = ''
        this.errors[name] = ''
      }
      this.errors._schema = ''
    },
    showModal () {
      this.refresh()
      this.$refs.signUpModal.show()
    },
    hideModal () {
      this.$refs.signUpModal.hide()
    },
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
  },
  computed: {
    isAuthenticated () {
      return this.$store.getters['auth/isAuthenticated']
    }
  }
}
</script>
