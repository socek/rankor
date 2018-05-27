<template>
  <b-breadcrumb :items="items"/>
</template>

<script>
export default {
  computed: {
    items () {
      return this.$store.state.breadcrumb.crumbs
    }
  }
}
</script>
