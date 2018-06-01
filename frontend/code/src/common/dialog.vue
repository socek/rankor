<template>
  <b-btn size="sm" :variant="variant" @click="showModal">
    <slot name="anhor"></slot>

    <b-modal ref="baseModal" :title="title" hide-footer>
      <slot name="content"></slot>
    </b-modal>
  </b-btn>
</template>

<script>
  export default {
    props: {
      title: String,
      variant: {
        type: String,
        default: 'primary'
      }
    },
    methods: {
      showModal (modal) {
        this.moveModalToTopOfTheDOM()
        this.$refs.baseModal.show()
        this.$emit('onRefresh', true)
      },
      moveModalToTopOfTheDOM () {
        let div = this.$el.querySelector('div')
        if (div) document.body.appendChild(div)
      },
      hideModal (modal) {
        this.$refs.baseModal.hide()
      }
    }
  }
</script>
