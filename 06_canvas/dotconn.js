var c = document.getElementById("clear");
var d = document.getElementById("slate");
var ctx = d.getContext("2d");
var xLast = -1;
var yLast = -1;


var clear = function(e) {
    ctx.clearRect(0, 0, 300, 300);
    xLast = -1;
    yLast = -1;
}
c.addEventListener("click", clear);


var connect = function(e) {
    console.log(e)
    ctx.beginPath();
    ctx.arc(e.offsetX, e.offsetY, 5, 0, 2 * Math.PI);
    ctx.fill();
    if (xLast >= 0) {
      ctx.moveTo(xLast,yLast);
      ctx.lineTo(e.offsetX,e.offsetY)
      ctx.stroke();
    }

    xLast = e.offsetX;
    yLast = e.offsetY;
}
d.addEventListener("click", connect);
