a=true;
function search(){
    if (a){
    document.getElementById('tab2').style.transition="1s";
    document.getElementById('tab4').style.width="190px";
    document.getElementById('tab5').style.left="223px";
    document.getElementById('tab2').style.left="249px";
    document.getElementById('tab3_ch').style.transform="rotate(360deg)";
    a=false;
    }
    else{
    document.getElementById('tab4').style.width="0px";
    document.getElementById('tab5').style.left="34px";
    document.getElementById('tab2').style.left="59px";
    document.getElementById('tab3_ch').style.transform="rotate(0deg)";
    a=true;
    }
}

l=document.getElementsByClassName('ab_p_imgl');
deg=0;
function load(){
    if(deg==360)
        deg=0;
    else
        deg+=30;
    for(i=0;i<3;i++){
        l[i].style.transform= "rotate("+deg+"deg)";
    }
}
window.setInterval(load,70);