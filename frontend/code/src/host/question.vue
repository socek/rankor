<template>
  <span>
    <h1>Question</h1>
    <h2>Name</h2>
    <p>{{ name }}</p>

    <h2>Category</h2>
    <p>{{ category }}</p>

    <h2>Description</h2>
    <p>{{ description }}</p>

    <ul class="screens">
      <li v-for="(screen, index) in screens">
        Screen {{ index + 1 }}
        <b-btn
          @click="onSendToScreen(screen)"
          :variant="getScreenVariant(screen)"
          size="small"
          :disabled="form.fields.team_id === null">
          Send to screen
        </b-btn>
      </li>
    </ul>

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
                        @change="onSelectTeam"
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
            <input :id="'answer_' + index" type="radio" :value="answer.value" v-model="form.fields.answer_id" @change="onSelectAnswer">
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
  import screenResource from '@/screen/resource'

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
        screens: [],

        game_id: this.$route.params.game_id,
        question_id: this.$route.params.question_id,
        currentScreens: [],

        hostResource: hostResource(this),
        screenResource: screenResource(this)
      }
    },
    created () {
      this.refresh()
    },
    methods: {
      getScreenVariant (screen) {
        return (this.currentScreens.indexOf(screen) >= 0) ? 'danger' : 'primary'
      },
      onSelectTeam (event) {
        this.form.fields.team_id = event
        return this.doCommand({
          'name': 'attach_team',
          'data': {
            'team_id': event
          }
        })
      },
      onSelectAnswer (event) {
        return this.doCommand({
          'name': 'select_answer',
          'data': {
            'answer_id': event.target.value
          }
        })
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
          // this.sendUpdate()

          this.screenResource.listScreens(params).then(response => {
            this.screens = response.data
          })
        })
      },
      saveCall () {
        return this.hostResource.save_answer(this.params(), this.form.fields)
      },
      makeParams (screen) {
        return {
          game_id: this.game_id,
          screen_id: screen.id
        }
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
      },
      onSendToScreen (screen) {
        this.currentScreens.push(screen)
        return this.doCommand({
          'name': 'show_question',
          'data': {
            'view': 'question',
            'question_id': this.question_id,
            'team_id': this.form.fields.team_id
          },
          screen
        })
      },
      doCommand (data, screen) {
        let screens = screen ? [screen] : this.currentScreens
        screens.forEach(screen => {
          const params = this.makeParams(screen)
          return this.screenResource.doCommand(params, data)
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
