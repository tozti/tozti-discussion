<template>
    <section class="thread" v-if="!loading">
            <section class="thread-container">
                <section class="level main-title">
                    <h2 class="level-left">
                        <i class="material-icons">chat_bubble_outline</i> {{ resource.body.name }}
                    </h2>
                </section>

                <section class="boxed messages-container" ref="messagesContainer">
                    <thread-element v-for="message in messages" 
                        :key="message.id"
                        :id="message.id"
                        :editor-state="editorState"></thread-element>
                </section>

                <div ref="editor">
                    <editor :thread="resource" :state="editorState"></editor>
                </div>

                <div v-if="editorState.floating" :style="{height: editorHeight}"></div>
            </section>

            <aside class="thread-aside">
                <div class="inner">
                    <a class="button is-primary"
                        @click.prevent="editorState.floating = true">
                        <i class="material-icons">reply</i>&nbsp; Répondre
                    </a>
                    <a class="button is-light"><i class="material-icons">notifications_none</i>&nbsp; Suivre</a>
                    <a class="button is-light"><i class="material-icons">star_outline</i>&nbsp; Importants</a>
                    <a class="button is-light"><i class="material-icons">attachment</i>&nbsp; Pièces jointes</a>
                    <a class="button is-light"><i class="material-icons">subdirectory_arrow_right</i>&nbsp; Dernier non-lu</a>

                    <scrubber
                        :messages-container="$refs.messagesContainer">
                    </scrubber>
                </div>
            </aside>
    </section>
</template>

<script>
    import { resourceMixin } from 'tozti'

    import ThreadElement from './ThreadElement.vue'
    import Editor from './Editor.vue'
    import Scrubber from './Scrubber.vue'

    export default {
        mixins: [ resourceMixin ],
        components: { ThreadElement, Editor, Scrubber },

        data: function() {
            return {
                // TODO(liautaud): We should probably use Vuex.
                editorState: {
                    floating: false,
                    parentMessage: null,
                    parentAuthor: null
                }
            }
        },

        computed: {
            messages() {
                return this.resource.body.messages.data
            },

            editorHeight() {
                return this.$refs.editor.clientHeight + 'px'
            }
        },
    }
</script>