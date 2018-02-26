<template>
    <section class="thread">
            <section class="thread-container">
                <section class="level main-title">
                    <h2 class="level-left">
                        <i class="material-icons">chat_bubble_outline</i> {{ resource.body.name }}
                    </h2>
                </section>

                <section class="thread boxed">
                    <thread-element v-for="message in messages" :key="message.id" :id="message.id"></thread-element>
                </section>

                <editor :is-floating.sync="isEditorFloating"></editor>
            </section>

            <aside class="thread-aside">
                <div class="inner">
                    <a class="button is-primary"><i class="material-icons">reply</i>&nbsp; Répondre</a>
                    <a class="button is-light"><i class="material-icons">notifications_none</i>&nbsp; Suivre</a>
                    <a class="button is-light"><i class="material-icons">star_outline</i>&nbsp; Importants</a>
                    <a class="button is-light"><i class="material-icons">attachment</i>&nbsp; Pièces jointes</a>
                    <a class="button is-light"><i class="material-icons">subdirectory_arrow_right</i>&nbsp; Dernier non-lu</a>

                    <scrubber :current="2" :total="10" :date="'Janvier 2018'"></scrubber>
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

        data: () => {
            isEditorFloating: false
        },

        computed: {
            messages() {
                return this.resource.body.messages.data
            }
        },
    }
</script>