<template>
  <div class="row justify-content-md-center">
    <div class="col-lg-12">
      <h1>Games</h1>
      <table class="table table-striped">
        <thead class="thead-dark">
          <tr>
            <th scope="col">#</th>
            <th scope="col">Name</th>
            <th scope="col">Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(game, index) in games">
            <td scope="row">{{index + 1}}</td>
            <td>{{game.name}}</td>
            <td>
              <router-link :to="{name: 'HostView', params: {game_id: game.id}}">
                <icon name="play"></icon>
              </router-link>
              <gameEditDialog @onSuccess="refresh" :game_id="game.id"></gameEditDialog>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
  import gameEditDialog from '@/games/dialogs/edit'
  import gameResource from '@/games/resource'

  export default {
    data () {
      return {
        games: [],
        resource: gameResource(this)
      }
    },
    created () {
      this.$store.dispatch('breadcrumb/Games', this)
      this.refresh()
    },
    methods: {
      refresh () {
        this.resource.list().then((response) => {
          this.games = response.data.games
        })
      }
    },
    components: {
      gameEditDialog
    }
  }
</script>
