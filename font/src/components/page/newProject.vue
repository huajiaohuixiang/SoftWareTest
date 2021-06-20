<template>
    <div class="container">
        <div class="content-title">添加新项目</div>
        <el-form ref="form" :model="form" label-width="80px">
            <el-form-item label="项目名称">
                <el-input v-model="form.projectName"></el-input>
            </el-form-item>
            <el-form-item label="方法名称">
                <el-input v-model="form.funcName"></el-input>
            </el-form-item>
            <el-form-item label="方法代码">
                <el-input type="textarea" rows="5" v-model="form.func"></el-input>
            </el-form-item>
            <el-form-item label="输入参数">
                <el-input type="textarea" rows="5" v-model="form.inputParam"></el-input>
            </el-form-item>
            <el-form-item label="输出参数">
                <el-input type="textarea" rows="5" v-model="form.outputParam"></el-input>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="onSubmit">项目创建</el-button>
                <el-button>取消</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>


<script>
import axios from 'axios';
import bus from '../common/bus';

import VueCropper from 'vue-cropperjs';
import CONST from '../common/CONST.vue';
export default {
    data() {
        return {
            form: {
                projectName: '',
                funcName: '',
                func: '',
                inputParam: '',
                outputParam: ''
            }
        };
    },
    methods: {
        onSubmit() {
            var that = this;
            var temp;
            axios.post(CONST.url + '/project/createNewProject',{
										form: this.form
			})
                .then(function (response) {
                        console.log(response)
                }
                );
            this.$message.success('提交成功！');
        }
    }
};
</script>

<style scoped>
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