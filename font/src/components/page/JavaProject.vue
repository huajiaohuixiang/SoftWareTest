<template>
    <div>
        <div class="container">
            <el-dropdown @command="handleCommand">
                <span class="el-dropdown-link"> 选择项目<i class="el-icon-arrow-down el-icon--right"></i> </span>
                <el-dropdown-menu slot="dropdown" >
                    <el-dropdown-item  v-for="(item,i) in allproject" v-bind:key="i" :command="item">{{item}}</el-dropdown-item>
                    
                </el-dropdown-menu>
            </el-dropdown>
            <div class="content-title">{{ JavaProjectName }}</div>
        </div>
        <div class="container">
            <el-row>
                <el-col :span="8"
                    ><el-tree :data="data" show-checkbox node-key="id" ref="tree" highlight-current :props="defaultProps"> </el-tree>
                </el-col>

                <el-col :span="8">
                    <div class="buttons">
                        <el-button @click="getCheckedNodes">通过 node 获取</el-button>

                        <!-- <el-button @click="setCheckedNodes">通过 node 设置</el-button> -->

                        <el-button @click="resetChecked">清空</el-button>
                    </div>
                </el-col>
            </el-row>
        </div>
    </div>
</template>
<script>
import axios from 'axios';
import CONST from '../common/CONST.vue'
export default {
    methods: {},

    data() {
        return {
            data: [
                {
                    id: 1,
                    label: '一级 1',
                    children: [
                        {
                            id: 4,
                            label: '二级 1-1',
                            children: [
                                {
                                    id: 9,
                                    label: '三级 1-1-1'
                                },
                                {
                                    id: 10,
                                    label: '三级 1-1-2'
                                }
                            ]
                        }
                    ]
                },
                {
                    id: 2,
                    label: '一级 2',
                    children: [
                        {
                            id: 5,
                            label: '二级 2-1'
                        },
                        {
                            id: 6,
                            label: '二级 2-2'
                        }
                    ]
                },
                {
                    id: 3,
                    label: '一级 3',
                    children: [
                        {
                            id: 7,
                            label: '二级 3-1'
                        },
                        {
                            id: 8,
                            label: '二级 3-2'
                        }
                    ]
                }
            ],
            defaultProps: {
                children: 'children',
                label: 'label'
            },
            allproject: [],
            JavaProjectName: '请选择项目',
        };
    },
    created() {
        this.getJavaProjectInfo()
    },
    methods: {
        handleCommand(command) {
        let that = this;
            axios
                .get('http://127.0.0.1:5000/java/getAllJavaProjectFiles/' + command)
                .then(function (response) {
                    console.log(response);
                    that.data = response.data;
                });
        this.JavaProjectName=command
      },
        getAllJavaProject() {
            let that = this;
            axios
                .get('http://127.0.0.1:5000/java/getAllJavaProjectFiles/' + localStorage.getItem('JavaProjectName'))
                .then(function (response) {
                    console.log(response);
                    that.data = response.data;
                });
        },
        getJavaProjectInfo(){
            var that=this;
            axios.get(CONST.url+"/java/getAllJavaProject").then(function(response){
                console.log(response);
                that.allproject=response.data
                
            })
        },
        getCheckedNodes() {
            console.log(this.$refs.tree.getCheckedNodes());
            let nodes=this.$refs.tree.getCheckedNodes()
            let that=this
            axios.post(CONST.url+'/java/testOneService/'+that.JavaProjectName+'/'+nodes[0].label).then(function(response){

            })

        },

        

        resetChecked() {
            this.$refs.tree.setCheckedKeys([]);
        }
    }
};
</script>

<style scoped>
  .el-dropdown-link {
    cursor: pointer;
    color: #409EFF;
  }
  .el-icon-arrow-down {
    font-size: 12px;
  }
</style>