'use strict'

import Thread from './components/Thread.vue'

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

// Custom resource types.
import TaxonomyItem from './components/TaxonomyItem.vue'
import NewThreadForm from './components/Forms/NewThreadForm.vue'
tozti.addResourceType(
    'discussion/thread',
    'discussion', 'f', 
    TaxonomyItem,
    NewThreadForm
)
