<template>
  <span>
    <h2>Questions</h2>

    <div v-for="(questions, category) in categories">
      <table class="table table-striped table-sm">
        <tr class="title table-success">
          <th scope="col" colspan="5"><strong>{{ category }}</strong></th>
        </tr>
        <tr class="table-secondary">
          <th scope="col">#</th>
          <th scope="col">Name</th>
          <th scope="col">Status</th>
          <th scope="col">Team</th>
          <th scope="col">Actions</th>
        </tr>
        <tbody>
          <tr v-for="(question, index) in questions">
            <td scope="row">{{index + 1}}</td>
            <td>{{question.name}}</td>
            <td>
              <icon name="check" style="color: green" v-if="question.status == 'correct'"></icon>
              <icon name="times" style="color: red;" v-if="question.status == 'incorrect'"></icon>
              <icon name="hourglass" v-if="question.status == 'not started'"></icon>
            </td>
            <td>{{question.team}}</td>
            <td>
              <router-link :to="route_to_question(question)">
                <icon name="gavel"></icon>
              </router-link>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

  </span>
</template>

<script>
  import hostResource from '@/host/resource'

  export default {
    data () {
      return {
        categories: {},
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
            game_id: this.$route.params.game_id,
            question_id: question.id
          }
        }
      },
      refresh () {
        let params = {game_id: this.$route.params.game_id}
        this.resource.list_questions(params).then((response) => {
          this.categories = response.data.categories
        })
      }
    }
  }
</script>
