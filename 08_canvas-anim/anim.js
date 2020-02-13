//Jacob Olin
//SoftDev1 pd2
//K08: What is it saving the screen from?
//2020-02-14

var c = document.getElementById("circle");
var end = document.getElementById("stop");
var dvd = document.getElementById("dvd");
var can = document.getElementById("slate");
var ctx = can.getContext("2d");
var radius = 0;
var running = false;
var inc = 1;
var id;
var logo = new Image();
var x,y,vx,vy;
logo.src = "logo_dvd.jpg"


var anim = function(e) {
  w = 500;
  h = 500;
  ctx.clearRect(0,0,w,h);
  ctx.beginPath();

  ctx.arc(w/2, h/2, radius, 0, 2 * Math.PI);
  ctx.fillStyle = "#1FBED6";
  ctx.fill();
  radius += 1*inc
  if (!((radius < 250 && inc == 1) || (radius > 0 && inc == -1))){   //checks if circle can keep expanding/contracting
      inc *= -1;
  }
  id = window.requestAnimationFrame(anim); //continuously stores new frame's id
}

var start_anim = function(e){
    if (!running){         //checks to see if the function is already running
      running = true;
      id = window.requestAnimationFrame(anim);
    }
}
c.addEventListener("click", start_anim);

var dvd_anim = function(e) {
  ctx.clearRect(0,0,500,500);
  ctx.beginPath();
  ctx.arc(x,y,2,0,2*Math.PI);
  ctx.fill();
  if (x <= 0 || x >= 500){
    vx *= -1;
    console.log('hi');
  }
  if (y <= 0 || y >= 500){
    vy *= -1;
    console.log("hi");
  }
  x += vx;
  y += vy;
  id = window.requestAnimationFrame(dvd_anim);
}

var dvd_anim_start = function(e){
  x = Math.random() * 500;
  y = Math.random() * 500;
  if (Math.random() < 0.5) {
    vx = 1;
  }
  else {
    vx = -1;
  }
  if (Math.random() < 0.5){
    vy = 1;
  }
  else {vy = -1;}
  id = window.requestAnimationFrame(dvd_anim);
}
dvd.addEventListener("click",dvd_anim_start);

var stop = function(e) {
    window.cancelAnimationFrame(id);  //stops the animation
    running = false;
}
end.addEventListener("click", stop);
