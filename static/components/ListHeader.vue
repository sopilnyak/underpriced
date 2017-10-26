<template>
    <div class="list-header">
        <a class="tab" :class="{ tabActive: this.$store.state.active === 'underpriced' }" @click="clickUnderpriced">
            Недооцененные
        </a>
        <a class="tab" :class="{ tabActive: this.$store.state.active === 'overpriced' }" @click="clickOverpriced">
            Переоцененные
        </a>
        <a class="tab" :class="{ tabActive: this.$store.state.active === 'estimate' }">
            Оценить квартиру
        </a>
    </div>
</template>

<script>

    export default {
        name: 'ListHeader',
        methods: {
            clickOverpriced() {
                this.$store.state.active = 'overpriced';
                this.$router.push({name: 'overpriced'});
            },
            clickUnderpriced() {
                this.$store.state.active = 'underpriced';
                this.$router.push({name: 'underpriced'});
            },
        }
    }
</script>

<style scoped>
    .list-header {
        background: #072050;
        background: -webkit-linear-gradient(to right, #072050, #375084, #072050);
        background: linear-gradient(to right, #072050, #375084, #072050);
    }
    .tab {
        background-color: rgba(167,177,199,0.78);
        padding: 7px;
        display: inline-block;
        width: 200px;
        text-align: center;
    }
    .tab:not(.tabActive):hover {
        cursor: pointer;
    }
    .tabActive {
        background-color: #EDEFF1;
    }
</style>
