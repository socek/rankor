<template>
  <div>
    <h2>Screens
      <b-btn size="sm" variant="primary" @click="onCreate">
        <icon name="plus"></icon>
      </b-btn>
    </h2>
    <ul>
      <li v-for="(screen, index) in screens">
        Screen {{ index + 1 }}
        <b-btn @click="onWelcome(screen)" variant="primary" size="small">
          Show Welcome
        </b-btn>

        <b-btn @click="onHighscore(screen)" variant="warning" size="small">
          Show Highscore
        </b-btn>

        <b-btn @click="onDelete(screen)" variant="danger" size="small">
          Delete
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
      onWelcome (screen) {
        console.log('welcome', screen.id)
      },
      onHighscore (screen) {
        console.log('Highscore', screen.id)
      },
      onCreate () {
        this.screenResource.createScreen(this.params, {}).then(response => {
          this.refresh()
        })
      },
      onDelete (screen) {
        const params = {
          game_id: this.params.game_id,
          screen_id: screen.id
        }
        this.screenResource.deleteScreen(params, {}).then(response => {
          this.refresh()
        })
      }
    }
  }
</script>

<style scoped>
  ul li {
    margin-top: 3px;
    margin-bottom: 3px;
  }
</style>
