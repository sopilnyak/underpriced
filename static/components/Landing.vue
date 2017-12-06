<template>
    <div>
        <landing-header></landing-header>
        <div class="landing" :key="'loading'">
            <div v-if="isNotLoaded">
                <g-loading></g-loading>
            </div>
            <div :key="'landing'" v-else>
                <div class="landing-left">
                    <div class="landing-intro-text">

                        <div class="landing-main">Найдите недооцененные и переоцененные квартиры</div>
                        <div class="landing-sub">При помощи нашего сервиса вы можете найти квартиры, цена аренды
                            которых занижена или завышена
                        </div>
                        <div class="landing-button" @click="clickUnderpriced">
                            Перейти к списку объявлений
                        </div>

                    </div>

                    <div class="landing-intro-text">

                        <div class="landing-main">Оцените свою квартиру</div>
                        <div class="landing-sub">Узнайте, сколько стоит аренда вашей квартиры</div>
                        <div class="landing-button" @click="clickEstimate">
                            Оценить квартиру
                        </div>

                    </div>
                </div>
                <div class="landing-right">
                    <img @click="clickUnderpriced" class="image" src="/static/icons/screen_main.png" />
                </div>
            </div>

        </div>
    </div>
</template>

<script>
    import GLoading from "./GLoading.vue"
    import LandingHeader from './LandingHeader.vue'

    export default {
        name: 'Landing',
        components: {
            GLoading,
            LandingHeader,
        },
        created() {
            this.$store.state.active = 'landing';
        },
        mounted() {
            this.setListener();
            this.setHeight();
        },
        computed: {
            isNotLoaded() {
                return this.subways === null;
            },
        },
        methods: {
            setListener() {
                let this_ = this;
                $(window).resize(function() {
                    this_.setHeight();
                });
            },
            setHeight() {
                $('.landing').height($('body').height() - $('.header').outerHeight() -
                    $('.list-header').outerHeight() - $('.footer').outerHeight());
            },
            clickUnderpriced() {
                this.$store.state.active = 'underpriced';
                this.$router.push({name: 'underpriced'});
            },
            clickEstimate() {
                this.$store.state.active = 'estimate';
                this.$router.push({name: 'estimate'});
            },
        }
    }
</script>

<style scoped>

    .landing {
        display: block;
        padding: 0 7%;
        position: relative;
        overflow: hidden;
        color: #EDEFF1;
        background: -webkit-linear-gradient(to right, #072050, #375084, #072050);
        background: linear-gradient(to right, #072050, #375084, #072050);
        box-shadow: inset 0 0 20px rgba(0,0,0,0.3);
    }

    .landing-button {
        width: 16em;
        display: block;
        margin-top: 20px;
        color: #000000;
        font-size: 17px;
        text-align: center;
        padding: 0.4em;
        border-radius: 5px;
        background-color: #e9d282;
        height: 1.5em;
        box-shadow: 0 0 10px rgba(0,0,0,0.5);
        cursor: pointer;
    }

    .landing-main {
        font-size: 30px;
        color: #d2d4c4;
        font-weight: bold;
        padding-top: 40px;
    }

    .landing-sub {
        margin-top: 15px;
        color: #aeb0a0;
        width: 80%;
        font-size: 17px;
        max-width: 500px;
    }

    .image {
        margin-left: 3em;
        margin-top: 50px;
        height: 400px;
        display: block;
        box-shadow: 0 0 20px rgba(0,0,0,0.5);
    }

    .landing-left {
        float: left;
        width: 50%;
    }

    .landing-right {
        float: left;
        width: 40%;
    }

</style>