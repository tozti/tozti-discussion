<template>
    <!-- TODO(liautaud): Implement the "important" class. -->
    <article class="media" v-if="!loading">
        <figure class="media-left">
            <p class="image is-64x64">
                <!-- TODO(liautaud): Add the actual avatar -->
                <img :src="'https://identicon-api.herokuapp.com/' + author.body.name + '/64?format=png'">
            </p>
        </figure>
        <div class="media-content">
            <div class="content">
                <p class="author">
                    <strong>{{ author.body.name }}</strong>
                    <small>
                        <timeago :since="message.meta.created"></timeago>
                    </small>
                </p>
                
                <div v-html="parsed"></div>

                <div class="level">
                    <div class="level-left status">
                        <template v-if="replies.length > 0">
                            <a href="#"
                                @click.prevent="repliesHidden = false"
                                v-if="repliesHidden">
                                <i class="material-icons">reply</i> Afficher les {{ replies.length }} réponses
                            </a>
                            <a href="#"
                                @click.prevent="repliesHidden = true"
                                v-else>
                                <i class="material-icons">reply</i> Masquer les {{ replies.length }} réponses
                            </a>
                        </template>
                    </div>
                    <div class="level-right actions">
                        <a v-if="!isReply"
                            @click.prevent="answerMessage"
                            class="button is-white is-small" href="#">Répondre</a>
                        <a v-if="author.id == user.id"
                            @click.prevent="deleteMessage"
                            class="button is-white is-small" href="#">Supprimer</a>
                        <a class="button is-white is-small" href="#">Citer le message</a>
                        <a class="button is-white is-small" href="#">Démarrer un fil</a>
                        <a class="button is-white is-small" href="#">Marquer comme important</a>
                    </div>
                </div>
            </div>

            <div class="replies" v-if="replies.length > 0 && !repliesHidden">
                <message 
                    v-for="reply in replies"
                    :key="reply.id"
                    :id="reply.id">
                </message>
            </div>
        </div>
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
                this.loading = false
            })
    }

    export default {
        name: 'message',
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
                repliesHidden: true
            }
        },

        computed: {
            parsed() {
                // TODO(liautaud): Add a Markdown parser or something similar.
                return '<p>' + this.message.body.content + '</p>'
            },

            isReply() {
                return !!this.message.body.parent.data
            },

            replies() {
                return this.message.body.replies.data
            },

            user() {
                return tozti.me
            }
        },

        methods: {
            answerMessage() {
                // TODO(liautaud): We should probably use Vuex.
                this.editorState.floating = true
                this.editorState.parentMessage = this.message
                this.editorState.parentAuthor = this.author
            },

            deleteMessage() {
                tozti.api
                    .post('/api/discussion/deleteMessage', {
                        message_id: this.message.id
                    })
                    .catch(res => {
                        this.$toast.open({
                            message: 'Une erreur est survenue lors de la suppression du message',
                            type: 'is-danger',
                            position: 'is-top'
                        })
                    })
            }
        }
    }
</script>