<template>
    <!-- TODO(liautaud): Implement the "important" class. -->
    <article class="media">
        <figure class="media-left">
            <p class="image is-64x64">
                <!-- TODO(liautaud): Add the actual avatar -->
                <img src="https://placeimg.com/128/128/people">
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
                        <a href="#" v-if="replies.length > 0">
                            <!-- TODO(liautaud): Toggle between "Afficher" and "Masquer" -->
                            <i class="material-icons">reply</i> Masquer les {{ replies.length }} réponses
                        </a>
                    </div>
                    <div class="level-right actions">
                        <a v-if="!isReply"
                            class="button is-white is-small" href="#">Répondre</a>
                        <a v-if="author.id == user.id" @click.prevent="deleteMessage()"
                            class="button is-white is-small" href="#">Supprimer</a>
                        <a class="button is-white is-small" href="#">Citer le message</a>
                        <a class="button is-white is-small" href="#">Démarrer un fil</a>
                        <a class="button is-white is-small" href="#">Marquer comme important</a>
                    </div>
                </div>
            </div>

            <div class="replies" v-if="replies.length > 0">
                <message 
                    v-for="reply in replies"
                    :key="reply.id"
                    :id="reply.id"
                </message>
            </div>
        </div>
    </article>
</template>

<script>
    export default {
        name: 'message',
        props: ['message', 'author'],

        computed: {
            parsed() {
                // TODO(liautaud): Add a Markdown parser or something similar.
                return '<p>' + this.message.body.content + '</p>'
            },

            isReply() {
                return !!this.message.body.parent
            },

            replies() {
                return this.message.body.replies.data
            },

            user() {
                return tozti.me
            }
        },

        methods: {
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