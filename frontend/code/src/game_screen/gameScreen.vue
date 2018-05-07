<template>
  <div class="row justify-content-md-center">
    <div class="col-lg-12">
      <div v-if="showView('connecting')">
        Connecting...
      </div>

      <div v-if="showView('highscore')">
        This is highscore
      </div>

      <div v-if="showView('question')">
        This is question
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        view: 'connecting',
        connected: false
      }
    },
    methods: {
      showView (name) {
        return this.view === name
      }
    },
    created () {
      this.$options.sockets.onopen = (data) => {
        this.connected = true
        this.$socket.send('game_uuid:' + this.$route.params.game_uuid)
      }
      this.$options.sockets.onmessage = (event) => {
        let data = JSON.parse(event.data)
        this.view = data.view
      }
      this.$connect()
    }
  }
</script>
