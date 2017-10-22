<template>
    <div class="loading">
        <span class="loading-1"></span>
        <span class="loading-2"></span>
        <span class="loading-3"></span>
        <br>
        Loading, please wait
    </div>
</template>

<script>
    export default {
        name: 'GLoading'
    }
</script>

<style scoped>

    .loading-1 {
        display: inline-block;
        width: 20px;
        height: 20px;
        background: rgba(0,188,212,0.72);
    }

    .loading-2 {
        display: inline-block;
        width: 20px;
        height: 20px;
        background: rgba(0,188,212,0.52);
    }

    .loading-3 {
        display: inline-block;
        width: 20px;
        height: 20px;
        background: rgba(0,188,212,0.32);
    }

    .loading {
        margin: 50px auto;
        width: 100%;
        text-align: center;
    }
</style>
