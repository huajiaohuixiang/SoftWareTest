import Vue from 'vue';
import Router from 'vue-router';

Vue.use(Router);

export default new Router({
    routes: [{
            path: '/',
            redirect: '/newProject'
        },
        {
            path: '/',
            component: () =>
                import ( /* webpackChunkName: "home" */ '../components/common/Home.vue'),
            meta: { title: '自述文件' },
            children: [{
                    path: '/newProject',
                    component: () =>
                        import ( /* webpackChunkName: "dashboard" */ '../components/page/newProject.vue'),
                    meta: { title: '添加项目' }
                },
                {
                    path: '/JavaProject',
                    component: () =>
                        import ( /* webpackChunkName: "dashboard" */ '../components/page/JavaProject.vue'),
                    meta: { title: '我的测试项目' }
                },
                {
                    path: '/project',
                    component: () =>
                        import ( /* webpackChunkName: "dashboard" */ '../components/page/Project.vue'),
                    meta: { title: '我的项目' }
                },
                {
                    path: '/charge',
                    component: () =>
                        import ( /* webpackChunkName: "dashboard" */ '../components/page/charge.vue'),
                    meta: { title: '电信收费问题' }
                },
                {
                    path: '/computer',
                    component: () =>
                        import ( /* webpackChunkName: "dashboard" */ '../components/page/computer.vue'),
                    meta: { title: '电脑销售问题' }
                },
                {
                    path: '/projectboundary',
                    component: () =>
                        import ( /* webpackChunkName: "dashboard" */ '../components/page/projectboundary.vue'),
                    meta: { title: '项目边界值问题' }
                },
                {
                    path: '/discussion1',
                    component: () =>
                        import ( /* webpackChunkName: "dashboard" */ '../components/page/discussion1.vue'),
                    meta: { title: '讨论题2' }
                },
                {
                    path: '/discussion2',
                    component: () =>
                        import ( /* webpackChunkName: "dashboard" */ '../components/page/discussion2.vue'),
                    meta: { title: '讨论题4' }
                },
                {
                    path: '/discussion3',
                    component: () =>
                        import ( /* webpackChunkName: "dashboard" */ '../components/page/discussion3.vue'),
                    meta: { title: '讨论题7' }
                }
            ]
        },


    ]
});