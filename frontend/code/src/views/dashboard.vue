<template>
  <div class="row justify-content-md-center">
    <div class="col-lg-12">
      <h1>List of contests <contestCreateDialog @onSuccess="refresh"></contestCreateDialog></h1>
      <table class="table table-striped">
        <thead class="thead-dark">
          <tr>
            <th scope="col">#</th>
            <th scope="col">Name</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(contest, index) in contests">
            <td scope="row">{{index + 1}}</td>
            <td>{{contest.name}}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
  // import AjaxView from '../models/ajax'
  import contestCreateDialog from '@/dialogs/contests/create'
  import contestResource from '@/contests/resource'

  export default {
    data () {
      return {
        contests: [],
        resource: contestResource(this)
      }
    },
    created: function () {
      this.refresh()
    },
    methods: {
      refresh () {
        this.resource.get().then((response) => {
          this.contests = response.data.contests
        })
      }
    },
    components: {
      contestCreateDialog
    }
  }
</script>

