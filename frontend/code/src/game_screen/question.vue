<template>
  <span>
    <h1>Pytanie:</h1>
    <h2>Drużyna: {{ team }}</h2>
    <h3>Kategoria: {{ category }}</h3>
    <p>{{ description }}</p>
    <ul>
      <li v-for="(answer, index) in answers" >
        {{ index + 1 }}: <span :class='{selected: answer.value === answer_uuid, answer: true, success: answer.value === answer_uuid && is_correct === true, fail: answer.value === answer_uuid && is_correct === false}'>{{ answer.text }}</span>
      </li>
    </ul>
  </span>
</template>

<script>
  import hostResource from '@/host/resource'

  export default {
    props: ['question_uuid', 'timestamp', 'team_name', 'answer_uuid', 'is_correct'],
    data () {
      return {
        team: this.team_name,
        description: null,
        category: null,
        answers: [],
        hostResource: hostResource(this)
      }
    },
    created () {
      this.fillQuestion()
    },
    methods: {
      refresh () {
        this.team = this.team_name
        this.description = null
        this.answers = []
      },
      fillQuestion () {
        this.refresh()
        let params = {
          game_uuid: this.$route.params.game_uuid,
          question_uuid: this.question_uuid
        }
        this.hostResource.get_question(params).then(response => {
          let question = response.data
          this.description = question.description
          this.category = question.category
        })

        this.hostResource.list_answers(params).then(response => {
          this.answers = []
          response.data.answers.forEach(answer => {
            this.answers.push({
              text: answer.name,
              value: answer.uuid
            })
          })
        })
      }
    },
    watch: {
      timestamp (val) {
        this.fillQuestion()
      }
    }
  }
</script>

<style>
  .selected {
    background-color: yellow;
    /*color: white;*/
  }
  .answer {
    padding: 5px;
  }
  .success {
    background-color: green;
    color: white;
  }
  .fail {
    background-color: red;
    color: white;
  }
</style>
