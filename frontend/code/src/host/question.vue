<template>
  <span>
    <h1>Question</h1>
    <h2>Name</h2>
    <p>{{ name }}</p>

    <h2>Category</h2>
    <p>{{ category }}</p>

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
                        v-model="form.fields.team_id"
                        :options="teams"
                        :state="form.errors.team_id.length == 0 ? null : false"
                        class="mb-3" />
        </b-form-input>
        <b-form-invalid-feedback v-for="error in form.errors.team_id" :key="error">
          {{ error }}
        </b-form-invalid-feedback>
      </b-form-group>

      <b-form-group
                    label="Answers:"
                    label-for="answerField">
        <b-form-invalid-feedback v-for="error in form.errors.answer_id" :key="error" :force-show="true">
          {{ error }}
        </b-form-invalid-feedback>

        <ul>
          <li v-for="(answer, index) in answers">
            <input :id="'answer_' + index" type="radio" :value="answer.value" v-model="form.fields.answer_id" @change="sendUpdate">
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
  import hostResource from '@/host/resource'
  import baseForm from '@/forms'

  export default {
    extends: baseForm,
    data () {
      return {
        name: '',
        category: '',
        description: '',
        form: this.prepareForm({
          team_id: null,
          answer_id: null
        }),
        teams: [],
        answers: [],

        game_id: this.$route.params.game_id,
        question_id: this.$route.params.question_id,

        hostResource: hostResource(this)
      }
    },
    created () {
      this.refresh()
    },
    methods: {
      sendUpdate () {
        let params = {
          question_id: this.$route.params.question_id,
          game_id: this.$route.params.game_id,
          view: 'question',
          team_name: this.getTeamName(),
          answer_id: this.form.fields.answer_id
        }
        this.hostResource.change_view(params, params)
      },
      onChangeTeam (event) {
        this.form.fields.team_id = event
        this.sendUpdate()
      },
      getTeamName () {
        for (let loop = 0; loop < this.teams.length; loop++) {
          let name = this.teams[loop].text
          let id = this.teams[loop].value
          if (id && id === this.form.fields.team_id) {
            return name
          }
        }
      },
      params () {
        return {
          game_id: this.game_id,
          question_id: this.question_id
        }
      },
      refresh () {
        this.refreshForm()

        let params = {
          game_id: this.game_id,
          question_id: this.question_id
        }

        this.hostResource.get_question(params).then(response => {
          const question = response.data.question
          this.name = question.name
          this.category = question.category
          this.description = question.description
          this.category = question.category

          this.teams = [{ value: null, text: 'Please select a team' }]
          response.data.teams.forEach(team => {
            this.teams.push({
              value: team.id,
              text: team.name
            })
          })

          this.answers = []
          response.data.answers.forEach(answer => {
            this.answers.push({
              value: answer.id,
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
              game_id: this.$route.params.game_id
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
