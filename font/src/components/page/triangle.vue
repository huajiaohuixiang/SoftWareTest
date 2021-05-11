<template>
    <div>
        <div class="crumbs">
           
        </div>
        <div class="container">
            <div class="content-title">上传测试用例</div>
            

            <el-upload
                class="upload-demo"
                drag
                action="http://127.0.0.1:5000/upload"
                
                >
                <i class="el-icon-upload"></i>
                <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
                <div class="el-upload__tip" slot="tip">只能上传excel文件哦，且不超过500kb,注意文件内数据格式哦</div>
            </el-upload>

        

        </div>
       

        <div class="container">
            <div class="content-title">下载测试后数据</div>
            
            <div class="plugins-tips">
                <a href="http://127.0.0.1:5000/download" target="_blank">点击下载</a>
            </div>


        

        </div>
    </div>
</template>

<script>
    import VueCropper  from 'vue-cropperjs';
    export default {
        name: 'upload',
        data: function(){
            return {
                defaultSrc: require('../../assets/img/img.jpg'),
                fileList: [],
                imgSrc: '',
                cropImg: '',
                dialogVisible: false,
               
            }
        },
        components: {
            VueCropper
        },
        methods:{
            refresh(){

            }
        },
        created(){
            this.cropImg = this.defaultSrc;
        }
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
</style>