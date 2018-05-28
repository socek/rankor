<template>
  <b-jumbotron :header="game ? game.name : ''">
    <p>{{ game ? game.welcome_message : '' }}</p>
  </b-jumbotron>
</template>

<script>
  import gameResource from '@/games/resource'

  export default {
    data () {
      return {
        game: null,
        resource: gameResource(this)
      }
    },
    created () {
      this.refresh()
    },
    methods: {
      refresh () {
        this.resource.get({game_id: this.$route.params.game_id}).then(response => {
          this.game = response.data
        })
      },

      getText () {
        if (this.game) {
          return this.game.welcome_message
        } else {
          return ''
        }
      }
    }
  }
</script>

<style scoped>
p {
  white-space: pre;
}
</style>
