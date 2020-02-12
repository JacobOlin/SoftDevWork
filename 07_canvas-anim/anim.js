//Jacob Olin
//SoftDev1 pd2
//KK #06: Dot Dot Dot
//2020-02-12

var c = document.getElementById("start");
var d = document.getElementById("stop");
var can = document.getElementById("slate");
var ctx = can.getContext("2d");
var radius = 0;
var stopped = false;
var inc = 1;
var id;


var anim = function(e) {
  w = 500
  h = 500
  ctx.clearRect(0,0,w,h);
  ctx.beginPath();

  ctx.arc(w/2, h/2, radius, 0, 2 * Math.PI);
  ctx.fill();

  radius += 1*inc
  if ((radius < 250 && inc == 1) || (radius > 0 && inc == -1)){
    //id = window.requestAnimationFrame(anim);
    window.requestAnimationFrame(anim);
  }
  else{
    inc *= -1;
    window.requestAnimationFrame(anim);
  }

}
c.addEventListener("click", anim);


var stop = function(e) {
    window.cancelAnimationFrame(id);
}
c.addEventListener("click", stop);
