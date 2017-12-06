<template>
    <div class="underpriced">
        <list-header></list-header>
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
                <option value="студия">Студия</option>
            </select>
            <input class="filter-underground" v-model="filterQueries['underground']" placeholder="Поиск по метро...">
            Не более
            <input class="filter-distance" v-model="filterQueries['distance']" placeholder="время до метро"> минут
            <select class="filter-distance-type" v-model="filterQueries['distance_type']">
                <option selected value="">на чем угодно</option>
                <option value="пешком">пешком</option>
                <option value="на машине">на транспорте</option>
            </select>
            <div class="sort-container">
                <span class="folders-head-sort">
                    <span @click="setDropdownVisibility()">По {{ sortFieldText }}</span>
                    <span @click="changeSortDirection" class="filter"> {{ sortDirectionSign }} </span>
                </span>
                <div :class="{ 'dropdown-hidden': isDropdownHidden, 'dropdown': !isDropdownHidden }">
                    <div class="dropdown-entry" @click="sortBy('price')">По реальной цене</div>
                    <div class="dropdown-entry" @click="sortBy('estimated_price')">По предсказанной цене</div>
                    <div class="dropdown-entry" @click="sortBy('relative_goodness')" title="Сортировать по соотношению реальной и предсказанной цен">
                        По соотношению
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
                      :list="overpricedFlats"
                      :per="20">
                <div v-for="flat in paginated('flats')" class="entry">
                    <div class="image-column">
                        <div :style="{ backgroundImage: 'url(' + getImage(flat) + '), url(\'/static/icons/default_flat.png\')' }" class="flat-image"></div>
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
                        <span title="Предсказанная цена" class="predicted-price">{{ formatPrice(flat.estimated_price) }}</span>
                        <span class="predicted-price-hint">руб. / месяц</span><br>
                        <span class="actual-price-title">Реальная цена:</span>
                        <span class="actual-price">{{ formatPrice(flat.price.rub_price) }}</span>
                        <span class="actual-price-hint">руб. / месяц</span><br>
                        <a :href="flat.url" target="_blank" class="button">Перейти к объявлению</a><br>
                        <a :href="flat.url" title="Источник объявления" target="_blank" class="source">cian.ru</a>
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
    import ListHeader from './ListHeader.vue'

    export default {
        name: 'Overpriced',
        components: {
            GLoading,
            ListHeader
        },
        data: function () {
            return {
                filterQueries: {
                    rooms: "",
                    underground: "",
                    address: "",
                    distance: "",
                    distance_type: "",
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
            overpricedFlats() {
                let this_ = this;
                let filterFields = Object.keys(this_.filterQueries);
                return this_.$store.state.overpricedData
                    .filter(
                        function (flat) {
                            let filter = true;
                            filterFields.forEach(function(field) {
                                switch (field) {
                                case 'distance':
                                    if (Object.keys(flat.underground)[0] !== undefined) {
                                        let distance = flat.underground[Object.keys(flat.underground)[0]].match(/\d+/)[0];
                                        filter = filter && (this_.filterQueries['distance'] === "" ||
                                            parseInt(distance) <= parseInt(this_.filterQueries['distance']));
                                    }
                                    break;
                                case 'distance_type':
                                    if (Object.keys(flat.underground)[0] !== undefined) {
                                        filter = filter && flat.underground[Object.keys(flat.underground)[0]].toString().toLowerCase()
                                            .indexOf(this_.filterQueries['distance_type'].toLowerCase()) !== -1;
                                    }
                                    break;
                                case 'underground':
                                    if (Object.keys(flat.underground)[0] !== undefined) {
                                        filter = filter && Object.keys(flat.underground)[0].toString().toLowerCase()
                                            .indexOf(this_.filterQueries[field].toLowerCase()) !== -1;
                                    }
                                    break;
                                default:
                                    if (flat[field] === null) {
                                        filter = false;
                                    }
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
                            let sortField = this_.sortField;
                            let sortDirection = this_.sortDirection;
                            let value1 = parseInt(a[sortField]);
                            let value2 = parseInt(b[sortField]);
                            if (sortField === "price") {
                                value1 = parseInt(a.price.rub_price);
                                value2 = parseInt(b.price.rub_price);
                            }
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
                if (this.sortField === 'estimated_price') {
                    return 'предсказанной цене';
                }
                if (this.sortField === 'relative_goodness') {
                    return 'соотношению';
                }
                return '';
            },
            shareButtonVK() {
                return VK.Share.button({ url: "http://underpriced.ru/"}, {type: "round", text: "Поделиться" });
            },
            shareButtonFB() {
                return '<iframe class="fb-iframe" src="https://www.facebook.com/plugins/share_button.php?href=http%3A%2F%2Funderpriced.ru&layout=button_count&size=small&mobile_iframe=true&width=68&height=20&appId" ' +
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
            predicted(price) {
                return this.formatPrice(parseInt(price) + parseInt(Math.random() * 10000));
            },
            getImage(flat) {
                return flat.images[0] !== undefined ? flat.images[0] : '/static/icons/default_flat.png';
            },
        }
    }
</script>
