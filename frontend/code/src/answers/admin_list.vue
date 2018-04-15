<template>
  <div class="row justify-content-md-center">
    <div class="col-lg-12">
      <h1>List of answers</h1>
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
            <td>{{question.name}}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
  import contestCreateDialog from '@/contests/dialogs/create'
  import questionResource from '@/questions/resource'

  export default {
    data () {
      return {
        questions: [],
        resource: questionResource(this)
      }
    },
    created: function () {
      this.refresh()
    },
    methods: {
      refresh () {
        this.resource.get().then((response) => {
          this.questions = response.data.questions
        })
      }
    }
  }
</script>
