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
    props: ['question', 'team', 'answer'],
    data () {
      return {
        answers: [],
        hostResource: hostResource(this)
      }
    },
    created () {
      this.refresh()
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
        let answerId = answer.id
        let selectedId = this.answer ? this.answer.id : null
        let isCorrect = this.answer ? this.answers.is_correct : false
        return {
          answer: true,
          selected: answerId === selectedId,
          success: answerId === selectedId && isCorrect,
          fail: answerId === selectedId && !isCorrect
        }
      },
      refresh () {
        this.answers = []
        if (this.question) {
          let params = {
            game_id: this.$route.params.game_id,
            question_id: this.question.id
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
