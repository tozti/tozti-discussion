<template>
    <article class="media event" v-if="!loading">
        <i class="material-icons">reply</i>
        <p>
        	<strong>{{ author.body.name }}</strong>
        	a répondu à <a href="#">un message</a> de
        	<strong>{{ parentAuthor.body.name }}</strong> il y a 
        	<small><timeago :since="message.meta.created"></timeago></small>.
        </p>
    </article>
</template>

<script>
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

                tozti.store.rels.fetch(this.message.body.parent)
                    .then(parentMessage => {
                        this.parentMessage = parentMessage
                        return tozti.store.rels.fetch(this.parentMessage.body.author)
                    })
                    .then(parentAuthor => {
                        this.parentAuthor = parentAuthor
                        this.loading = false
                    })
            })
    }

	export default {
		props: ['id', 'editorState'],

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