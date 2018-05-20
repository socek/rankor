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
        <b-btn @click="onWelcome(screen)" variant="primary" size="small">
          Show Welcome
        </b-btn>

        <b-btn @click="onHighscore(screen)" variant="primary" size="small">
          Show Highscore
        </b-btn>

        <b-btn :to="{name: 'GameScreen', params: makeParams(screen)}" variant="warning" size="small">
          <icon name="play"></icon>
        </b-btn>

        <b-btn @click="onDelete(screen)" variant="danger" size="small">
          <icon name="trash"></icon>
        </b-btn>
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
        return this.screenResource.doCommand(params, data)
      },
      onWelcome (screen) {
        this.changeView(screen, 'welcome')
      },
      onHighscore (screen) {
        this.changeView(screen, 'highscore')
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
