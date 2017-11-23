import Vue from 'vue'
import VuePaginate from 'vue-paginate'
import VeeValidate from 'vee-validate'
import VueScript2 from 'vue-script2'

/* '@' is alias for static directory */
import Root from '@/components/Root.vue'
import router from './router'
import store from './store';

Vue.use(VuePaginate);
Vue.use(VeeValidate);
Vue.use(VueScript2);

new Vue({
    el: '#app',
    store,
    router,
    template: '<Root/>',
    components: {Root}
});
