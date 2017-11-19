import Vue from 'vue'
import VuePaginate from 'vue-paginate'
import VeeValidate from 'vee-validate';

/* '@' is alias for static directory */
import Root from '@/components/Root.vue'
import router from './router'
import store from './store';

Vue.use(VuePaginate);
Vue.use(VeeValidate);

new Vue({
    el: '#app',
    store,
    router,
    template: '<Root/>',
    components: {Root}
});
