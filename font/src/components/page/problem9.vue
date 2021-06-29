<template>
    <div id="Problem9">
        <p>Problem9</p>
        构建ATM系统的state transition diagram, 利用state transition testing方法将其转换成transition tree，而后基于transition tree的路径设计测试用例，要考虑robustness。<br>
        &#12288;&#12288;&#12288;&#12288;&#12288;&#12288;&#12288;state transition diagram
        &#12288;&#12288;&#12288;&#12288;&#12288;&#12288;&#12288;&#12288;&#12288;&#12288; transition tree<br>
        <img src="../../assets/img/state.png"/>
        <img src="../../assets/img/transitionTree.png"/><br>
        测试用例根据状态转移条件类似，在transition tree种，考虑了密码错误，处理业务错误命令，未取卡等robustness。

    </div>
</template>