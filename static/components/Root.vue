<template>
    <div id="main">
        <g-header></g-header>
        <list-header></list-header>
        <router-view></router-view>
        <g-footer></g-footer>
    </div>
</template>

<script>
    import GHeader from './GHeader.vue'
    import GFooter from './GFooter.vue'
    import GLoading from './GLoading.vue'
    import ListHeader from './ListHeader.vue'

    export default {
        name: 'main',
        components: {
            GHeader,
            ListHeader,
            GFooter,
            GLoading
        }
    }
</script>

<style>
    body {
        margin: 0;
        color: #313334;
        font-family: "Open Sans";
        font-size: 14px;
        background-color: #FFFDE7;
        min-width: 1000px;
    }

    .number {
        display: inline;
        margin: 4px 4px;
    }

    .left-arrow {
        display: inline;
        margin: 4px 4px;
        text-decoration: underline;
    }

    .right-arrow {
        display: inline;
        margin: 4px 4px;
        text-decoration: underline;
    }

    .left-arrow.disabled {
        display: none;
    }
    .right-arrow.disabled {
        display: none;
    }

    .left-arrow:hover {
        cursor: pointer;
    }

    .right-arrow:hover {
        cursor: pointer;
    }

    .number:not(.active) {
        text-decoration: underline;
    }

    .number:hover:not(.active) {
        cursor: pointer;
    }

    ul {
        margin: 0;
        padding: 0;
    }
</style>
