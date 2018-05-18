import Vue from 'vue'
import Router from 'vue-router'

import store from '@/store'

import NotLoggedIn from '@/auth/not-logged-in'
import Contests from '@/contests/admin_list'
import Questions from '@/questions/admin_list'
import Answers from '@/answers/admin_list.vue'
import Games from '@/games/admin_list'
import HostView from '@/host/dashboard'
import HostQuestionView from '@/host/question'
import GameScreen from '@/game_screen/gameScreen'

Vue.use(Router)

function requireAuth (to, from, next) {
  if (!store.getters['auth/isAuthenticated']) {
    next({
      name: 'NotLoggedIn',
      query: { redirect: to.fullPath }
    })
  } else {
    next()
  }
}

function onlyNotLoggedIn (to, from, next) {
  if (store.getters['auth/isAuthenticated']) {
    next({
      name: 'Contests'
    })
  } else {
    next()
  }
}

export default new Router({
  routes: [
    {
      path: '/',
      name: 'NotLoggedIn',
      component: NotLoggedIn,
      beforeEnter: onlyNotLoggedIn
    },
    {
      path: '/contests/',
      name: 'Contests',
      component: Contests,
      beforeEnter: requireAuth
    },
    {
      path: '/contests/:contest_id/questions/',
      name: 'Questions',
      component: Questions,
      beforeEnter: requireAuth
    },
    {
      path: '/contests/:contest_id/questions/:question_id',
      name: 'Answers',
      component: Answers,
      beforeEnter: requireAuth
    },
    {
      path: '/games/',
      name: 'Games',
      component: Games,
      beforeEnter: requireAuth
    },
    {
      path: '/games/:game_id',
      name: 'HostView',
      component: HostView,
      beforeEnter: requireAuth
    },
    {
      path: '/games/:game_id/question/:question_id',
      name: 'HostQuestionView',
      component: HostQuestionView,
      beforeEnter: requireAuth
    },
    {
      path: '/games/:game_id/screen/:screen_id',
      name: 'GameScreen',
      component: GameScreen
    }
  ]
})
