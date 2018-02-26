<template>
    <message
        v-if="!parentMessage"
        :message="message"
        :author="author">
    </message>

    <event
        v-else
        :message="message"
        :author="author"
        :parent-message="parentMessage"
        :parent-author="parentAuthor">
    </event>
</template>

<script>
    import Message from './Message.vue'
    import Event from './Event.vue'

    // TODO(liautaud): Ideally, we would use the resourceMixin in combination
    // with the `include` property from the API to fetch both the message and
    // its author. However, since `include` is not yet available, we have to
    // copy/paste the code of the mixin, and load the author manually.
    function fetch() {
        tozti.store.get(this.id)
            .then(message => {
                this.message = message
                return tozti.store.rels.fetch(this.message.body.author)
            })
            .then(author => {
                this.author = author

                if (!this.message.body.parent) {
                    this.loading = false
                } else {
                    tozti.store.rels.fetch(this.message.body.parent)
                        .then(parentMessage => {
                            this.parentMessage = parent
                            return tozti.store.rels.fetch(this.parentMessage.body.author)
                        })
                        .then(parentAuthor => {
                            this.parentAuthor = parentAuthor
                            this.loading = false
                        })
                }
            })
    }

    export default {
        props: { id: String },
        components: { Message, Event },

        watch: {
            id() {
                fetch.call(this)
            }
        },

        mounted() {
            fetch.call(this)
        },

        data() {
            return {
                loading: true,
                message: null,
                author: null,
                parentMessage: null,
                parentAuthor: null,
            }
        }
    }
</script>