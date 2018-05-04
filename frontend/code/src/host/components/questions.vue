<template>
  <span>
    <h2>Questions</h2>
    <table class="table table-striped">
      <thead class="thead-dark">
        <tr>
          <th scope="col">#</th>
          <th scope="col">Name</th>
          <th scope="col">Status</th>
          <th scope="col">Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(question, index) in questions">
          <td scope="row">{{index + 1}}</td>
          <td>{{question.name}}</td>
          <td>
            <icon name="check" style="color: green" v-if="question.status == 'correct'"></icon>
            <icon name="times" style="color: red;" v-if="question.status == 'incorrect'"></icon>
            <icon name="hourglass" v-if="question.status == 'not started'"></icon>
          </td>
          <td>
            <router-link :to="route_to_question(question)">
              <icon name="gavel"></icon>
            </router-link>
          </td>
        </tr>
      </tbody>
    </table>
  </span>
</template>

<script>
  import hostResource from '@/host/resource'

  export default {
    data () {
      return {
        questions: [],
        resource: hostResource(this)
      }
    },
    created () {
      this.refresh()
    },
    methods: {
      route_to_question (question) {
        return {
          name: 'HostQuestionView',
          params: {
            game_uuid: this.$route.params.game_uuid,
            question_uuid: question.uuid
          }
        }
      },
      refresh () {
        let params = {game_uuid: this.$route.params.game_uuid}
        this.resource.list_questions(params).then((response) => {
          this.questions = response.data
        })
      }
    }
  }
</script>
