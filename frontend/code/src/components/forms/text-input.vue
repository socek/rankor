<template>
  <div role="group">
    <b-form-input v-model.trim="field.value"
        type="text"
        :state="field.error ? false : ''"
        :placeholder="placeholder"></b-form-input>
    <b-form-invalid-feedback>
      {{ field.error }}
    </b-form-invalid-feedback>
  </div>
</template>

<script>
  export default {
    props: ['form', 'field', 'placeholder']
  }
</script>
