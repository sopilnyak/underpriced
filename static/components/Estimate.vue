<template>
    <div class="estimate">
        <list-header></list-header>
        <div v-if="isNotLoaded" :key="'notloaded'">
            <g-loading></g-loading>
        </div>
        <div v-else class="filters" :key="'loaded'">
            <span class="shareFB" v-html="$parent.shareButtonFB"></span>
            <span class="shareVK" v-html="$parent.shareButtonVK"></span>
            <div class="header">
                Введите параметры своей квартиры, и мы оценим примерную стоимость ее аренды.
            </div>
            <form class="estimate-input">
                <div class="input-block underground">
                    <div class="input-label">Метро</div>
                    <input v-on:keyup.enter="postEstimate" v-validate="'required'" name="underground_name"
                           v-model="filterSubway" ref="underground_name" class="underground-input">
                    <span v-show="errors.has('underground_name')" class="error-message">
                        {{ errors.first('underground_name') }}
                    </span>
                    <div class="subway-list"
                         :class="{ 'subway-list-hidden': this.filterSubway === '' || this.selectedSubway !== null }" >
                        <div v-for="subway in subwayList" class="subway-list-entry"
                             @click="selectSubway(subway.name)">
                            {{ subway.name }}
                        </div>
                    </div>
                </div>
                <div class="input-block underground-time">
                    <div class="input-label">Минут до метро</div>
                    <input v-on:keyup.enter="postEstimate" class="underground-time-input"
                           v-validate="{ required: true, numeric: true, not_in: [0] }" name="underground_time"
                           ref="underground_time">
                    <span v-show="errors.has('underground_time')" class="error-message">
                        {{ errors.first('underground_time') }}
                    </span>
                </div>
                <div class="input-block">
                    <div class="input-label underground_way">&nbsp;</div>
                    <select ref="underground_way" class="underground_way-input">
                        <option value="пешком" selected>пешком</option>
                        <option value="на машине">на транспорте</option>
                    </select>
                </div>
                <div class="input-block">
                    <div class="input-label rooms">Кол-во комнат</div>
                    <select ref="rooms" class="rooms-input">
                        <option value="1" selected>1</option>
                        <option value="2">2</option>
                        <option value="3">3</option>
                        <option value="4">4</option>
                        <option value="5">5</option>
                        <option value="студия">Студия</option>
                    </select>
                </div>
                <div class="input-block area">
                    <div class="input-label">Общая площадь, кв. м.</div>
                    <input v-on:keyup.enter="postEstimate" class="area-input"
                           v-validate="{ required: true, regex: /^\d*[\.\,]?\d*$/, not_in: [0] }" name="area"
                           ref="area">
                    <span v-show="errors.has('area')" class="error-message">
                        {{ errors.first('area') }}
                    </span>
                </div>
                <div class="input-block kitchen-area">
                    <div class="input-label">Площадь кухни, кв. м.</div>
                    <input v-on:keyup.enter="postEstimate" class="kitchen-area-input"
                           v-validate="{ regex: /^\d*[\.\,]?\d*$/, max_value: this.getArea() }" name="kitchen-area"
                           ref="kitchen_area">
                    <span v-show="errors.has('kitchen-area')" class="error-message">
                        {{ errors.first('kitchen-area') }}
                    </span>
                </div>
                <div class="input-block living-area">
                    <div class="input-label">Жилая площадь, кв. м.</div>
                    <input v-on:keyup.enter="postEstimate" class="living-area-input"
                           v-validate="{ regex: /^\d*[\.\,]?\d*$/, max_value: this.getArea() }" name="living-area"
                           ref="living_area">
                    <span v-show="errors.has('living-area')" class="error-message">
                        {{ errors.first('living-area') }}
                    </span>
                </div>
                <br>
                <div class="input-block repair">
                    <div class="input-label">Ремонт</div>
                    <select ref="repair" class="repair-input">
                        <option value="косметический" selected>Косметический</option>
                        <option value="евроремонт">Евроремонт</option>
                        <option value="дизайнерский">Дизайнерский</option>
                        <option value="отсутствует">Отсутствует</option>
                    </select>
                </div>
                <div class="input-block has-balcony">
                    <div class="input-label">Наличие балкона</div>
                    <select ref="has_balcony" class="has-balcony-input">
                        <option value="да">Да</option>
                        <option value="нет" selected>Нет</option>
                    </select>
                </div>
                <div class="input-block has-loggia">
                    <div class="input-label">Наличие лоджии</div>
                    <select ref="has_loggia" class="has-loggia-input">
                        <option value="да" selected>Да</option>
                        <option value="нет">Нет</option>
                    </select>
                </div>
                <div class="input-block house-type">
                    <div class="input-label">Тип дома</div>
                    <select ref="house_type" class="house-type-input">
                        <option value="панельный" selected>Панельный</option>
                        <option value="блочный">Блочный</option>
                        <option value="кирпичный">Кирпичный</option>
                        <option value="монолитный">Монолитный</option>
                        <option value="кирпично-монолитный">Кирпично-монолитный</option>
                        <option value="сталинский">Сталинский</option>
                        <option value="старый фонд">Старый фонд</option>
                    </select>
                </div>
                <div class="input-block curr-floor">
                    <div class="input-label">Этаж</div>
                    <input v-on:keyup.enter="postEstimate" class="curr-floor-input"
                           v-validate="{ numeric: true, not_in: [0] }" name="curr-floor"
                           ref="curr_floor">
                    <span v-show="errors.has('curr-floor')" class="error-message">
                        {{ errors.first('curr-floor') }}
                    </span>
                </div>
                <div class="input-block total-floor">
                    <div class="input-label">Этажей в доме</div>
                    <input v-on:keyup.enter="postEstimate" class="total-floor-input"
                           v-validate="{ numeric: true, min_value: this.getFilledCurrFloor(), not_in: [0] }"
                           name="total-floor" ref="total_floor">
                    <span v-show="errors.has('total-floor')" class="error-message">
                        {{ errors.first('total-floor') }}
                    </span>
                </div>
                <div class="input-block construction-year">
                    <div class="input-label">Год постройки дома</div>
                    <input v-on:keyup.enter="postEstimate" class="construction-year-input"
                           v-validate="{ numeric: true, max_value: this.getCurrentYear() }"
                           name="construction-year" ref="construction_year">
                    <span v-show="errors.has('construction-year')" class="error-message">
                        {{ errors.first('construction-year') }}
                    </span>
                </div>
                <br>
            </form>
            <div class="post-estimate">
                <a @click.prevent="postEstimate" target="_blank" class="button button-estimate">Оценить</a>
                <a @click.prevent="clear" target="_blank" class="button button-clear">Очистить</a>
            </div>
            <div v-if="hasFormErrors" class="error-message-big">Пожалуйста, проверьте форму на ошибки.</div>
            <div v-if="hasBackendErrors" class="error-message-big">Что-то пошло не так. Попробуйте еще раз.</div>
            <div v-if="isEstimating">
                <g-loading></g-loading>
            </div>
            <div v-if="isEstimated && !isEstimating && !hasBackendErrors && !hasFormErrors" class="price">
                <span class="price-text">Предсказанная цена:</span>
                <span class="price-number">{{ $parent.formatPrice(estimatedPrice) }} рублей в месяц</span>
                <div>
                    <span class="shareVKEstimate" v-html="$parent.shareButtonVK"></span>
                    <span class="shareFBEstimate" v-html="$parent.shareButtonFB"></span>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import GLoading from "./GLoading.vue"
    import ListHeader from './ListHeader.vue'
    import ru from '../resources/validation.js';

    export default {
        name: 'Estimate',
        components: {
            GLoading,
            ListHeader
        },
        data: function () {
            return {
                subways: null,
                filterSubway: "",
                selectedSubway: null,
                estimatedPrice: null,
                hasFormErrors: false,
                isEstimating: false,
                hasBackendErrors: false,
            }
        },
        created() {
            this.loadSubways();
            this.$store.state.active = 'estimate';
            this.$validator.localize('ru', {
                messages: ru.messages,
                attributes: {
                    'underground_name': '"Метро"',
                    'area': '"Общая площадь"',
                    'kitchen-area': '"Площадь кухни"',
                    'living-area': '"Жилая площадь"',
                    'curr-floor': '"Этаж"',
                    'total-floor': '"Этажей в доме"',
                    'construction-year': '"Год постройки дома"',
                    'underground_time': '"Минут до метро"',
              }
            });
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
                return this.estimatedPrice !== null;
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
                let this_ = this;
                this.$validator.validateAll().then((result) => {
                    if (!result) {
                        this_.hasFormErrors = true;
                        return;
                    }
                    this_.isEstimating = true;
                    this_.hasBackendErrors = false;
                    this_.hasFormErrors = false;
                    $.ajax({
                        url: '/flats/estimate/',
                        type: 'POST',
                        data: {
                            area: this_.formatFloat(this.$refs.area.value),
                            combined_bathroom_count: "",
                            construction_year: this.$refs.construction_year.value,
                            house_type: this.$refs.house_type.value,
                            kitchen_area: this_.formatFloat(this.$refs.kitchen_area.value),
                            living_area: this_.formatFloat(this.$refs.living_area.value),
                            repair: this.$refs.repair.value,
                            rooms: this.$refs.rooms.value,
                            underground_name: this.$refs.underground_name.value,
                            has_balcony: this.$refs.has_balcony.value,
                            has_loggia: this.$refs.has_loggia.value,
                            curr_floor: this.$refs.curr_floor.value,
                            total_floor: this.$refs.total_floor.value,
                            underground_way: this.$refs.underground_way.value,
                            underground_time: this.$refs.underground_time.value,
                        },
                        success: function (response) {
                            this_.isEstimating = false;
                            this_.estimatedPrice = Math.round(response.price);
                        },
                        error: function (jqXHR, e) {
                            this_.isEstimating = false;
                            this_.hasBackendErrors = true;
                        }
                    });
                });
            },
            formatFloat(input) {
                // replaces commas with dots
                return input.replace(/,/g, '.');
            },
            selectSubway(subway) {
                this.filterSubway = subway;
                this.selectedSubway = subway;
            },
            getCurrentYear() {
                return (new Date()).getFullYear();
            },
            getFilledCurrFloor() {
                return this.$refs.curr_floor === undefined ? 0 : this.$refs.curr_floor.value;
            },
            getArea() {
                return this.$refs.area === undefined ? 0 : this.$refs.area.value;
            },
            clear() {
                this.$refs.area.value = "";
                this.$refs.construction_year.value = "";
                this.$refs.kitchen_area.value = "";
                this.$refs.living_area.value = "";
                this.filterSubway = "";
                this.$refs.underground_name.value = "";
                this.$refs.curr_floor.value = "";
                this.$refs.total_floor.value = "";
                this.$refs.underground_way.value = "";
                this.$refs.underground_time.value = "";
                this.hasFormErrors = false;
                this.isEstimating = false;
                this.estimatedPrice = null;
                this.hasBackendErrors = false;
                this.errors.clear();
            }
        },
        watch: {
            filterSubway: function (query) {
                if (query !== this.selectedSubway) {
                    this.selectedSubway = null;
                }
            }
        }
    }
