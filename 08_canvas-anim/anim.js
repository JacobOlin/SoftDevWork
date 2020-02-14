//Jacob Olin and Justin Chen
//SoftDev1 pd2
//K08: What is it saving the screen from?
//2020-02-14

var c = document.getElementById("circle");
var end = document.getElementById("stop");
var dvd = document.getElementById("dvd");
var can = document.getElementById("slate");
var ctx = can.getContext("2d");
var radius = 0;
var runningCircle = false;
var runningDvd = false;
var inc = 1;
var id;
var logo = new Image();
var x,y,vx,vy;
logo.src = "logo_dvd.jpg"

//console.log('hello');


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
  if (runningDvd) {
    runningDvd = false;
    window.cancelAnimationFrame(id);
  }
    if (!runningCircle){         //checks to see if the function is already running
      runningCircle = true;
      id = window.requestAnimationFrame(anim);
    }
}
c.addEventListener("click", start_anim);

var dvd_anim = function(e) {
  ctx.clearRect(0,0,500,500);
  ctx.beginPath();
  //ctx.arc(x,y,2,0,2*Math.PI);
  //ctx.fill();
  ctx.drawImage(logo, x, y, 150, 100);
  if (x <= -10 || x >= 360){
    vx *= -1;
  }
  if (y <= -20 || y >= 420){
    vy *= -1;
  }
  x += vx;
  y += vy;
  id = window.requestAnimationFrame(dvd_anim);
}

var dvd_anim_start = function(e){
  if (runningCircle) {
    runningCircle = false;
    window.cancelAnimationFrame(id);
  }
  if (runningDvd){
    window.cancelAnimationFrame(id);
  }

  runningDvd = true;
  x = Math.random() * 350;
  y = Math.random() * 400;
  angle = (Math.random() + 1) * (Math.PI / 6);
  if (Math.random() < 0.5){
    vx = Math.cos(angle);
  }
  else {vx = -1 * Math.cos(angle);}
  if (Math.random() < 0.5){
    vy = Math.sin(angle);
  }
  else {vy = -1 * Math.sin(angle);}
  //console.log(angle  * 180 / Math.PI);
  id = window.requestAnimationFrame(dvd_anim);

}
dvd.addEventListener("click",dvd_anim_start);

var stop = function(e) {
    window.cancelAnimationFrame(id);  //stops the animation
    runningCircle = false;
    runningDvd = false;
}
end.addEventListener("click", stop);
