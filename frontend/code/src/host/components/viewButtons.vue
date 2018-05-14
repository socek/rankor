<template>
  <div>
    <b-btn @click="onQuestion" variant="primary" size="small">
      Show Question
    </b-btn>

    <b-btn @click="onHighscore" variant="warning" size="small">
      Show Highscore
    </b-btn>
  </div>
</template>

<script>
  import hostResource from '@/host/resource'

  export default {
    data () {
      return {
        hostResource: hostResource(this),
        params: {
          game_id: this.$route.params.game_id
        }
      }
    },
    methods: {
      changeView (view) {
        return () => {
          this.hostResource.change_view(this.params, {'view': view})
        }
      },
      onQuestion () {
        this.changeView('question')()
      },
      onHighscore () {
        this.changeView('highscore')()
      }
    }
  }
</script>
