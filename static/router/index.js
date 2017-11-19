import Vue from 'vue'
import Router from 'vue-router'

/* '@' is alias for static directory */
import Underpriced from '@/components/Underpriced.vue'
import Overpriced from '@/components/Overpriced.vue'
import Estimate from '@/components/Estimate.vue'

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'underpriced',
      component: Underpriced
    },
    {
      path: '/overpriced',
      name: 'overpriced',
      component: Overpriced
    },
    {
      path: '/estimate',
      name: 'estimate',
      component: Estimate
    }
  ]
})
