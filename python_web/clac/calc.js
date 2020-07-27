// 初始化，建议所有的初始化统一用js来做
// 初始化的工作尽量统一到js里完成，不要放到html标签里，不方便统一管理
function init(){
    var num=document.getElementById('num');
    num.value = 0;
    num.disabled = "disabled";
    // var n1=document.getElementById('n1');
    // n1.onclick = function(){
    //     alert('123');
    // }
    var oButton = document.getElementsByTagName('input');
    var btn_num1;
    var fh;
    for(var i=0;i<oButton.length;i++){
        oButton[i].onclick = function(){
            if(isNumber(this.value)){
                // num.value = (num.value+this.value)*1;
                if(isNull(num.value)){
                    num.value = this.value;
                }else{
                    num.value = num.value+this.value;
                }
            }else{
                var btn_num=this.value;
                switch(btn_num){
                    case "+":
                        btn_num1=num.value*1;
                        num.value=0;
                        fh="+";
                        break;
                    case "-":
                        btn_num1=num.value*1;
                        num.value=0;
                        fh="-";
                        break;
                    case "×":
                        btn_num1=num.value*1;
                        num.value=0;
                        fh="*";
                        break;
                    case "÷":
                        btn_num1=num.value*1;
                        num.value=0;
                        fh="/";
                        break;
                    case "+/-":
                        num.value = sign(num.value);
                        break;
                    case "C":
                        num.value="0";
                        break;
                    case "=":
                        switch(fh){
                            case "+":
                                num.value=btn_num1+num.value*1;
                                break;
                            case "-":
                                num.value=btn_num1-num.value*1;
                                break;
                            case "*":
                                num.value=btn_num1*num.value*1;
                                break;       
                            case "/":
                                if(num.value=="0"){
                                    alert("除数不能为0");
                                    num.value=0;
                                }else{
                                    num.value=btn_num1/num.value*1;
                                }
                                break;                 
                        }
                        break;
                    case ".":
                        //只能出现一次
                        num.value=dec_number(num.value);
                        break;
                    case "m":
                        break;
                    case "←":
                        num.value=back(num.value);
                        break;
                }
            }
        }
    }
    document.getElementById("bing").onclick=function(){
        window.location.href="https://cn.bing.com";
    }

}


//正负号
function sign(n){
    // if(n.indexOf('-')==-1){
    //     n = "-"+n;
    // }else{
    //     n=n.substr(1,n.length);
    // }
    n=Number(n)*-1;
    return n;
}
//退位键
function back(n){
    n=n.substr(0,n.length-1);
    if(isNull(n)){
        n=0;
    }
    return n;
}

//小数点
function dec_number(n){
    if(n.indexOf(".")==-1){
        n=n+".";
    } 
    return n;
}

//验证文本框是否为空或者0
function isNull(n){
    // if(n=='0' || n.length==0){
    //     return true;
    // }else{
    //     return false;
    // }
    return (n=='0' || n.length==0);
}

function isNumber(n){
    // if(!isNaN(n)){
    //     return true; //参数n是数字
    // }else{
    //     return false; //参数n不是数字
    // }
    // isNaN 不能转换为数字true，可以转换成数字false
    return !isNaN(n);
}



















//需要优化
// function num_1_click(){
//     var num=document.getElementById('num');
//     var n = num.value;
//     //方法一，文本框去掉第一个0
//     // if(n=="0"){
//     //     n = '1';
//     // }else{
//     //     n = n + '1';
//     // }
//     // document.getElementById('num').value = n;

//     //方法二
//     // if(n=='0'){
//     //     n='';
//     // }
//     // n = n +'1';
//     // document.getElementById('num').value = n;

//     //方法三
//     n = n + '1';
//     document.getElementById('num').value = n*1;
// }

// function num_2_click(){
//     var num=document.getElementById('num');
//     var n = num.value;
//     n = n + '2';
//     document.getElementById('num').value = n*1;
// }

// function num_3_click(){
//     var num=document.getElementById('num');
//     var n = num.value;
//     n = n + '3';
//     document.getElementById('num').value = n*1;
// }