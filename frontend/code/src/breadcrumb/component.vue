<template>
  <b-breadcrumb :items="items"/>
</template>

<script>
export default {
  computed: {
    items () {
      for (let index = 0; index < this.$store.state.breadcrumb.crumbs.length; index++) {
        let crumb = this.$store.state.breadcrumb.crumbs[index]
        if (crumb.textMethod) {
          crumb.text = crumb.textMethod()
        }
      }
      return this.$store.state.breadcrumb.crumbs
    }
  }
}
</script>
