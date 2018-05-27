<template>
  <div class="row justify-content-md-center">
    <div class="col-lg-12">
      <h1>Game: {{game.name}}</h1>
      <viewButtons></viewButtons>
      <teamComponent></teamComponent>
      <questionsComponent></questionsComponent>
    </div>
  </div>
</template>

<script>
  import gameResource from '@/games/resource'
  import questionsComponent from '@/host/components/questions'
  import teamComponent from '@/host/components/teams'
  import viewButtons from '@/host/components/viewButtons'

  export default {
    data () {
      return {
        game: {
          name: ''
        },
        gameResource: gameResource(this)
      }
    },
    created () {
      this.$store.dispatch('breadcrumb/HostView', this)
      this.refresh()
    },
    methods: {
      refresh () {
        let params = {game_id: this.$route.params.game_id}
        this.gameResource.get(params).then(response => {
          this.game = response.data
        })
      }
    },
    components: {
      questionsComponent,
      teamComponent,
      viewButtons
    }
  }
</script>
