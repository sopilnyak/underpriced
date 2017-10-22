<template>
    <div class="list-header">
        <a class="tab" :class="{ tabActive: this.$store.state.active === 'underpriced' }" @click="clickUnderpriced">
            Недооцененные
        </a>
        <a class="tab" :class="{ tabActive: this.$store.state.active === 'overpriced' }" @click="clickOverpriced">
            Переоцененные
        </a>
        <a class="tab" :class="{ tabActive: this.$store.state.isUnderpricedActive === 'estimate' }">
            Оценить квартиру
        </a>
    </div>
</template>

<script>

    export default {
        name: 'ListHeader',
        methods: {
            clickOverpriced() {
                this.$router.push({name: 'overpriced'})
            },
            clickUnderpriced() {
                this.$router.push({name: 'underpriced'})
            },
        }
    }
</script>

<style scoped>
    .list-header {
        padding: 0 40px;
        background-color: #FDD835;
    }
    .tab {
        background-color: #FFF59D;
        padding: 7px;
        display: inline-block;
        width: 200px;
        text-align: center;
    }
    .tab:not(.tabActive):hover {
        cursor: pointer;
    }
    .tabActive {
        background-color: #FFFDE7;
    }
</style>
