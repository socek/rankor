<template>
  <span>
    <h1>Question</h1>

    <h2>Team</h2>
    <b-form-select v-model="team" :options="teams" class="mb-3" />

    <h2>Name</h2>
    <p>{{ name }}</p>

    <h2>Description</h2>
    <p>{{ description }}</p>

    <h2>Answers</h2>
    <div>
      <ul>
        <li v-for="(answerObject, index) in answers">
          <input :id="'answer_' + index" type="radio" :value="answerObject.value" v-model="answer">
          <label :for="'answer_' + index" :class="{correct: answerObject.is_correct}">
            {{ answerObject.text }}
          </label>
        </li>
      </ul>
    </div>

    <b-btn variant="primary" @click="onSave">
      Verify
    </b-btn>

  </span>
</template>

<script>
  import teamResource from '@/team/resource'
  import hostResource from '@/host/resource'

  export default {
    data () {
      return {
        name: '',
        description: '',
        team: null,
        answer: null,
        teams: [],
        answers: [],

        game_uuid: this.$route.params.game_uuid,
        question_uuid: this.$route.params.question_uuid,

        teamResource: teamResource(this),
        hostResource: hostResource(this)
      }
    },
    created () {
      this.refresh()
    },
    methods: {
      refresh () {
        let params = {
          game_uuid: this.game_uuid
        }
        this.teamResource.list(params).then(response => {
          this.teams = [{ value: null, text: 'Please select a team' }]
          response.data.forEach(team => {
            this.teams.push({
              value: team.uuid,
              text: team.name
            })
          })
        })

        params = {
          game_uuid: this.game_uuid,
          question_uuid: this.question_uuid
        }
        this.hostResource.get_question(params).then(response => {
          let question = response.data
          this.name = question.name
          this.description = question.description
          this.category = question.category
        })

        this.hostResource.list_answers(params).then(response => {
          this.answers = []
          response.data.answers.forEach(answer => {
            this.answers.push({
              value: answer.uuid,
              text: answer.name,
              is_correct: answer.is_correct
            })
          })
        })
      },
      onSave () {
        let params = {
          game_uuid: this.game_uuid,
          question_uuid: this.question_uuid
        }
        let form = {
          team_uuid: this.team,
          answer_uuid: this.answer
        }
        this.hostResource.save_answer(params, form).then(response => {
          this.$router.push({
            name: 'HostView',
            params: {
              game_uuid: this.$route.params.game_uuid
            }
          })
        })
      }
    }
  }
</script>

<style>
  .correct {
    background-color: #7FFF00;
    padding: 3px;
  }
</style>
