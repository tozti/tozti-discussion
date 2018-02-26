<template>
    <nav class="scrubber">
        <p><i class="material-icons">arrow_upward</i> Premier message</p>
        
        <div class="area">
            <div class="current">
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
        props: ['current', 'total', 'date']
    }
</script>