<template>
  <div>
    <h2>Screens
      <b-btn size="sm" variant="primary" @click="onCreate">
        <icon name="plus"></icon>
      </b-btn>
    </h2>
    <ul class="screens">
      <li v-for="(screen, index) in screens">
        Screen {{ index + 1 }}
        <div>
          Commands:
          <b-btn @click="onWelcome(screen)" :variant="getScreenVariant(screen, 'welcome')" size="small">
            Show Welcome
          </b-btn>

          <b-btn @click="onHighscore(screen)" :variant="getScreenVariant(screen, 'highscore')" size="small">
            Show Highscore
          </b-btn>

          <b-btn @click="onQuestions(screen)" :variant="getScreenVariant(screen, 'questions')" size="small">
            Show Questions
          </b-btn>

          <b-btn :disabled="true" :variant="getScreenVariant(screen, 'question')" size="small">
            Question
          </b-btn>
        </div>

        <div>
          Actions:
          <b-btn :to="{name: 'GameScreen', params: makeParams(screen)}" variant="warning" size="small">
            <icon name="play"></icon>
          </b-btn>

          <b-btn @click="onDelete(screen)" variant="danger" size="small">
            <icon name="trash"></icon>
          </b-btn>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
  import screenResource from '@/screen/resource'

  export default {
    data () {
      return {
        screenResource: screenResource(this),
        screens: [],
        params: {
          game_id: this.$route.params.game_id
        }
      }
    },
    created () { this.refresh() },
    methods: {
      getScreenVariant (screen, view) {
        return screen.view === view ? 'danger' : 'primary'
      },
      refresh () {
        this.screenResource.listScreens(this.params).then(response => {
          this.screens = response.data
        })
      },
      makeParams (screen) {
        return {
          game_id: this.params.game_id,
          screen_id: screen.id
        }
      },
      changeView (screen, view) {
        const params = this.makeParams(screen)
        const data = {
          'name': 'change_view',
          'data': {
            'view': view
          }
        }
        return this.screenResource.doCommand(params, data).then(response => {
          screen.view = view
        })
      },
      onWelcome (screen) {
        this.changeView(screen, 'welcome')
      },
      onHighscore (screen) {
        this.changeView(screen, 'highscore')
      },
      onQuestions (screen) {
        this.changeView(screen, 'questions')
      },
      onCreate () {
        this.screenResource.createScreen(this.params, {}).then(response => {
          this.refresh()
        })
      },
      onDelete (screen) {
        const params = this.makeParams(screen)
        this.screenResource.deleteScreen(params, {}).then(response => {
          this.refresh()
        })
      }
    }
  }
</script>

<style>
  ul.screens li {
    margin-top: 3px;
    margin-bottom: 3px;
  }
</style>
