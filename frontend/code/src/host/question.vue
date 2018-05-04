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
          <label :for="'answer_' + index"">
            {{ answerObject.text }}
          </label>
        </li>
      </ul>
    </div>

    <b-btn variant="primary">
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
        teams: [
          { value: null, text: 'Please select a team' },
          { value: 'a', text: 'First Team' },
          { value: 'b', text: 'Second Team' }
        ],
        answers: [
          { text: 'Toggle this custom radio', value: 'first' },
          { text: 'Or toggle this other custom radio', value: 'second' }
        ],

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

        // get question with answers

        // let params = {
        //   game_uuid: this.game_uuid
        // }
        // this.resource.list(params).then((response) => {
        //   this.questions = response.data
        // })
      }
    }
  }
</script>
