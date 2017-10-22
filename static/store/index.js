import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        underpricedData: null,
        overpricedData: null,
        active: 'underpriced',
    },
    mutations: {
        setUnderpriced(state, data) {
            state.underpricedData = data;
        },
        setOverpriced(state, data) {
            state.overpricedData = data;
        }
    },
    actions: {
        loadUnderpriced({commit}) {
            $.ajax({
                url: '/static/data/underpriced.json',
                type: 'GET',
                success: function (response) {
                    commit('setUnderpriced', response);
                },
                error: function (jqXHR, e) {
                    console.log('Unable to load underpriced' + e);
                }
            });
        },
        loadOverpriced({commit}) {
            $.ajax({
                url: '/static/data/overpriced.json',
                type: 'GET',
                success: function (response) {
                    commit('setOverpriced', response);
                },
                error: function (jqXHR, e) {
                    console.log('Unable to load overpriced' + e);
                }
            });
        },
    }
});
