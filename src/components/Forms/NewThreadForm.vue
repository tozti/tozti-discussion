<template>
    <t-new-resource-form
        title="Nouvelle discussion"
        :resource="thread"
        :callback="attemptNewThread"
        :parent="$parent"
        :root="root">
    </t-new-resource-form>
</template>

<script>
    export default {
        props: {
            root: {
                type: Object,
                default: null,
                validate(root) {
                    return root && [
                        'core/group',
                        'core/folder',
                    ].indexOf(root.type) > -1
                }
            }
        },

        data() {
            return {
                thread: {
                    name: '',
                    handle: '',
                    messages: { data: [] },
                    important: { data: [] },
                },
            }
        },

        methods: {
            attemptNewThread(handler) {
                let prom = tozti
                    // Create the thread.
                    .store.create({
                        type: 'discussion/thread',
                        body: this.thread
                    }, false)

                    // Link the thead to the root folder.
                    .then(({ id, type }) => {
                        let linkage = { id, type }
                        if (this.root)
                            return tozti.store
                                .rels.add(this.root.body.children, {
                                    [this.thread.handle]: linkage
                                })

                        else {
                            return tozti.api
                                .post(tozti.api.handleURL(this.thread.handle), {
                                    data: linkage
                                })
                        }
                    })

                handler(prom)
            }
        }
    }
</script>
