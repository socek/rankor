<template>
  <span>
    <h2>Teams <createDialog :game_id="game_id" @onSuccess="refresh"></createDialog></h2>
    <table class="table table-striped">
      <thead class="thead-dark">
        <tr>
          <th scope="col">#</th>
          <th scope="col">Name</th>
          <th scope="col">Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(team, index) in teams">
          <td scope="row">{{index + 1}}</td>
          <td>{{team.name}}</td>
          <td>
          </td>
        </tr>
      </tbody>
    </table>
  </span>
</template>

<script>
  import teamResource from '@/team/resource'
  import createDialog from '@/team/dialogs/create'

  export default {
    data () {
      return {
        teams: [],
        resource: teamResource(this),
        game_id: this.$route.params.game_id
      }
    },
    created () {
      this.refresh()
    },
    methods: {
      refresh () {
        let params = {
          game_id: this.game_id
        }
        this.resource.list(params).then((response) => {
          this.teams = response.data
        })
      }
    },
    components: {
      createDialog
    }
  }
</script>
