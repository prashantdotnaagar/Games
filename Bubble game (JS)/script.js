var rn=0;
var timer=60;
var newhit


function makebubble(){
    var clutter=" "

for(var i=1;i<130;i++){
    rn= Math.floor(Math.random()*10)
    clutter+=`<div class="bubble">${rn}</div>`;
}

document.querySelector("#pbtm").innerHTML=clutter;
}


function runtimer(){

    var timerint=setInterval(function(){
        if(timer>0){
        timer--;
        document.querySelector("#timer").textContent=timer;
        }
        else{
            clearInterval(timerint);
            document.querySelector("#pbtm").innerHTML=`<h2>Game Over</h2>`;
        }
    },1000)
}


function getnewhit(){
    newhit=Math.floor(Math.random()*10);
    document.querySelector("#hitval").textContent=newhit;
}

var score=0;
function increasescore(){
    score+=10;
    document.querySelector("#scoreval").textContent=score;
}


document.querySelector("#pbtm").addEventListener("click",function(detail){
    var clickednum=Number(detail.target.textContent);
    if(clickednum===newhit){
        increasescore()
        getnewhit();
        makebubble()
    }
})

makebubble();
runtimer();
getnewhit();
