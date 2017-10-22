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
            </select>
            <input v-model="filterQueries['subway']" placeholder="Поиск по метро...">
            <input v-model="filterQueries['district']" placeholder="Поиск по району...">

            <paginate name="flats" :list="underpricedFlats" :per="20">
                <div v-for="flat in paginated('flats')" class="entry">
                    <div class="first-column">
                        <span class="subway">м. {{ flat.subway }}</span><br>
                        <span class="location">{{ flat.location }}</span><br>
                        <span class="district">район {{ flat.district }}</span>
                        <a :href="flat.link" target="_blank" class="button">Перейти к объявлению</a>
                    </div>
                    <div class="second-column">
                        <span class="rooms">{{ flat.rooms }}</span>
                        <span class="rooms-hint">комн,</span>
                        <span class="area">{{ flat.rooms }}</span>
                        <span class="area-hint">кв. м</span><br>
                        <span class="floor">{{ flat.floor }}</span>
                        <span class="area-hint">этаж</span><br>
                        <span class="external">{{ flat.external }}</span><br>
                    </div>
                    <div class="third-column">
                        <span class="actual-price">{{ flat.actual_price }}</span>
                        <span class="actual-price-hint">руб. / месяц</span><br>
                        <span class="predicted-price-title">Предсказанная цена:</span>
                        <span class="predicted-price">{{ flat.predicted_price }}</span>
                        <span class="predicted-price-hint">руб. / месяц</span><br>
                        <a :href="flat.link" target="_blank" class="source">{{ flat.source }}</a>
                    </div>
                    <br>
                </div>
            </paginate>
            <paginate-links for="flats"
                      :show-step-links="true"
                    :step-links="{
                        next: 'Вперед',
                        prev: 'Назад'
                     }"></paginate-links>
        </div>
    </div>
</template>

<script>
    import GLoading from "./GLoading.vue"

    export default {
        name: 'Overpriced',
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
                    subway: "",
                    district: ""
                },
                paginate: ['flats']
            }
        },
        created() {
            this.$store.dispatch('loadOverpriced');
            this.$store.state.active = 'overpriced';
        },
        computed: {
            isNotLoaded() {
                return this.$store.state.overpricedData === null;
            },
            underpricedFlats() {
                let this_ = this;
                let filterFields = Object.keys(this_.filterQueries);
                return this_.$store.state.overpricedData
                    .filter(
                        function (flat) {
                            let filter = true;
                            filterFields.forEach(function(field) {
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

<style scoped>
    .underpriced {
        width: 100%;
    }

    .filters {
        padding: 20px 40px;
    }

    select {
        -webkit-appearance: button;
        -webkit-border-radius: 2px;
        -webkit-padding-end: 20px;
        -webkit-padding-start: 2px;
        -webkit-user-select: none;
        background-image: url(http://i62.tinypic.com/15xvbd5.png);
        background-color: #FFFFFF;
        background-position: 97% center;
        background-repeat: no-repeat;
        border: 1px solid #bbb694;
        color: #555;
        font-size: 15px;
        overflow: hidden;
        padding: 5px 10px;
        text-overflow: ellipsis;
        white-space: nowrap;
        width: 160px;
        margin-right: 10px;
    }

    select:hover {
        cursor: pointer;
    }

    .button {
        -webkit-appearance: button;
        -webkit-border-radius: 2px;
        background-color: #f8ffcc;
        border: 1px solid #bbb694;
        color: #555;
        overflow: hidden;
        padding: 5px 10px;
        text-overflow: ellipsis;
        white-space: nowrap;
        display: inline-block;
        text-decoration: none;
        margin-top: 10px;
    }

    .button:hover {
        cursor: pointer;
    }

    input {
        -webkit-border-radius: 2px;
        padding: 5px 10px;
        border: 1px solid #bbb694;
        color: #555;
        font-size: 15px;
        overflow: hidden;
        padding: 5px 10px;
        text-overflow: ellipsis;
        white-space: nowrap;
        width: 160px;
        margin-right: 10px;
    }

    .entry {
        display: block;
        margin: 20px 0;
        border: 1px solid #bbb694;
        -webkit-border-radius: 2px;
        padding: 20px 30px;
    }

    .entry:hover {
        background-color: #FFF9C4;
        border-color: #F9A825;
    }

    .first-column {
        float: left;
        width: 30%;
    }

    .second-column {
        float: left;
        width: 30%;
    }

    .third-column {
        float: right;
        text-align: right;
    }

    br {
        clear: both;
    }

    .actual-price {
        font-size: 30px;
        color: #424445;
    }

    .actual-price-hint {
        color: gray;
        font-size: 18px;
        margin-left: 2px;
    }

    .predicted-price-title {
        color: gray;
        font-size: inherit;
    }

    .predicted-price-hint {
        color: gray;
        font-size: 15px;
    }

    .source {
        font-size: 10px;
        color: gray;
        text-decoration: none;
    }

    .subway {
        font-weight: bold;
    }

    .location {
        font-size: 12px;
    }

    .district {
        display: block;
        margin-top: 5px;
    }

    .rooms {

    }

    .rooms-hint {
        color: gray;
    }

    .area {

    }

    .area-hint {
        color: gray;
    }

    .floor {

    }

    .external {
        display: block;
        margin-top: 3px;
    }


</style>
