<template>
  <span>
    <div v-for="(questions, category) in categories">
      <table class="table table-striped table-sm">
        <tr class="title table-success">
          <th scope="col" colspan="5"><strong>{{ category }}</strong></th>
        </tr>
        <tr class="table-secondary">
          <th scope="col">#</th>
          <th scope="col">Status</th>
          <th scope="col">Team</th>
        </tr>
        <tbody>
          <tr v-for="(question, index) in questions">
            <td scope="row">{{index + 1}}</td>
            <td>
              <span style="color: green" v-if="question.status == 'correct'">Success</span>
              <span style="color: red;" v-if="question.status == 'incorrect'">Fail</span>
              <span v-if="question.status == 'not started'"></span>
            </td>
            <td>{{question.team}}</td>
          </tr>
        </tbody>
      </table>
    </div>

  </span>
</template>

<script>
  import hostResource from '@/host/resource'

  export default {
    props: ['game_id'],
    data () {
      return {
        categories: {},
        params: {
          game_id: this.game_id
        },
        resource: hostResource(this)
      }
    },
    created () {
      this.refresh()
    },
    methods: {
      refresh () {
        console.log(this.params)
        this.resource.list_questions(this.params).then((response) => {
          this.categories = response.data.categories
        })
      }
    }
  }
</script>
