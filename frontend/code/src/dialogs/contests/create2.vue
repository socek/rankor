<template>
  <transition name="modal">
    <div class="modal-mask" @click="close" v-show="show">
      <div class="modal-container" @click.stop>
        <div class="modal-header">
            <h3>New Post</h3>
        </div>
        <div class="modal-body">
          <label class="form-label">
            Title
            <input class="form-control">
          </label>
          <label class="form-label">
            Body
            <textarea rows="5" class="form-control"></textarea>
          </label>
        </div>
        <div class="modal-footer text-right">
          <button class="modal-default-button" @click="savePost()">
            Save
          </button>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
  export default {
    props: ['show'],
    methods: {
      close: function () {
        this.$emit('close')
      },
      savePost: function () {
        // Some save logic goes here...

        this.close()
      }
    }
  }
</script>
