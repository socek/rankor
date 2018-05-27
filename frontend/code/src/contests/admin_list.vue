<template>
  <div class="row justify-content-md-center">
    <div class="col-lg-12">
      <h1>Contests <contestCreateDialog @onSuccess="refresh"></contestCreateDialog></h1>
      <table class="table table-striped">
        <thead class="thead-dark">
          <tr>
            <th scope="col">#</th>
            <th scope="col">Name</th>
            <th scope="col">Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(contest, index) in contests">
            <td scope="row">{{index + 1}}</td>
            <td>{{contest.name}}</td>
            <td>
              <router-link :to="{name: 'Questions', params: {contest_id: contest.id}}">
                <icon name="list-ol"></icon>
              </router-link>
              <contestEditDialog @onSuccess="refresh" :contest_id="contest.id"></contestEditDialog>
              <gameStart @onSuccess="refresh" :contest_id="contest.id"></gameStart>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
  import contestCreateDialog from '@/contests/dialogs/create'
  import contestEditDialog from '@/contests/dialogs/edit'
  import contestResource from '@/contests/resource'
  import gameStart from '@/games/dialogs/start'

  export default {
    data () {
      return {
        contests: [],
        resource: contestResource(this)
      }
    },
    created () {
      this.$store.dispatch('breadcrumb/Contests', this)
      this.refresh()
    },
    methods: {
      refresh () {
        this.resource.list().then((response) => {
          this.contests = response.data.contests
        })
      }
    },
    components: {
      contestCreateDialog,
      contestEditDialog,
      gameStart
    }
  }
</script>
