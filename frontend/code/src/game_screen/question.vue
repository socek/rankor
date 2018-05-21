<template>
  <span>
    <h1>Pytanie:</h1>
    <h2>Drużyna: {{ getTeamName() }}</h2>
    <h3>Kategoria: {{ getCategory() }}</h3>
    <p>{{ getDescription() }}</p>
    <ul>
      <li v-for="(answer, index) in answers" >
        {{ index + 1 }}: <span :class='getAnswerClass(answer)'>{{ answer.text }}</span>
      </li>
    </ul>
  </span>
</template>

<script>
  import hostResource from '@/host/resource'

  export default {
    data () {
      return {
        answers: [],
        hostResource: hostResource(this)
      }
    },
    created () {
      this.onNewQuestion(this.question)
    },
    computed: {
      question () {
        let question = this.$store.state.screen.question
        this.onNewQuestion(question)
        return question
      },
      team () {
        return this.$store.state.screen.team
      },
      answer () {
        return this.$store.state.screen.answer
      },
      isCorrect () {
        return this.$store.state.screen.isCorrect
      }
    },
    methods: {
      getTeamName () {
        return this.team ? this.team.name : null
      },
      getCategory () {
        return this.question ? this.question.category : null
      },
      getDescription () {
        return this.question ? this.question.description : null
      },
      getAnswerClass (answer) {
        let answerId = answer.value
        let selectedId = this.answer ? this.answer.id : null
        let isCorrect = this.isCorrect
        let data = {
          answer: true,
          selected: answerId === selectedId,
          success: answerId === selectedId && isCorrect === true,
          fail: answerId === selectedId && isCorrect === false
        }
        // console.log(answer.text, data.selected, answerId, selectedId)
        return data
      },
      onNewQuestion (question) {
        this.answers = []
        if (question) {
          let params = {
            game_id: this.$route.params.game_id,
            question_id: question.id
          }

          this.hostResource.get_question(params).then(response => {
            this.answers = []
            response.data.answers.forEach(answer => {
              this.answers.push({
                value: answer.id,
                text: answer.name
              })
            })
          })
        }
      }
    }
  }
</script>

<style>
  .selected {
    background-color: yellow;
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
