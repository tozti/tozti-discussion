<template>
    <nav class="scrubber" v-if="messagesContainer">
        <p><i class="material-icons">arrow_upward</i> Premier message</p>
        
        <div class="area">
            <div class="current" :style="{top: this.cursorTop + 'px'}">
                <strong>{{ current }} sur {{ total }} messages</strong>
                <time>
                    <timeago :since="date"></timeago>
                </time>
            </div>
        </div>
        
        <p><i class="material-icons">arrow_downward</i> Maintenant</p>
    </nav>
</template>

<script>
    export default {
        props: ['messagesContainer'],

        data() {
            return {
                viewportTop: window.pageYOffset,
                viewportHeight: window.innerHeight
            }
        },

        methods: {
            onScroll() {
                this.viewportTop = window.pageYOffset
            }
        },

        computed: {
            total() {
                return this.messagesContainer.childElementCount
            },

            containerPosition() {
                let containerBox = this.messagesContainer.getBoundingClientRect()
                let containerTop = containerBox.top + this.viewportTop
                let containerHeight = this.messagesContainer.offsetHeight

                let realTop = this.viewportTop - containerTop
                let realBottom = realTop + this.viewportHeight
                let realHeight = containerHeight - this.viewportHeight

                return {realTop, realBottom, realHeight}
            },

            normalizedTop() {
                let {realTop, realHeight} = this.containerPosition

                return Math.max(Math.min(realTop / realHeight, 1), 0)
            },

            cursorTop() {
                return this.normalizedTop * (190 - 42)
            },

            current() {
                let {realBottom, realHeight} = this.containerPosition

                // Find the first message to appear in the viewport.
                let lastVisible = 0

                this.messagesContainer.childNodes.forEach(message => {
                    let bottom = message.offsetTop + message.offsetHeight
                    if (bottom >= realBottom) return
                    lastVisible++
                })

                return (lastVisible >= 1) ? lastVisible : 1
            },

            date() {
                let children = this.messagesContainer.childNodes
                let message = children[this.current - 1]
                let time = message.getElementsByTagName('time')[0]

                return time.getAttribute('datetime')
            }
        },
        
        beforeMount () {
            window.addEventListener('scroll', this.onScroll)
        },

        beforeDestroy () {
            window.removeEventListener('scroll', this.onScroll)
        }
    }
</script>