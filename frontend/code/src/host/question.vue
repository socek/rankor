<template>
  <span>
    <h1>Question</h1>
    <h2>Name</h2>
    <p>{{ name }}</p>

    <h2>Description</h2>
    <p>{{ description }}</p>

    <form @submit.prevent="onSave">
      <b-form-invalid-feedback  v-for="error in form.errors._schema"
                                :key="error"
                                :force-show="true" >
        {{ error }}
      </b-form-invalid-feedback>

      <b-form-group
                    label="Team:"
                    label-for="teamField">
        <b-form-select  id="teamField"
                        @change="onChangeTeam"
                        v-model="form.fields.team_uuid"
                        :options="teams"
                        :state="form.errors.team_uuid.length == 0 ? null : false"
                        class="mb-3" />
        </b-form-input>
        <b-form-invalid-feedback v-for="error in form.errors.team_uuid" :key="error">
          {{ error }}
        </b-form-invalid-feedback>
      </b-form-group>

      <b-form-group
                    label="Answers:"
                    label-for="answerField">
        <b-form-invalid-feedback v-for="error in form.errors.answer_uuid" :key="error" :force-show="true">
          {{ error }}
        </b-form-invalid-feedback>

        <ul>
          <li v-for="(answer, index) in answers">
            <input :id="'answer_' + index" type="radio" :value="answer.value" v-model="form.fields.answer_uuid" @change="sendUpdate">
            <label :for="'answer_' + index" :class="{correct: answer.is_correct}">
              {{ answer.text }}
            </label>
          </li>
        </ul>
      </b-form-group>

      <input type="submit" value="Verify" class="btn btn-primary">
    </form>

  </span>
</template>

<script>
  import teamResource from '@/team/resource'
  import hostResource from '@/host/resource'
  import baseForm from '@/forms'

  export default {
    extends: baseForm,
    data () {
      return {
        name: '',
        description: '',
        form: this.prepareForm({
          team_uuid: null,
          answer_uuid: null
        }),
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
      sendUpdate () {
        let params = {
          question_uuid: this.$route.params.question_uuid,
          game_uuid: this.$route.params.game_uuid,
          view: 'question',
          team_name: this.getTeamName(),
          answer_uuid: this.form.fields.answer_uuid
        }
        this.hostResource.change_view(params, params)
      },
      onChangeTeam (event) {
        this.form.fields.team_uuid = event
        this.sendUpdate()
      },
      getTeamName () {
        for (let loop = 0; loop < this.teams.length; loop++) {
          let name = this.teams[loop].text
          let uuid = this.teams[loop].value
          if (uuid && uuid === this.form.fields.team_uuid) {
            return name
          }
        }
      },
      params () {
        return {
          game_uuid: this.game_uuid,
          question_uuid: this.question_uuid
        }
      },
      refresh () {
        this.refreshForm()

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

        this.hostResource.get_question(this.params()).then(response => {
          let question = response.data
          this.name = question.name
          this.description = question.description
          this.category = question.category
        })

        this.hostResource.list_answers(this.params()).then(response => {
          this.answers = []
          response.data.answers.forEach(answer => {
            this.answers.push({
              value: answer.uuid,
              text: answer.name,
              is_correct: answer.is_correct
            })
          })
          this.form.fields = response.data.answer
          this.sendUpdate()
        })
      },
      saveCall () {
        return this.hostResource.save_answer(this.params(), this.form.fields)
      },
      onSave () {
        this.saveCall().then((response) => {
          this.$router.push({
            name: 'HostView',
            params: {
              game_uuid: this.$route.params.game_uuid
            }
          })
        }).catch(this.onError)
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
