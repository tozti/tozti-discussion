<template>
    <div v-if="loading"></div>
    
    <message
        v-else-if="!resource.body.parent.data"
        :id="resource.id"
        :editor-state="editorState">
    </message>

    <event
        v-else
        :id="resource.id"
        :editor-state="editorState">
    </event>
</template>

<script>
    import { resourceMixin } from 'tozti'

    import Message from './Message.vue'
    import Event from './Event.vue'

    export default {
        props: { id: String, editorState: Object },
        mixins: [ resourceMixin ],
        components: { Message, Event }
    }
</script>