</script>

<style scoped>
    .estimate {
        min-width: 1100px;
    }
    .subway-list-hidden {
        display: none;
    }
    .subway-list {
        position: absolute;
        max-height: 300px;
        overflow: hidden;
        width: 13.3em;
        z-index: 4;
    }
    .header {
        font-size: 20px;
        margin-top: 60px;
        margin-left: 100px;
        margin-bottom: 10px;
    }
    .button-estimate {
        width: 11.7em;
        text-align: center;
        margin-right: 0.5em;
        margin-bottom: 1em;
    }
    .button-clear {
        width: 11.7em;
        text-align: center;
        background-color: rgba(140,154,182,0.41);
        border-color: rgba(140,154,182,0.31);
        color: inherit;
        margin-bottom: 1em;
    }
    .post-estimate {
        margin-top: 20px;
        margin-left: 100px;
    }
    .price {
        margin-left: 100px;
        font-size: 30px;
    }
    .price-text {
        color: gray;
    }
    .subway-list-entry {
        padding: 5px 10px;
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
    }
    .underground {
        width: 14em;
    }
    .underground-input {
        width: 11em !important;
    }
    .underground-time {
        width: 7.6em;
    }
    .underground-time-input {
        width: 5em !important;
    }
    .rooms {
        width: 12em;
    }
    .area {
        width: 9.8em;
    }
    .area-input {
        width: 7em !important;
    }
    .kitchen-area {
        width: 10em;
    }
    .kitchen-area-input {
        width: 7em;
    }
    .living-area {
        width: 10em;
    }
    .living-area-input {
        width: 7em;
    }
    .repair {
        width: 11.4em;
    }
    .repair-input {
        width: 10em;
    }
    .has-balcony {
        width: 10.2em;
    }
    .has-balcony-input {
        width: 8.8em !important;
    }
    .has-loggia {
        width: 12.1em;
    }
    .curr-floor {
        width: 9.8em;
    }
    .curr-floor-input {
        width: 7em !important;
    }
    .total-floor {
        width: 10em;
    }
    .total-floor-input {
        width: 7em;
    }
    .construction-year {
        width: 10em;
    }
    .construction-year-input {
        width: 7em !important;
    }
    .house-type {
        width: 12.15em;
    }
    .house-type-input {
        width: 10.65em;
    }
    .input-block {
        margin-top: 15px;
        float: left;
    }
    .input-label {
        margin-bottom: 5px;
        margin-left: 1px;
        font-size: 11px;
        width: inherit;
        overflow: hidden;
        text-overflow: ellipsis;
    }
    br {
        clear: both;
    }
    .error-message {
        color: red;
        font-size: 11px;
    }
    .error-message-big {
        color: red;
        margin-left: 100px;
    }
    .shareVKEstimate {
        float: left;
        margin-top: 11px;
        margin-right: 10px;
    }
    .shareFBEstimate {
        float: left;
    }
</style>