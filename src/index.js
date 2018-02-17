import Discussion from './components/Discussion.vue';


// add a new route with highest priority
tozti.routes.unshift(
  { path: '/discussion', component: Discussion }
)
tozti.addMenuItem("Discussion", "/discussion")
