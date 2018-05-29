<template>
  <div class="row justify-content-md-center">
    <div class="col-lg-12">
      <h1>Questions <createDialog @onSuccess="refresh"></createDialog></h1>

      <div v-for="(questions, category) in categories">
        <table class="table table-striped table-sm">
          <tr class="title table-success">
            <th scope="col" colspan="4"><strong>{{ category }}</strong></th>
          </tr>
          <tr class="table-secondary">
            <th scope="col">#</th>
            <th scope="col">Name</th>
            <th scope="col">Description</th>
            <th scope="col">Actions</th>
          </tr>
          <tbody>
            <tr v-for="(question, index) in questions">
              <td scope="row">{{index + 1}}</td>
              <td>{{question.name}}</td>
              <td>{{question.description}}</td>
              <td>
                <router-link :to="{name: 'Answers', params: {contest_id: contest_id, question_id: question.id}}">
                  <icon name="list-ol"></icon>
                </router-link>
                <editDialog :question_id="question.id" @onSuccess="refresh"></editDialog>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
  import createDialog from '@/questions/dialogs/create'
  import editDialog from '@/questions/dialogs/edit'
  import questionResource from '@/questions/resource'

  export default {
    data () {
      return {
        categories: {},
        resource: questionResource(this),
        contest_id: this.$route.params.contest_id
      }
    },
    created () {
      this.$store.dispatch('breadcrumb/Questions', this)
      this.refresh()
    },
    methods: {
      refresh () {
        this.resource.get().then((response) => {
          this.categories = response.data.categories
        })
      }
    },
    components: {
      createDialog,
      editDialog
    }
  }
</script>
