<template>
  <div class="row justify-content-md-center">
    <div class="col-lg-12">
      <div v-if="showView('connecting')">
        Connecting...
      </div>

      <welcome v-if="showView('welcome')">
      </welcome>

      <highscore v-if="showView('highscore')">
      </highscore>

      <question
                v-if="showView('question')"
                :question_id="question_id"
                :timestamp="timestamp"
                :team_name="team_name"
                :answer_id="answer_id"
                :is_correct="is_correct"
      ></question>
    </div>
  </div>
</template>

<script>
  import question from '@/game_screen/question'
  import highscore from '@/game_screen/highscore'
  import welcome from '@/game_screen/welcome'

  export default {
    data () {
      return {
        view: 'connecting',
        connected: false,
        question_id: null,
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
        this.$socket.send('game_id:' + this.$route.params.game_id)
      }
      this.$options.sockets.onmessage = (event) => {
        let data = JSON.parse(event.data)
        this.view = data.view
        this.question_id = data.view_data.question_id
        this.team_name = data.view_data.team_name
        this.answer_id = data.view_data.answer_id
        this.is_correct = data.view_data.is_correct
        this.timestamp = data.timestamp
      }
      this.$connect()
    },
    components: {
      question,
      highscore,
      welcome
    }
  }
</script>

