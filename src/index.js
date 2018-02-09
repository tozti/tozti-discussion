import App from './components/App.vue';


// add a new route with highest priority
tozti.routes.unshift(
  { path: '/discussion', component: App }
)
tozti.addMenuItem("Discussion", "/discussion")
