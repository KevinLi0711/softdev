var c = document.getElementById("playground");
var dotbutton = document.getElementById("buttonCircle");
var stopbutton = document.getElementById("buttonStop");

var ctx = c.getContext("2d");
ctx.fillStyle = "blue"
var requestID;

var clear = (e) => {
    ctx.clearRect(0, 0, c.width, c.height)
};

var radius = 0;
var growing = true;

var drawDot = () => {
    window.requestAnimationFrame(drawDot)
    clear()
    drawCircle()
    if (growing) {
        if (radius > c.width / 2) {
            growing = false
        }
        radius += 1
    } else {
        if (radius <= 0) {
            growing = true
        }
        radius -= 1
    }
}

var drawCircle = () => {
    var x = c.width / 2
    var y = c.height / 2
    ctx.beginPath()
    ctx.arc(x, y, radius, 0, 2 * Math.PI)
    ctx.stroke()
}

dotbutton.addEventListener("click", drawDot)
//stopbutton.addEventListener("click", stopIt)
