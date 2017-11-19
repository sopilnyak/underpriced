<template>
    <div class="footer">
        Underpriced, version {{ version }}
    </div>
</template>

<script>
    export default {
        name: 'GFooter',
        data: function() {
            return {
                version: 0.2
            }
        }
    }
</script>

<style scoped>
    .footer {
        margin-top: 20px;
        padding-top: 8px;
        padding-left: 10px;
        height: 30px;
        background: #072050;
        color: #EDEFF1;
        background: -webkit-linear-gradient(to right, #072050, #375084, #072050);
        background: linear-gradient(to right, #072050, #375084, #072050);
    }
</style>
