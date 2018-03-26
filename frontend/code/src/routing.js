import Vue from 'vue'
import Router from 'vue-router'

import NotLoggedIn from '@/auth/not-logged-in'
import Dashboard from '@/contests/dashboard'
import User from '@/models/user'

Vue.use(Router)

function requireAuth (to, from, next) {
  if (!User.isAuthenticated()) {
    next({
      name: 'NotLoggedIn',
      query: { redirect: to.fullPath }
    })
  } else {
    next()
  }
}

function onlyNotLoggedIn (to, from, next) {
  if (User.isAuthenticated()) {
    next({
      name: 'Dashboard'
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
      path: '/dashboard',
      name: 'Dashboard',
      component: Dashboard,
      beforeEnter: requireAuth
    }
  ]
})
