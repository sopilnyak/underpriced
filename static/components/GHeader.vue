<template>
    <div class="header">
        <img src="/static/icons/ur_white.png" class="logo" @click="clickIndex">
        <div class="title" @click="clickIndex">Underpriced</div>
    </div>
</template>

<script>
    export default {
        name: 'GHeader',
        methods: {
            clickIndex() {
                this.$router.push({name: 'landing'})
            },
        }
    }
</script>

<style scoped>
    .header {
        background: #072050;
        background: -webkit-linear-gradient(to right, #072050, #375084, #072050);
        background: linear-gradient(to right, #072050, #375084, #072050);
        margin: 0;
        padding: 20px 40px;
        height: 35px;
    }
    .title {
        float: left;
        font-size: 22px;
        color: #ffffff;
    }
    .logo {
        float: left;
        display: block;
        width: 100px;
        height: 100px;
        margin-right: 10px;
        margin-top: -15px;
    }
    .title:hover {
        cursor: pointer;
    }
    .logo:hover {
        cursor: pointer;
    }
</style>
