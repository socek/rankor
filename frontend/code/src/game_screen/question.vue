<template>
  <span>
    <h1>Pytanie:</h1>
    <h2>Drużyna: {{ team }}</h2>
    <h3>Kategoria: {{ category }}</h3>
    <p>{{ description }}</p>
    <ul>
      <li v-for="(answer, index) in answers" >
        {{ index + 1 }}: <span :class='{selected: answer.value === answer_id, answer: true, success: answer.value === answer_id && is_correct === true, fail: answer.value === answer_id && is_correct === false}'>{{ answer.text }}</span>
      </li>
    </ul>
  </span>
</template>

<script>
  import hostResource from '@/host/resource'

  export default {
    props: ['question_id', 'timestamp', 'team_name', 'answer_id', 'is_correct'],
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
          game_id: this.$route.params.game_id,
          question_id: this.question_id
        }

        this.hostResource.get_question(params).then(response => {
          const question = response.data.question
          this.name = question.name
          this.description = question.description
          this.category = question.category

          this.answers = []
          response.data.answers.forEach(answer => {
            this.answers.push({
              value: answer.id,
              text: answer.name
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
