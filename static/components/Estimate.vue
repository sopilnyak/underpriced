<template>
    <div class="estimate">
        <div v-if="isNotLoaded">
            <g-loading></g-loading>
        </div>
        <div v-else class="filters">
            <div class="header">
                Введите параметры своей квартиры, и мы оценим примерную стоимость ее аренды.
            </div>
            <form class="estimate-input">
                <input v-on:keyup.enter="postEstimate" placeholder="Метро..."
                       v-model="filterSubway" ref="underground" class="underground">
                <div class="subway-list"
                     :class="{ 'subway-list-hidden': this.filterSubway === '' || this.isSubwaySelected !== null }" >
                    <div v-for="subway in subwayList" class="subway-list-entry"
                         @click="selectSubway(subway.name)">
                        {{ subway.name }}
                    </div>
                </div>
                <select ref="rooms" class="rooms">
                    <option selected>Кол-во комнат</option>
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                    <option value="4">4</option>
                    <option value="5">5</option>
                    <option value="студия">Студия</option>
                </select>
                <input v-on:keyup.enter="postEstimate" placeholder="Общая площадь"
                       ref="area" class="area">
                <input v-on:keyup.enter="postEstimate" placeholder="Площадь кухни"
                       ref="kitchen_area" class="kitchen-area">
                <input v-on:keyup.enter="postEstimate" placeholder="Жилая площадь"
                       ref="living_area" class="living-area">
                <select ref="repair" class="repair">
                    <option selected>Ремонт</option>
                    <option value="косметический">Косметический</option>
                    <option value="евроремонт">Евроремонт</option>
                    <option value="дизайнерский">Дизайнерский</option>
                    <option value="отсутствует">Отсутствует</option>
                </select>
                <br>
                <select ref="has_balcony" class="has-balcony">
                    <option selected>Наличие балкона</option>
                    <option value="да">Да</option>
                    <option value="нет">Нет</option>
                </select>
                <select ref="has_loggia" class="has-loggia">
                    <option selected>Наличие лоджии</option>
                    <option value="да">Да</option>
                    <option value="нет">Нет</option>
                </select>
                <input v-on:keyup.enter="postEstimate" placeholder="Этаж"
                       ref="curr_floor" class="curr-floor">
                <input v-on:keyup.enter="postEstimate" placeholder="Этажей в доме"
                       ref="total_floor" class="total-floor">
                <input v-on:keyup.enter="postEstimate" placeholder="Год постройки дома"
                       ref="construction_year" class="construction-year">
                <select ref="house_type" class="house-type">
                    <option selected>Тип дома</option>
                    <option value="панельный">Панельный</option>
                    <option value="блочный">Блочный</option>
                    <option value="кирпичный">Кирпичный</option>
                    <option value="монолитный">Монолитный</option>
                    <option value="кирпично-монолитный">Кирпично-монолитный</option>
                    <option value="сталинский">Сталинский</option>
                    <option value="старый фонд">Старый фонд</option>
                </select>
            </form>
            <div class="post-estimate">
                <a @click.prevent="postEstimate" target="_blank" class="button button-estimate">Оценить</a>
            </div>
            <div v-if="isEstimated" class="price">
                <span class="price-text">Предсказанная цена:</span>
                <span class="price-number">{{ estimatedPrice }} рублей</span>
            </div>
            <div class="pre-footer"></div>
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
                estimatedPrice: null,
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
            },
            isEstimated() {
                return this.estimatedPrice;
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
                let flat = {
                    area: this.$refs.area.value,
                    combined_bathroom_count: this.$refs.area.combined_bathroom_count,
                    construction_year: this.$refs.construction_year.value,
                    house_type: this.$refs.house_type.value,
                    kitchen_area: this.$refs.kitchen_area.value,
                    living_area: this.$refs.living_area.value,
                    repair: this.$refs.repair.value,
                    rooms: this.$refs.rooms.value,
                    underground: this.$refs.underground.value,
                    has_balcony: this.$refs.has_balcony.value,
                    has_loggia: this.$refs.has_loggia.value,
                    curr_floor: this.$refs.curr_floor.value,
                    total_floor: this.$refs.total_floor.value
                };
                $.ajax({
                    url: '/flats/estimate/',
                    type: 'POST',
                    data: flat,
                    success: function (response) {
                        alert(response);
                    },
                    error: function (jqXHR, e) {
                        //console.log('Unable to load overpriced' + e);
                        alert("error!");
                    }
                });

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
    .estimate {
        min-width: 1300px;
    }
    .subway-list-hidden {
        display: none;
    }
    .subway-list {
        position: absolute;
        left: 140px;
        max-height: 300px;
        overflow: hidden;
    }
    .header {
        font-size: 20px;
        margin-top: 60px;
        margin-left: 100px;
        margin-bottom: 10px;
    }
    .button-estimate {
        width: 200px;
        text-align: center;
    }
    .post-estimate {
        margin-top: 20px;
        margin-left: 100px;
        width: 100%;
    }
    .price {
        margin-top: 20px;
        text-align: center;
        font-size: 30px;
    }
    .pre-footer {
        margin-bottom: 350px;
    }
    .price-text {
        color: gray;
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
    .estimate-input {
        margin-left: 100px;
        margin-right: 100px;
    }
    .estimate-input input {
        margin-top: 20px;
    }
    .estimate-input select {
        margin-top: 20px;
    }
    .underground {
        width: 10.5em;
    }
    .area {
        width: 8em;
    }
    .kitchen-area {
        width: 8em;
    }
    .living-area {
        width: 8em;
    }
    .curr-floor {
        width: 5.3em;
    }
    .total-floor {
        width: 8em;
    }
    .has-balcony {
        width: 12em;
    }
    .rooms {
        width: 11em;
    }
    .has-loggia {
        width: 11em;
    }
</style>