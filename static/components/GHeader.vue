<template>
    <div class="header">
        <img src="/static/logo.png" class="logo" @click="clickIndex">
        <div class="title" @click="clickIndex">Underpriced</div>
    </div>
</template>

<script>
    export default {
        name: 'GHeader',
        methods: {
            clickIndex() {
                this.$router.push({name: 'underpriced'})
            },
        }
    }
</script>

<style scoped>
    .header {
        background-color: #00BCD4;
        margin: 0;
        padding: 20px 40px;
        height: 30px;
    }
    .title {
        float: left;
        font-size: 22px;
        color: #ffffff;
    }
    .logo {
        float: left;
        display: block;
        width: 20px;
        height: 20px;
        margin-right: 20px;
    }
    .title:hover {
        cursor: pointer;
    }
    .logo:hover {
        cursor: pointer;
    }
</style>
