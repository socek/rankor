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
      refreshForm (force = false) {
        for (let name in this.form.fields) {
          if (force || !this.form.fields[name]) this.form.fields[name] = this.form.defaults[name]
          this.form.errors[name] = []
        }
        this.form.errors._schema = []
      },
      onError (response) {
        this.refreshForm()
        for (let name in response.body) {
          this.form.errors[name] = response.body[name]
        }
      },
      moveModalToTopOfTheDOM () {
        let div = this.$el.querySelector('div')
        if (div) document.body.appendChild(div)
      },
      showModal (modal) {
        this.moveModalToTopOfTheDOM()
        this.refreshForm(true)
        this.getFormModal().show()
      },
      hideModal (modal) {
        this.getFormModal().hide()
      },
      onSave () {
        this.resource.save({}, this.form.fields).then((response) => {
          this.hideModal()
          this.$emit('onSuccess')
        }).catch(this.onError)
      }
    }
  }
</script>
