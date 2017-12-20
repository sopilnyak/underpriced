<template>
    <div>
        <landing-header></landing-header>
        <div class="landing" :key="'loading'">
            <div v-if="isNotLoaded">
                <g-loading></g-loading>
            </div>
            <div :key="'landing'" v-else>

                <div class="landing-main part-1 container">

                    <div class="row">

                        <div class="col-md-4 landing-block">
                            <img class="landing-icon" src="static/icons/landing1.png" @click="clickUnderpriced">
                            <div class="landing-header" @click="clickUnderpriced">
                                Недооцененные квартиры
                            </div>
                            <div class="landing-hint">
                                Найдите квартиры, цена аренды которых занижена или завышена
                            </div>
                        </div>

                        <div class="col-md-4 landing-block">
                            <img class="landing-icon" src="static/icons/landing2.png" @click="clickEstimate">
                            <div class="landing-header" @click="clickEstimate">
                                Оцените свою квартиру
                            </div>
                            <div class="landing-hint">
                                Укажите параметры своей квартиры и мы оценим стоимость ее аренды
                            </div>
                        </div>

                        <div class="col-md-4 landing-block">
                            <img class="landing-icon how-button" src="static/icons/landing3.png">
                            <div class="landing-header how-button">
                                Как это работает?
                            </div>
                            <div class="landing-hint">
                                Узнайте, какие алгоритмы мы используем
                            </div>
                        </div>

                    </div>

                </div>

                <div class="landing-main part-2">

                    <div class="how-header">Как это работает?</div>

                    <div class="how-block">
                        <img class="how-icon" src="static/icons/landing4.png">
                        <div class="how-text how-1">
                            Мы используем машинное обучение, чтобы проанализировать десятки тысяч объявлений
                        </div>
                    </div>

                    <div class="how-block">
                        <img class="how-icon" src="static/icons/landing5.png">
                        <div class="how-text how-2">
                            Мы оцениваем объявления
                            о сдаче квартир во всех районах Москвы, разного класса и стоимости, и тем самым непрерывно
                            следим за текущим состоянием рынка недвижимости
                        </div>
                    </div>

                    <div class="how-block">
                        <img class="how-icon" src="static/icons/landing6.png">
                        <div class="how-text how-3">
                            Алгоритм определяет, какие параметры дают
                            наибольший вклад в стоимость квартиры: площадь, удаленность от метро, размер кухни или же
                            тип окон
                        </div>
                    </div>

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
            this.setHeight();

            // Scroll to next screen
            $(".how-button").click(function(e) {
                e.preventDefault();
                let target = $(this).parent().parent().parent().nextAll("div");
                $('html, body').stop().animate({
                   scrollTop: target.offset().top
                }, 700);
            });

        },
        computed: {
            isNotLoaded() {
                return this.subways === null;
            },
        },
        methods: {
            setHeight() {
                $('.landing-main').height($('body').height() - $('.header').outerHeight() -
                    $('.list-header').outerHeight() - $('.footer').outerHeight() - 82);
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
        background: #1c263c;
        background: -webkit-linear-gradient(to right, #1c263c, #072050);
        background: linear-gradient(to right, #1c263c, #072050);
        box-shadow: inset 0 0 20px rgba(0,0,0,0.6);
    }

    .landing-main {
        margin: 0 auto;
        width: 80%;
        max-width: 1400px;
        font-size: 30px;
        color: #d2d4c4;
    }

    .landing-block {
        text-align: center;
        cursor: pointer;
        margin-top: 5em;
    }

    .landing-hint {
        font-size: 17px;
        max-width: 320px;
        margin: 0 auto 1em;
        text-align: center;
        color: #a4a6a8;
    }

    .landing-icon {
        width: 200px;
        height: 200px;
        border-radius: 50%;
    }

    .landing-header {
        font-size: 25px;
        font-weight: 300;
        max-width: 350px;
        margin: 1em auto 0.2em;
    }

    .how-header {
        text-align: center;
        font-size: 40px;
        margin: 0 auto 1em;
        padding-top: 3em;
    }

    .how-icon {
        float: left;
        width: 100px;
        height: 100px;
        border-radius: 50%;
    }

    .how-text {
        float: left;
        font-size: 20px;
        margin-left: 2em;
        margin-bottom: 1em;
        width: 80%;
    }

    .how-block {
        padding-top: 1.5em;
        clear: both;
    }

    .how-1 {
        margin-top: 30px;
    }

    .how-2 {
        margin-top: 20px;
    }

    .how-3 {
        margin-top: 20px;
    }

</style>