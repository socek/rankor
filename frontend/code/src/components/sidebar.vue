<template>
  <div class="col-sm-3 col-md-2 sidebar">
    <ul class="nav nav-sidebar" v-for="group in menu">
      {{ group.name }}
      <li v-for="element in group.elements" v-bind:class="{ active: element.isActive }">
        <a v-bind:href="element.url">{{ element.text }}</a>
      </li>
    </ul>
  </div>
</template>

<script>
import AjaxView from '../models/ajax'

export default {
  data () {
    return {
      menu: []
    }
  },
  created: function () {
    var self = this
    new AjaxView(function (response) {
      self.menu = response.data.menu
    }).run('/api/menu')
  }
}
</script>
