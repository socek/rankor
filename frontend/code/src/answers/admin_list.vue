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
          <tr v-for="(answer, index) in answers">
            <td scope="row">{{index + 1}}</td>
            <td>{{question.name}}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
  import answerResource from '@/answers/resource'

  export default {
    data () {
      return {
        answers: [],
        resource: answerResource(this),
        contest_uuid: this.$route.params.contest_uuid,
        question_uuid: this.$route.params.question_uuid
      }
    },
    created: function () {
      this.refresh()
    },
    methods: {
      refresh () {
        this.resource.get().then((response) => {
          this.answers = response.data.answers
        })
      }
    }
  }
</script>
