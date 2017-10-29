<template>
    <div class="estimate">
        <div v-if="isNotLoaded">
            <g-loading></g-loading>
        </div>
        <div v-else class="filters">
            <div class="header">
                Введите параметры своей квартиры, и мы оценим примерную стоимость ее аренды.
            </div>
            <div class="subway-input">
                <input v-on:keyup.enter="postEstimate" placeholder="Метро..." v-model="filterSubway">
                <div class="subway-list"
                     :class="{ 'subway-list-hidden': this.filterSubway === '' || this.isSubwaySelected !== null }" >
                    <div v-for="subway in subwayList" class="subway-list-entry"
                         @click="selectSubway(subway.name)">
                        {{ subway.name }}
                    </div>
                </div>
                <input v-on:keyup.enter="postEstimate" placeholder="Минут от метро">
                <select>
                    <option selected>Кол-во комнат</option>
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                    <option value="4">4</option>
                    <option value="5">5</option>
                    <option value="-1">Студия</option>
                </select>
                <input v-on:keyup.enter="postEstimate" placeholder="Площадь">
                <input v-on:keyup.enter="postEstimate" placeholder="Этаж">
                <input v-on:keyup.enter="postEstimate" placeholder="Всего этажей в доме">
            </div>
            <div class="post-estimate">
                <a @click="postEstimate" target="_blank" class="button button-estimate">Оценить</a>
            </div>
        </div>
    </div>
</template>

<script>
    import GLoading from "./GLoading.vue"

    export default {
        name: 'Estimate',
        components: {
            GLoading
        },
        data: function () {
            return {
                subways: null,
                filterSubway: "",
                isSubwaySelected: null,
            }
        },
        created() {
            this.loadSubways();
            this.$store.state.active = 'estimate';
        },
        computed: {
            isNotLoaded() {
                return this.subways === null;
            },
            subwayList() {
                let this_ = this;
                return this_.subways
                    .filter(
                        function (subway) {
                            if (subway.name !== null) {
                                return subway.name.toLowerCase().indexOf(this_.filterSubway.toLowerCase()) !== -1;
                            }
                            return false;
                        }
                    )
            }
        },
        methods: {
            loadSubways() {
                let this_ = this;
                $.ajax({
                    url: '/static/data/subway.json',
                    type: 'GET',
                    success: function (response) {
                        this_.subways = response;
                    },
                    error: function (jqXHR, e) {
                        console.log('Unable to load overpriced' + e);
                    }
                });
            },
            postEstimate() {
                alert("ML!");
            },
            selectSubway(subway) {
                this.filterSubway = subway;
                this.isSubwaySelected = subway;
            }
        },
        watch: {
            filterSubway: function (query) {
                if (query !== this.isSubwaySelected) {
                    this.isSubwaySelected = null;
                }
            }
        }
    }
</script>

<style scoped>
    .subway-list-hidden {
        display: none;
    }
    .subway-list {
        position: absolute;
        left: 40px;
        max-height: 300px;
        overflow: hidden;
    }
    .header {
        font-size: 20px;
        text-align: center;
        margin-top: 60px;
        margin-bottom: 30px;
    }
    .button-estimate {
        width: 200px;
        text-align: center;
    }
    .post-estimate {
        margin-top: 30px;
        width: 100%;
        text-align: center;
        margin-bottom: 350px;
    }
    .subway-list-entry {
        padding: 5px 10px;
        width: 160px;
        overflow: hidden;
        background: #CCD2DD;
        border-bottom: 1px solid #010B20;
        border-left: 1px solid #010B20;
        border-right: 1px solid #010B20;
    }
    .subway-list-entry:hover {
        background: #334C80;
        color: #EDEFF1;
        cursor: pointer;
    }
</style>