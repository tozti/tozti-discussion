<template>
    <section :class="['editor', 'media', { floating: isFloating }]">
        <figure class="media-left">
            <p class="image is-64x64">
                <!-- TODO(liautaud): Add the actual avatar -->
                <img src="https://placeimg.com/128/128/people">
            </p>
        </figure>
        
        <div class="media-content">
            <div class="content">
                <p class="author">
                    <strong>{{ user.body.name }}</strong>
                </p>
                
                <textarea class="textarea" placeholder="Saisissez votre message" v-model="content"></textarea>
            </div>

            <div class="level">
                <div class="level-left toolbox">
                    <a href="#" class="button is-light"><i class="material-icons">format_bold</i></a>
                    <a href="#" class="button is-light"><i class="material-icons">format_italic</i></a>
                    <a href="#" class="button is-light"><i class="material-icons">format_underlined</i></a>
                    <a href="#" class="button is-light"><i class="material-icons">functions</i></a>
                    <a href="#" class="button is-light"><i class="material-icons">attach_file</i></a>
                    <a href="#" class="button is-light"><i class="material-icons">person</i></a>
                </div>

                <div class="level-right">
                    <button
                        type="submit"
                        class="button is-primary"
                        :disabled="attempting"
                        @click="attemptMessage">
                        <i class="material-icons">send</i>&nbsp; Envoyer
                    </button>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
    export default {
        props: ['thread', 'isFloating'],

        data() {
            return {
                content: '',
                attempting: false
            }
        },

        computed: {
            user() {
                return tozti.me
            }
        },

        methods: {
            attemptMessage() {
                this.attempting = true

                tozti.api
                    .post('/api/discussion/reply', {
                        thread_id: this.thread.id,
                        parent_id: null,
                        content: this.content,
                    })
                    .then(res => {
                        this.attempting = false
                        this.content = ''
                    })
                    .catch(res => {
                        this.$toast.open({
                            message: 'Une erreur est survenue lors de l\'écriture du message',
                            type: 'is-danger',
                            position: 'is-top'
                        })

                        this.attempting = false
                    })
            }
        }
    }
</script>
