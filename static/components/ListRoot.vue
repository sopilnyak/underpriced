<template>
    <div class="list-root">
        <list-header></list-header>
        <underpriced></underpriced>
    </div>
</template>

<script>
    import ListHeader from './ListHeader.vue'
    import Underpriced from './Underpriced.vue'

    export default {
        name: 'ListRoot',
        components: {
            ListHeader,
            Underpriced
        }
    }
</script>

<style>
    #main {
        font-family: 'Open Sans';
    }
</style>
