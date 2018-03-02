'use strict'

import Thread from './components/Thread.vue'

// Custom resource types.
import TaxonomyItem from './components/TaxonomyItem.vue'
import NewThreadForm from './components/Forms/NewThreadForm.vue'
tozti.addResourceType(
    'discussion/thread',
    'message-plus', 'discussion', 'f',
    TaxonomyItem,
    Thread,
    NewThreadForm
)
