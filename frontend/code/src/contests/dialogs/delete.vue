<template>
  <vueDialog  title="Are you sure?"
              variant="danger"
              ref="dialog">

    <template slot="anhor">
      <icon name="trash-alt"></icon>
    </template>

    <template slot="content">
      <p>Do you really want to remove "{{ contest.name }}"?</p>
      <div>
        <b-btn class="cancel" @click="onHide">Cancel</b-btn>
        <b-btn class="delete" @click="onDelete" variant="danger">Remove</b-btn>
      </div>
    </template>

  </vueDialog>
</template>

<script>
  import contestResource from '@/contests/resource'
  import vueDialog from '@/common/dialog'

  export default {
    props: ['contest'],
    data () {
      return {
        resource: contestResource(this)
      }
    },
    methods: {
      onHide () {
        this.$refs.dialog.hideModal()
      },
      onDelete () {
        this.resource.delete({'contest_id': this.contest.id}).then(response => {
          this.$refs.dialog.hideModal()
          this.$emit('deleted')
        })
      }
    },
    components: {
      vueDialog
    }
  }
</script>

<style scoped>
.delete {
  float: left;
}
.cancel {
  float: right;
}
</style>
