<template>
  <table class="table table-striped">
    <thead>
      <tr class="table-success">
        <th scope="col">#</th>
        <th scope="col">Nazwa</th>
        <th scope="col">Odpowiedzi</th>
        <th scope="col">Poprawnych</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(team, index) in teams">
        <td>{{ index + 1 }}</td>
        <td>{{ team.name }}</td>
        <td>{{ team.count }}</td>
        <td>{{ team.wins }}</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
  import hostResource from '@/host/resource'

  export default {
    data () {
      return {
        teams: [],
        resource: hostResource(this)
      }
    },
    methods: {
      getHighscore () {
        const params = {game_id: this.$route.params.game_id}
        return this.resource.get_highscore(params)
      },
      refresh () {
        this.getHighscore().then(response => {
          this.teams = response.body
        })
      }
    },
    created () {
      this.refresh()
    }
  }
</script>
