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

      <question v-if="showView('question')">
      </question>

      <questions v-if="showView('questions')" :game_id="game_id">
      </questions>
    </div>
  </div>
</template>

<script>
  import question from '@/game_screen/question'
  import questions from '@/game_screen/questions'
  import highscore from '@/game_screen/highscore'
  import welcome from '@/game_screen/welcome'

  export default {
    data () {
      return {
        connected: false,
        game_id: this.$route.params.game_id
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
    computed: {
      view () {
        return this.$store.state.screen.view
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
        this.$store.dispatch('screen/parseData', data)
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
      welcome,
      questions
    }
  }
</script>

