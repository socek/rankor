<template>
  <span>
    <h2>Teams</h2>
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

  export default {
    data () {
      return {
        teams: [],
        resource: teamResource(this)
      }
    },
    created () {
      this.refresh()
    },
    methods: {
      refresh () {
        let params = {
          game_uuid: this.$route.params.game_uuid
        }
        this.resource.list(params).then((response) => {
          this.teams = response.data
        })
      }
    }
  }
</script>
