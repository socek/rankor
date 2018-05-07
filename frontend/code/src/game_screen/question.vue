<template>
  <span>
    <h1>Pytanie:</h1>
    <h2>{{ team }}</h2>
    <h3>{{ category }}</h3>
    <p>{{ description }}</p>

    <ul>
      <li v-for="(answer, index) in answers">
          {{ index }}: {{ answer.text }}
        </label>
      </li>
    </ul>
  </span>
</template>

<script>
  import hostResource from '@/host/resource'

  export default {
    props: ['question_uuid'],
    data () {
      return {
        team: null,
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
        this.team = null
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
      }
    },
    watch: {
      question_uuid (val) {
        this.fillQuestion()
      }
    }
  }
</script>
