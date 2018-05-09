<template>
  <div class="row justify-content-md-center">
    <div class="col-lg-12">
      <div v-if="showView('connecting')">
        Connecting...
      </div>

      <div v-if="showView('highscore')">
        This is highscore
      </div>

      <question
                v-if="showView('question')"
                :question_uuid="question_uuid"
                :timestamp="timestamp"
                :team_name="team_name"
                :answer_uuid="answer_uuid"
                :is_correct="is_correct"
      ></question>
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
        question_uuid: null,
        timestamp: null
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
        this.question_uuid = data.view_data.question_uuid
        this.team_name = data.view_data.team_name
        this.answer_uuid = data.view_data.answer_uuid
        this.is_correct = data.view_data.is_correct
        this.timestamp = data.timestamp
      }
      this.$connect()
    },
    components: {
      question
    }
  }
</script>
