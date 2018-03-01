'use strict'

import Thread from './components/Thread.vue'
import Timeago from 'vue-timeago'

// TODO(liautaud): We don't actually need to declare a route.
// Instead, we should use the dispatching system provided by
// the API, which allows our component to be rendered when
// any entity of type `thread` has to be displayed.
// Sadly, this system is not yet implemented. So we wait.
tozti.addRoutes([
    {
        path: '/discussion/:id',
        component: Thread,
        props: true
    }
])

// TODO(liautaud): Maybe we should refactor this into the core,
// as it will probably be useful to many extensions.
Vue.use(Timeago, {
    name: 'timeago',
    locale: 'fr-FR',
    locales: {
        'fr-FR': require('vue-timeago/locales/fr-FR.json')
    }
})
