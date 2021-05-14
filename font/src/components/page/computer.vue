<template>
    <div>
        <div class="crumbs">
           
        </div>
        <div class="container">
            <div class="content-title">上传测试用例</div>
            <div>
                <el-input placeholder="请输入名字" v-model="name"  :input="refresh">
                    <template slot="prepend">测试人员姓名</template>
                </el-input>
            </div>
            <div>
                
                <el-select v-model="testmethod" slot="prepend" placeholder="请选择" :change="refresh">
                    
                    <el-option label="边界值测试" value="1"></el-option>
                
                </el-select>
                  <el-button type="success" round v-on:click= "refresh">确认</el-button>

            </div>    
            

            <el-upload
                class="upload-demo"
                drag
                :action="upload"
                
                >
                <i class="el-icon-upload"></i>
                <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
                <div class="el-upload__tip" slot="tip">只能上传excel文件哦，且不超过500kb,注意文件内数据格式哦</div>
            </el-upload>

        </div>

        <div class="container">
            <el-button type="success" round v-on:click="getAcc">获取测试结果</el-button>

            <el-row :gutter="30">
            <el-col :span="22">
                <el-card shadow="hover">
                    <schart ref="pie" class="schart" canvasId="pie" :options="options"></schart>
                </el-card>
            </el-col>
          
        </el-row>
        </div>
        


        <div class="container">
            <div class="content-title">下载测试后数据</div>
            
            <div class="plugins-tips">
                <a :href="download" target="_blank">点击下载</a>
            </div>


        </div>
    </div>
</template>

<script>
import Schart from 'vue-schart';
import axios from 'axios';
import bus from '../common/bus';

import VueCropper  from 'vue-cropperjs';
import CONST from '../common/CONST.vue';
    export default {
        name: 'upload',
        data: function(){
            return {
                defaultSrc: require('../../assets/img/img.jpg'),
                fileList: [],
                imgSrc: '',
                cropImg: '',
                dialogVisible: false,
                name: "admin",
                testmethod: "边界值测试",
                upload: CONST.url+"/question2/upload/",
                download: CONST.url+"/question2/download/",
                options: {
                    type: 'pie',
                    title: {
                        text: '测试正确率'
                    },
                    xRorate: 25,
                    labels: ['True', 'False'],
                    datasets: [{
                        data: [1,0]
                    }]
                },
                temp: 0
            }
        },

        // +this.name+"/"+this.testmethod
        // +this.name+"/"+this.testmethod
        components: {
            VueCropper,
            Schart
        },

        created(){
            this.cropImg = this.defaultSrc;
            this.upload=this.upload+this.name+"/"+this.testmethod;
            this.download=this.download+this.name+"/"+this.testmethod;
            this.handleListener();
        
        },
        activated() {
            this.handleListener();
        },
        deactivated() {
            window.removeEventListener('resize', this.renderChart);
            bus.$off('collapse', this.handleBus);
        },
        methods:{
            
            refresh(){
               this.upload=CONST.url+"/question2/upload/"+this.name+"/"+this.testmethod;
                this.download=CONST.url+"/question2/download/"+this.name+"/"+this.testmethod; 
                console.log(this.upload)
                console.log(this.download)
                return true
            },
            changeData(){
                this.options.datasets[0].data[0]=0.5
                        console.log("a")
                this.options.datasets[0].data[1]=0.5

                console.log(this.options.datasets[0].data)
                this.$refs.pie.renderChart();

            },
            getAcc(){
                var that=this
                var temp;
                axios.get(CONST.url+"/question2/getAccuracy/"+this.name+"/"+this.testmethod)
                    .then(function(response){
                        console.log(that.options.datasets[0].data[0])
                        console.log(response)
                        that.temp=response.data;
                        that.options.datasets[0].data[0]=response.data
                        console.log("a")
                        that.options.datasets[0].data[1]=1-response.data
                        console.log("b")
                        that.$refs.pie.renderChart();

                })
                

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
        
        },
        
    }
</script>

<style scoped>
    .content-title{
        font-weight: 400;
        line-height: 50px;
        margin: 10px 0;
        font-size: 22px;
        color: #1f2f3d;
    }
    .pre-img{   
        width: 100px;
        height: 100px;
        background: #f8f8f8;
        border: 1px solid #eee;
        border-radius: 5px;
    }
    .crop-demo{
        display: flex;
        align-items: flex-end;
    }
    .crop-demo-btn{
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
    .crop-input{
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