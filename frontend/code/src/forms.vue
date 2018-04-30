<script>
  export default {
    methods: {
      prepareForm (defaults) {
        let obj = {
          fields: {},
          errors: {_schema: []},
          defaults: defaults
        }
        for (let key in defaults) {
          obj.fields[key] = defaults[name]
          obj.errors[key] = []
        }
        return obj
      },
      onError (response) {
        this.refreshForm()
        for (let name in response.body) {
          this.form.errors[name] = response.body[name]
        }
      },
      refreshForm (force = false) {
        for (let name in this.form.fields) {
          if (force || !this.form.fields[name]) this.form.fields[name] = this.form.defaults[name]
          this.form.errors[name] = []
        }
        this.form.errors._schema = []
      },
      onSave () {
        this.resource.save({}, this.form.fields).then((response) => {
          this.$refs.dialog.hideModal()
          this.$emit('onSuccess')
        }).catch(this.onError)
      }
    }
  }
</script>
