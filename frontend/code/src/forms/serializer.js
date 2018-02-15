import axios from 'axios'

class FormSerializer {
  constructor (url, fieldNames) {
    this.fieldNames = fieldNames
    this.url = url
    this.reset()
  }

  reset () {
    let self = this
    let data = {
      error: null,
      fields: {}
    }
    self.data = data
    for (let fieldName of this.fieldNames) {
      self.data.fields[fieldName] = {
        error: null,
        value: ''
      }
    }
  }

  onSubmit (event, onSuccess, onFail) {
    var self = this
    event.preventDefault()
    axios.post(
      self.url,
      self.data,
      {
        responseType: 'json',
        headers: {
          'Content-Type': 'application/json'
        }
      }
    )
    .then(function (response) {
      if (onSuccess) {
        onSuccess(self.data)
      }
    })
    .catch(function (error) {
      if (error.response.status === 400) {
        self.data = error.response.data.form
        if (onFail) {
          onFail(self, self.data)
        }
      } else {
        throw error
      }
    })
  }
}

export default FormSerializer
