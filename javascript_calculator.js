function multiply(){
    var mul1= parseFloat(document.getElementById("product1").value);
    var mul2= parseFloat(document.getElementById("product2").value);
    var multiplyer= mul1*mul2;
    document.getElementById("result_product").value= multiplyer;
}
function sum(){
    var sum1= parseFloat(document.getElementById("sum1").value);
    var sum2= parseFloat(document.getElementById("sum2").value);
    var final_sum=sum1+sum2;
    document.getElementById("result_sum").value= final_sum;
}
function sub(){
    var sub1= parseFloat(document.getElementById("sub1").value);
    var sub2= parseFloat(document.getElementById("sub2").value);
    var final_sub= sub1-sub2;
    document.getElementById("result_sub").value= final_sub;
}

function div(){
    var div1= parseFloat(document.getElementById("div1").value);
    var div2= parseFloat(document.getElementById("div2").value);
    var final_div= div1/div2;
    document.getElementById("result_div").value= final_div;
}
function clear_m(){
    document.getElementById("product1").value=""
    document.getElementById("product2").value=""
    document.getElementById("result_product").value= "";
}
function clear_sum(){
    document.getElementById("sum1").value=""
    document.getElementById("sum2").value=""
    document.getElementById("result_sum").value= "";
}
function clear_sub(){
    document.getElementById("sub1").value=""
    document.getElementById("sub2").value=""
    document.getElementById("result_sub").value= "";
}
function clear_div(){
    document.getElementById("div1").value=""
    document.getElementById("div2").value=""
    document.getElementById("result_div").value= "";
}