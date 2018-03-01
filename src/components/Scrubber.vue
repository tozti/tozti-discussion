<template>
    <nav class="scrubber">
        <p><i class="material-icons">arrow_upward</i> Premier message</p>

        <div class="area" ref="area">
            <transition name="fade">
                <div class="current" ref="current"
                    v-if="messagesContainer"
                    :style="{top: this.cursorTop + 'px'}"
                    @mousedown="onMousedown">
                    <strong>{{ current }} sur {{ total }} messages</strong>
                    <time>
                        <timeago :since="date"></timeago>
                    </time>
                </div>
            </transition>
        </div>
        
        <p><i class="material-icons">arrow_downward</i> Maintenant</p>
    </nav>
</template>

<script>
    const AREA_HEIGHT = 190
    const CURRENT_HEIGHT = 42

    export default {
        props: ['messagesContainer'],

        data() {
            return {
                dragEnabled: false,
                dragOffset: 0,
                viewportTop: window.pageYOffset,
                viewportHeight: window.innerHeight
            }
        },

        methods: {
            onScroll() {
                this.viewportTop = window.pageYOffset
            },

            onMousedown(e) {
                this.dragEnabled = true

                let currentBox = this.$refs.current.getBoundingClientRect()
                this.dragOffset = e.clientY - currentBox.top
            },

            onMouseup() {
                this.dragEnabled = false
                this.dragOffset = 0
            },

            onMousemove(e) {
                if (!this.dragEnabled) return

                let areaBox = this.$refs.area.getBoundingClientRect()
                let areaTop = e.clientY - areaBox.top - this.dragOffset
                let areaHeight = AREA_HEIGHT - CURRENT_HEIGHT

                let {containerTop, realHeight} = this.containerPosition
                let desiredTop = areaTop / areaHeight * realHeight

                window.scrollTo(0, desiredTop + containerTop)
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

                return {
                    containerTop,
                    containerHeight,
                    realTop,
                    realBottom,
                    realHeight
                }
            },

            normalizedTop() {
                let {realTop, realHeight} = this.containerPosition

                return Math.max(Math.min(realTop / realHeight, 1), 0)
            },

            cursorTop() {
                return this.normalizedTop * (AREA_HEIGHT - CURRENT_HEIGHT)
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
            window.addEventListener('mouseup', this.onMouseup)
            window.addEventListener('mousemove', this.onMousemove)
        },

        beforeDestroy () {
            window.removeEventListener('scroll', this.onScroll)
            window.removeEventListener('mouseup', this.onMouseup)
            window.removeEventListener('mousemove', this.onMousemove)
        }
    }
</script>