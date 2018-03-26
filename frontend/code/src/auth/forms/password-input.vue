<template>
  <div class="form-group" :class="{ 'has-error': field.error }">
    <label class="control-label">{{ field.error }}</label>
    <input type="password" class="form-control" :class="{ 'form-control-danger': field.error }" :placeholder="placeholder" v-model="field.value">
  </div>
</template>

<script>
  export default {
    props: ['form', 'field', 'placeholder']
  }
</script>
