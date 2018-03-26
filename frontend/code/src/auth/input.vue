<template>
  <div class="form-group" v-bind:class="{ 'has-error': field.error }">
    <label class="control-label">{{ field.error }}</label>
    <input type="text" class="form-control" v-bind:class="{ 'form-control-danger': field.error }" v-bind:placeholder="placeholder" v-model="field.value">
  </div>
</template>

<script>
  export default {
    props: ['field', 'placeholder']
  }
</script>
