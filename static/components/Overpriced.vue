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
            <div class="sort-container">
                <span class="folders-head-sort">
                    <span @click="setDropdownVisibility()">Сортировано по {{ sortFieldText }}</span>
                    <span @click="changeSortDirection" class="filter"> {{ sortDirectionSign }} </span>
                </span>
                <div :class="{ 'dropdown-hidden': isDropdownHidden, 'dropdown': !isDropdownHidden }">
                    <div class="dropdown-entry" @click="sortBy('price')">По реальной цене</div>
                    <div class="dropdown-entry" @click="sortBy('predicted')">По предсказанной цене</div>
                    <div class="dropdown-entry" @click="sortBy('difference')" title="Сортировать по разнице между реальной и предсказанной ценой">
                        По разнице
                    </div>
                </div>
            </div>
            <!--<span class="sort-container">
                <span @click="changeSortDirection">Сортировать по цене</span>
                <span @click="changeSortDirection" class="filter"> {{ sortDirectionSign }} </span>
            </span>-->
            <span class="shareFB" v-html="shareButtonFB"></span>
            <span class="shareVK" v-html="shareButtonVK"></span>

            <paginate
                    name="flats"
                      :list="underpricedFlats"
                      :per="20"
            >
                <div v-for="flat in paginated('flats')" class="entry">
                    <div class="image-column">
                        <div :style="{ backgroundImage: 'url(' + flat.image + ')' }" class="flat-image"></div>
                    </div>
                    <div class="first-column">
                        <span class="subway">м. {{ flat.underground }}</span><br>
                        <span class="location">{{ flat.underground_distance }} мин. от метро</span><br>
                        <!-- <span class="district">район {{ flat.district }}</span> -->
                    </div>
                    <div class="second-column">
                        <span class="rooms">{{ flat.rooms_number }}</span>
                        <span class="rooms-hint">комн,</span>
                        <span class="area">{{ flat.areas[0] }}</span>
                        <span class="area-hint">кв. м
                            (кухня: {{ flat.areas[1] }} кв. м,
                            жилая: {{ flat.areas[2] }} кв. м)</span><br>
                        <span class="floor">{{ flat.floors[0] }}</span>
                        <span class="area-hint">этаж из {{ flat.floors[1] }}</span><br>
                        <span class="external">{{ flat.address }}</span><br>
                    </div>
                    <div class="third-column">
                        <span title="Предсказанная цена" class="predicted-price">{{ formatPrice(100000) }}</span>
                        <span class="predicted-price-hint">руб. / месяц</span><br>
                        <span class="actual-price-title">Реальная цена:</span>
                        <span class="actual-price">{{ formatPrice(flat.price) }}</span>
                        <span class="actual-price-hint">руб. / месяц</span><br>
                        <a :href="flat.ad" target="_blank" class="button">Перейти к объявлению</a><br>
                        <a :href="flat.ad" title="Источник объявления" target="_blank" class="source">cian.ru</a>
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
        name: 'Overpriced',
        components: {
            GLoading
        },
        data: function () {
            return {
                filterQueries: {
                    rooms_number: "",
                    underground: "",
                    address: ""
                },
                paginate: ['flats'],
                sortDirection: -1,
                sortField: "price",
                isDropdownHidden: true,
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
                    .sort(
                        function (a, b) {
                            let sortField = this_.sortField;
                            let sortDirection = this_.sortDirection;
                            let value1 = parseInt(a[sortField]);
                            let value2 = parseInt(b[sortField]);
                            if (value1 === null || value2 === null || value1 === value2) {
                                return sortDirection;
                            }
                            return ((value1 < value2) ? -1 : 1) * sortDirection;
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
            sortFieldText() {
                if (this.sortField === 'price') {
                    return 'реальной цене';
                }
                if (this.sortField === 'predicted') {
                    return 'предсказанной цене';
                }
                if (this.sortField === 'difference') {
                    return 'разнице';
                }
                return '';
            },
            shareButtonVK() {
                return VK.Share.button({ url: "http://underpriced.ru/"}, {type: "round", text: "Поделиться" });
            },
            shareButtonFB() {
                return '<iframe src="https://www.facebook.com/plugins/share_button.php?href=http%3A%2F%2Funderpriced.ru&layout=button_count&size=small&mobile_iframe=true&width=68&height=20&appId" ' +
                    'width="68" height="20" style="border:none;overflow:hidden" scrolling="no" frameborder="0" ' +
                    'allowTransparency="true"></iframe>'
            }
        },
        methods: {
            changeSortDirection() {
                this.sortDirection *= -1
            },
            sortBy(field) {
                this.sortField = field;
                this.isDropdownHidden = true;
            },
            formatPrice(price) {
                return price.toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ");
            },
            setDropdownVisibility() {
                this.isDropdownHidden = !this.isDropdownHidden;
            },
        },
    }
</script>
