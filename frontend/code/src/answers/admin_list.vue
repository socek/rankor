<template>
  <div class="row justify-content-md-center">
    <div class="col-lg-12">
      <h1>Answers <createDialog @onSuccess="refresh"></createDialog></h1>
      <table class="table table-striped">
        <thead class="thead-dark">
          <tr>
            <th scope="col">#</th>
            <th scope="col">Name</th>
            <th scope="col">State</th>
            <th scope="col">Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(answer, index) in answers">
            <td scope="row">{{index + 1}}</td>
            <td>{{answer.name}}</td>
            <td>
              <icon name="check" style="color: green;" v-if="answer.is_correct"></icon>
              <icon name="times" style="color: red;" v-else></icon>
            </td>
            <td>
              <editDialog :answer_id="answer.id" @onSuccess="refresh"></editDialog>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
  import answerResource from '@/answers/resource'
  import createDialog from '@/answers/dialogs/create'
  import editDialog from '@/answers/dialogs/edit'

  export default {
    data () {
      return {
        answers: [],
        resource: answerResource(this),
        contest_id: this.$route.params.contest_id,
        question_id: this.$route.params.question_id
      }
    },
    created: function () {
      this.$store.dispatch('breadcrumb/Answers', this)
      this.refresh()
    },
    methods: {
      refresh () {
        this.resource.get().then((response) => {
          this.answers = response.data.answers
        })
      }
    },
    components: {
      createDialog,
      editDialog
    }
  }
</script>
