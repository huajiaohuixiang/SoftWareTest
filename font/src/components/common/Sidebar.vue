<template>
<!-- unique-opened   -->
 
    <div class="sidebar">
        <el-menu
            class="sidebar-el-menu"
            :default-active="onRoutes"
            :collapse="collapse"
            background-color="#324157"
            text-color="#bfcbd9"
            active-text-color="#20a0ff"
           router
            
        >
            <template v-for="item in items">
                <template v-if="item.subs">
                    <el-submenu :index="item.index" :key="item.index" >
                        <template slot="title">
                            <i :class="item.icon"></i>
                            <span slot="title">{{ item.title }}</span>
                        </template>
                        <template v-for="(subItem,subindex) in item.subs">
                            <el-submenu
                                v-if="subItem.subs"
                                :index="subItem.index"
                                :key="subItem.index"
                            >
                                <template slot="title">{{ subItem.title }}</template>
                                <el-menu-item
                                    v-for="(threeItem,i) in subItem.subs"
                                    :key="i"
                                    :index="threeItem.index"
                                    v-on:click="changeProject()"
                                >{{ threeItem.title }}</el-menu-item>
                            </el-submenu>
                            <el-menu-item
                                v-else
                               :index="subindex+''"
                                :key="subItem.label"

                                v-on:click="changeProject(subItem)"
                            > <i :class="subItem.icon"></i>{{ subItem.title }}</el-menu-item>
                            <!-- :index="subItem.index" -->
                        </template>
                    </el-submenu>
                </template>
                <template v-else>
                    <el-menu-item :index="item.index" :key="item.index">
                        <i :class="item.icon"></i>
                        <span slot="title">{{ item.title }}</span>
                    </el-menu-item>
                </template>
            </template>
        </el-menu>
    </div>
</template>

<script>
import axios from 'axios';
import bus from '../common/bus';
import CONST from '../common/CONST.vue';

export default {
    data() {
        return {
            collapse: false,
            items: [
             
                {
                    icon: 'el-icon-menu',
                    index: 'project',
                    title: '我的项目'
                    
                }   ,
                {
                    icon: 'el-icon-plus',
                    index: 'newProject',
                    title: '添加项目'
                },
                {
                    icon: 'el-icon-menu',
                    index: 'JavaProject',
                    title: '我的测试项目',
                    
                }   ,{
                    icon: 'el-icon-lx-global',
                    index: 'a',
                    title: 'problem2',
                }  ,{
                    icon: 'el-icon-lx-global',
                    index: 'b',
                    title: 'problem4',
                }  ,{
                    icon: 'el-icon-lx-global',
                    index: 'c',
                    title: 'problem5',
                }  ,{
                    icon: 'el-icon-lx-global',
                    index: 'd',
                    title: 'problem7',
                }  ,{
                    icon: 'el-icon-lx-global',
                    index: 'e',
                    title: 'problem9',
                }  ,
                {
                    icon: 'el-icon-lx-global',
                    index: 'f',
                    title: 'problem10',
                }  ,
                {
                    icon: 'el-icon-lx-global',
                    index: 'g',
                    title: 'problem12',
                }  ,
                {
                    icon: 'el-icon-lx-global',
                    index: 'h',
                    title: 'problem13',
                },
            ]
        };
    },
    methods: {
        changeProject(subItem) {
            console.log(subItem)
            console.log(this._GLOBAL.project)
            this._GLOBAL.project=subItem.title
            if(subItem.mylabel=="JavaProject"){
                this.$router.push( '/JavaProject/' + subItem.title)
                localStorage.setItem("JavaProjectName",subItem.title)
            }else{
                this.$router.push( '/project/' + subItem.title)

            }
        },


    },
    computed: {
        onRoutes() {
            return this.$route.path.replace('/', '');
        }
    },

    created() {
        // 通过 Event Bus 进行组件间通信，来折叠侧边栏
        bus.$on('collapse', msg => {
            this.collapse = msg;
            bus.$emit('collapse-content', msg);
        });
      //  this.getProjectInfo()
       // this.getJavaProjectInfo()
    }
};
</script>

<style scoped>
.sidebar {
    display: block;
    position: absolute;
    left: 0;
    top: 70px;
    bottom: 0;
    overflow-y: scroll;
}
.sidebar::-webkit-scrollbar {
    width: 0;
}
.sidebar-el-menu:not(.el-menu--collapse) {
    width: 250px;
}
.sidebar > ul {
    height: 100%;
}
</style>
