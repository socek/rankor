<template>
  <b-btn size="sm" :variant="variant" @click="showModal">
    <slot name="anhor"></slot>

    <b-modal ref="baseModal" :title="title" hide-footer>
      <form @submit.prevent="$emit('onSave', $event.target.form)" v-show="!isLoading">
        <b-form-invalid-feedback  v-for="error in form.errors._schema"
                                  :key="error"
                                  :force-show="true" >
          {{ error }}
        </b-form-invalid-feedback>

        <slot name="content"></slot>

        <input type="submit" value="Save" class="btn btn-primary save">
        <b-btn class="cancel" variant="danger" @click="hideModal">Cancel</b-btn>
      </form>
      <div v-show="isLoading" class="modal-spiner">
        <icon name="sync" scale="2" spin></icon>
      </div>
    </b-modal>
  </b-btn>
</template>

<script>
  export default {
    props: {
      form: Object,
      title: String,
      variant: {
        type: String,
        default: 'primary'
      },
      fetchContent: {
        default: false
      }
    },
    data () {
      return {
        isLoading: true,
        withLoading: false
      }
    },
    methods: {
      showModal (modal) {
        this.moveModalToTopOfTheDOM()
        this.isLoading = this.withLoading
        this.$refs.baseModal.show()
        if (this.fetchContent) {
          this.fetchContent().then((response) => {
            this.form.defaults = response.body
            this.isLoading = false
            this.$emit('onRefresh', true)
          })
        } else {
          this.$emit('onRefresh', true)
        }
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

<style scoped>
  .modal-spiner {
    text-align: center;
  }
  .save {
    float: left;
  }
  .cancel {
    float: right;
  }
</style>
