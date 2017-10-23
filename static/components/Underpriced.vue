<template>
    <div class="underpriced">
        <div v-if="isNotLoaded">
            <g-loading></g-loading>
        </div>
        <div v-else class="filters">
            <select v-model="filterQueries['rooms_number']">
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

            <paginate
                    name="flats"
                      :list="underpricedFlats"
                      :per="20"
            >
                <div v-for="flat in paginated('flats')" class="entry">
                    <div class="image-column">
                        <img :src="flat.image" class="flat-image">
                    </div>
                    <div class="first-column">
                        <span class="subway">м. {{ flat.underground }}</span><br>
                        <span class="location">{{ flat.underground_distance }} мин. от метро</span><br>
                        <!-- <span class="district">район {{ flat.district }}</span> -->
                        <a :href="flat.ad" target="_blank" class="button">Перейти к объявлению</a>
                    </div>
                    <div class="second-column">
                        <span v-if="flat.rooms_number === -1" class="rooms">Студия,</span>
                        <span v-else>
                            {{ flat.rooms_number }}
                            <span class="rooms-hint">комн,</span>
                        </span>
                        <span class="area">{{ flat.areas[0] }}</span>
                        <span class="area-hint">кв. м
                            (кухня: {{ flat.areas[1] }} кв. м,
                            жилая: {{ flat.areas[2] }} кв. м)</span><br>
                        <span class="floor">{{ flat.floors[0] }}</span>
                        <span class="area-hint">этаж из {{ flat.floors[1] }}</span><br>
                        <span class="external">{{ flat.address }}</span><br>
                    </div>
                    <div class="third-column">
                        <span class="actual-price">{{ flat.price }}</span>
                        <span class="actual-price-hint">руб. / месяц</span><br>
                        <!--<span class="predicted-price-title">Предсказанная цена:</span>-->
                        <!--<span class="predicted-price">{{ flat.predicted_price }}</span>-->
                        <!--<span class="predicted-price-hint">руб. / месяц</span><br>-->
                        <a :href="flat.ad" target="_blank" class="source">cian.ru</a>
                    </div>
                    <br>
                </div>
            </paginate>
            <paginate-links for="flats" :show-step-links="true"
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
                    rooms_number: "",
                    underground: "",
                    address: ""
                },
                paginate: ['flats']
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
                                if (flat.hasOwnProperty(field)) {
                                    filter = filter && flat[field].toString().toLowerCase()
                                        .indexOf(this_.filterQueries[field].toLowerCase()) !== -1;
                                }
                            });
                            return filter;
                        }
                    )
            },
        },
    }
</script>
