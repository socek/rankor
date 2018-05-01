import Vue from 'vue'
import Router from 'vue-router'

import store from '@/store'

import NotLoggedIn from '@/auth/not-logged-in'
import Contests from '@/contests/admin_list'
import Questions from '@/questions/admin_list'

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
      path: '/contests/:contest_uuid/questions/',
      name: 'Questions',
      component: Questions,
      beforeEnter: requireAuth
    }
  ]
})
