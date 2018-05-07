<template>
  <div class="row justify-content-md-center">
    <div class="col-lg-12">
      <div v-if="showView('connecting')">
        Connecting...
      </div>

      <div v-if="showView('highscore')">
        This is highscore
      </div>

      <question v-if="showView('question')" :question_uuid="question_uuid"></question>
    </div>
  </div>
</template>

<script>
  import question from '@/game_screen/question'

  export default {
    data () {
      return {
        view: 'connecting',
        connected: false,
        question_uuid: null
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
        this.question_uuid = data.question_uuid
      }
      this.$connect()
    },
    components: {
      question
    }
  }
</script>
