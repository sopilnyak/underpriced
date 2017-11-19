<template>
    <div class="underpriced">
        <div v-if="isNotLoaded">
            <g-loading></g-loading>
        </div>
        <div v-else class="filters">
            <select v-model="filterQueries['rooms']">
                <option selected value="">Кол-во комнат</option>
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5">5</option>
                <option value="-1">Студия</option>
            </select>
            <input v-model="filterQueries['underground']" placeholder="Поиск по метро...">
            <input v-model="filterQueries['address']" placeholder="Поиск по адресу...">
            <span class="sort-container">
                <span @click="changeSortDirection">Сортировать по цене</span>
                <span @click="changeSortDirection" class="filter"> {{ sortDirectionSign }} </span>
            </span>

            <paginate
                    name="flats"
                      :list="underpricedFlats"
                      :per="20">
                <div v-for="flat in paginated('flats')" class="entry">
                    <div class="image-column">
                        <div :style="{ backgroundImage: 'url(' + flat.images[0] + ')' }" class="flat-image"></div>
                    </div>
                    <div class="first-column">
                        <span class="subway">м. {{ Object.keys(flat.underground)[0] }}</span><br>
                        <span class="location">{{ flat.underground[Object.keys(flat.underground)[0]] }}</span><br>
                        <span v-if="flat.district !== ''" class="district">район: {{ flat.district }}</span>
                    </div>
                    <div class="second-column">
                        <span v-if="flat.rooms === -1" class="rooms">Студия,</span>
                        <span v-else>
                            {{ flat.rooms }}
                            <span class="rooms-hint">комн,</span>
                        </span>
                        <span class="area">{{ flat.area }}</span>
                        <span class="area-hint">кв. м
                            (кухня: {{ flat.kitchen_area }} кв. м,
                            жилая: {{ flat.living_area }} кв. м)</span><br>
                        <span class="area-hint">Этаж:</span>
                        <span class="floor">{{ flat.floor }}</span><br>
                        <span class="external">{{ flat.address }}</span><br>
                    </div>
                    <div class="third-column">
                        <span class="actual-price">{{ flat.price.rub_price }}</span>
                        <span class="actual-price-hint">руб. / месяц</span><br>
                        <!--<span class="predicted-price-title">Предсказанная цена:</span>-->
                        <!--<span class="predicted-price">{{ flat.predicted_price }}</span>-->
                        <!--<span class="predicted-price-hint">руб. / месяц</span><br>-->
                        <a :href="flat.url" target="_blank" class="button">Перейти к объявлению</a><br>
                        <a :href="flat.url" target="_blank" class="source">cian.ru</a>
                    </div>
                    <br>
                </div>
            </paginate>
            <paginate-links class="pagination-block" for="flats" :show-step-links="true"
                            :step-links="{
                                next: 'Вперед',
                                prev: 'Назад'
                            }">
            </paginate-links>
        </div>
    </div>
</template>

<script>
    import GLoading from "./GLoading.vue"

    export default {
        name: 'Underpriced',
        components: {
            GLoading
        },
        data: function () {
            return {
                filterRooms: "",
                filterSubway: "",
                filterDistrict: "",
                filterQueries: {
                    rooms: "",
                    underground: "",
                    address: ""
                },
                paginate: ['flats'],
                sortDirection: 1,
            }
        },
        created() {
            this.$store.dispatch('loadUnderpriced');
            this.$store.state.active = 'underpriced';
        },
        computed: {
            isNotLoaded() {
                return this.$store.state.underpricedData === null;
            },
            underpricedFlats() {
                let this_ = this;
                let filterFields = Object.keys(this_.filterQueries);
                return this_.$store.state.underpricedData
                    .filter(
                        function (flat) {
                            let filter = true;
                            filterFields.forEach(function(field) {
                                if (flat[field] === null) {
                                    filter = false;
                                }
                                if (field === 'underground' && Object.keys(flat.underground)[0] !== undefined) {
                                    filter = filter && Object.keys(flat.underground)[0].toString().toLowerCase()
                                        .indexOf(this_.filterQueries[field].toLowerCase()) !== -1;
                                } else {
                                    if (flat.hasOwnProperty(field)) {
                                        filter = filter && flat[field].toString().toLowerCase()
                                            .indexOf(this_.filterQueries[field].toLowerCase()) !== -1;
                                    }
                                }
                            });
                            return filter;
                        }
                    )
                    .sort(
                        function (a, b) {
                            let value1 = parseInt(a.price.rub_price);
                            let value2 = parseInt(b.price.rub_price);

                            if (value1 === null || value2 === null || value1 === value2) {
                                return this_.sortDirection
                            }
                            return ((value1 < value2) ? -1 : 1) * this_.sortDirection;
                        }
                    );
            },
            sortDirectionSign() {
                if (this.sortDirection === 1) {
                    return '▲'
                } else {
                    return '▼';
                }
            },
        },
        methods: {
            changeSortDirection() {
                this.sortDirection *= -1
            },
        }
    }
</script>