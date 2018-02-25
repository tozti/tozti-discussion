import Discussion from './components/Discussion.vue';


// add a new route with highest priority

tozti.addMenuItem("Discussion", "/discussion")
tozti.addRoutes([
  { path: '/discussion', component: Discussion }
])
