<template>
    <div>
        <div class="container">
            <el-dropdown @command="handleCommand">
                <span class="el-dropdown-link"> 选择项目<i class="el-icon-arrow-down el-icon--right"></i> </span>
                <el-dropdown-menu slot="dropdown">
                    <el-dropdown-item v-for="(item, i) in allproject" v-bind:key="i" :command="item">{{ item }}</el-dropdown-item>
                </el-dropdown-menu>
            </el-dropdown>
            <div class="content-title">{{ projectID }}</div>
            <el-input type="textarea" rows="5" v-model="funcInfo" :disabled="funcvisi"></el-input>
        </div>

        <div class="container">
            <el-row :gutter="22">
                <el-col :span="12">
                    <div class="content-title">上传测试用例</div>

                    <el-input class="inputSty" placeholder="请输入" v-model="name" :input="refresh">
                        <template slot="prepend">测试人员姓名</template>
                    </el-input>
                    <el-input class="inputSty" placeholder="请输入" v-model="testmethod" :input="refresh">
                        <template slot="prepend">测试方法</template>
                    </el-input>

                    <el-button type="success" round v-on:click="refresh">确认</el-button>

                    <el-upload class="upload-demo" drag :action="upload" :on-success="accuCallBack">
                        <i class="el-icon-upload"></i>
                        <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
                        <div class="el-upload__tip" slot="tip">只能上传excel文件哦，且不超过500kb,注意文件内数据格式哦</div>
                    </el-upload>
                </el-col>
                <el-col :span="12">
                    <div class="content-title">下载测试后数据</div>
                    <div class="plugins-tips">
                        <a :href="download" target="_blank">点击下载</a>
                    </div>
                    <el-button type="success" round v-on:click="getAcc">获取测试结果</el-button>

                    <el-card shadow="hover">
                        <schart ref="pie" class="schart" canvasId="pie" :options="options"></schart>
                    </el-card>
                </el-col>
            </el-row>
        </div>
    </div>
</template>

<script>
import Schart from 'vue-schart';
import axios from 'axios';
import bus from '../common/bus';

import VueCropper from 'vue-cropperjs';
import CONST from '../common/CONST.vue';
export default {
    name: 'upload',
    data: function () {
        return {
            allproject: [],
            projectID: this._GLOBAL.project,
            funcInfo: '',
            funcvisi: true,
            defaultSrc: require('../../assets/img/img.jpg'),
            fileList: [],
            imgSrc: '',
            cropImg: '',
            dialogVisible: false,
            name: 'admin',
            testmethod: '边界值测试',
            upload: CONST.url + '/projecttest/upload/' + this._GLOBAL.project + '/',
            download: CONST.url + '/projecttest/download/' + this._GLOBAL.project + '/',
            options: {
                type: 'pie',
                title: {
                    text: '测试正确率'
                },
                xRorate: 25,
                labels: ['True', 'False'],
                datasets: [
                    {
                        data: [0.67, 0.33]
                    }
                ]
            },
            temp: 0
        };
    },

    // +this.name+"/"+this.testmethod
    // +this.name+"/"+this.testmethod
    components: {
        VueCropper,
        Schart
    },
    watch: {
        // 若路由路径变化，从全局变量刷新 projectID
        // $route() {
        //     this.projectID = this._GLOBAL.project;
        //     this.getProFunc();
        //     this.refresh();
        // }
    },
    created() {
        this.cropImg = this.defaultSrc;
        this.upload = this.upload + this.name + '/' + this.testmethod;
        this.download = this.download + this.name + '/' + this.testmethod;
        this.handleListener();
        this.getProjectInfo()
    },
    activated() {
        this.handleListener();
    },
    deactivated() {
        window.removeEventListener('resize', this.renderChart);
        bus.$off('collapse', this.handleBus);
    },
    methods: {
        handleCommand(command) {
            let that = this;
            this.getProFunc(command)
            this.projectID=command
            this.refresh()
        },
        getProjectInfo() {
            var that = this;
            axios.get(CONST.url + '/project/getAllProject').then(function (response) {
                console.log(response);
                that.allproject=response.data
            });
        },

        accuCallBack(response, file, fileList) {
            console.log(response);
            this.options.datasets[0].data[0] = response;
            this.options.datasets[0].data[1] = 1 - response;
            this.$refs.pie.renderChart();
            console.log('a');
        },
        getProFunc(name) {
            var that = this;
            axios.get(CONST.url + '/project/getProjectFunc/' + name).then(function (response) {
                console.log(response.data);
                that.funcInfo = response.data;
            });
        },
        refresh() {
            //刷新URL
            this.upload = CONST.url + '/projecttest/upload/' + this.projectID + '/' + this.name + '/' + this.testmethod;
            this.download = CONST.url + '/projecttest/download/' + this.projectID + '/' + this.name + '/' + this.testmethod;
            console.log(this.upload);
            console.log(this.download);
            return true;
        },
        changeData() {
            this.options.datasets[0].data[0] = 0.5;
            console.log('a');
            this.options.datasets[0].data[1] = 0.5;

            console.log(this.options.datasets[0].data);
            this.$refs.pie.renderChart();
        },
        getAcc() {
            //获得准确率
            var that = this;
            var temp;
            axios.get(CONST.url + '/question2/getAccuracy/' + this.name + '/' + this.testmethod).then(function (response) {
                console.log(that.options.datasets[0].data[0]);
                console.log(response);
                that.temp = response.data;
                that.options.datasets[0].data[0] = response.data;
                console.log('a');
                that.options.datasets[0].data[1] = 1 - response.data;
                console.log('b');
                that.$refs.pie.renderChart();
            });
        },
        handleListener() {
            bus.$on('collapse', this.handleBus);
            // 调用renderChart方法对图表进行重新渲染
            window.addEventListener('resize', this.renderChart);
        },
        handleBus(msg) {
            setTimeout(() => {
                this.renderChart();
            }, 200);
        },
        renderChart() {
            this.$refs.pie.renderChart();
            // this.$refs.line.renderChart();
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
.inputSty {
    width: 250px;
}
.content-title {
    font-weight: 400;
    line-height: 50px;
    margin: 10px 0;
    font-size: 22px;
    color: #1f2f3d;
}
.pre-img {
    width: 100px;
    height: 100px;
    background: #f8f8f8;
    border: 1px solid #eee;
    border-radius: 5px;
}
.crop-demo {
    display: flex;
    align-items: flex-end;
}
.crop-demo-btn {
    position: relative;
    width: 100px;
    height: 40px;
    line-height: 40px;
    padding: 0 20px;
    margin-left: 30px;
    background-color: #409eff;
    color: #fff;
    font-size: 14px;
    border-radius: 4px;
    box-sizing: border-box;
}
.crop-input {
    position: absolute;
    width: 100px;
    height: 40px;
    left: 0;
    top: 0;
    opacity: 0;
    cursor: pointer;
}
.schart {
    width: 100%;
    height: 300px;
}
.el-row {
    margin-bottom: 20px;
}
</style>