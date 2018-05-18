<template>
  <div class="row justify-content-md-center">
    <div class="col-lg-12">
      <div v-if="showView('connecting')">
        <icon name="sync" scale="2" spin></icon>
        Connecting...
      </div>

      <div v-if="showView('network_problems')">
        <div>
          <icon name="sync" scale="2" spin></icon>
        </div>
        <div>
          Connecting or network problems...
        </div>
        <b-btn variant="primary" @click="onConnect">
          Try to reconnect
        </b-btn>
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
      },
      onConnect () {
        this.$connect()
      }
    },
    created () {
      this.$options.sockets.onopen = (data) => {
        this.connected = true
        let payload = {
          game_id: this.$route.params.game_id,
          screen_id: this.$route.params.screen_id
        }
        this.$socket.send(JSON.stringify(payload))
        console.log('Connection established')
      }
      this.$options.sockets.onmessage = (event) => {
        let data = JSON.parse(event.data)
        let methods = {
          change_view: (data) => {
            this.view = data.view
          },
          init: (data) => {
            this.view = data.view
          }
        }
        methods[data['name']](data)
      }
      this.$options.sockets.onclose = () => {
        console.log('Connection closed')
        this.connected = false
        this.view = 'network_problems'
      }
      this.$options.sockets.onerror = () => {
        console.log('Connection error')
        this.connected = false
        this.view = 'network_problems'
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

