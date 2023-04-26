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
    stopIt() //stops current animation
    requestID = window.requestAnimationFrame(drawDot) //starts a new animation
    clear() //clear canvas
    drawCircle() //draw image
    if (growing) {
        radius += 1
        if (radius > c.width / 2) {
            growing = false
        }
    } else {
        radius -= 1
        if (radius <= 0) {
            growing = true
        }
    }
}

var drawCircle = () => {
    var x = c.width / 2
    var y = c.height / 2
    ctx.beginPath()
    ctx.arc(x, y, radius, 0, 2 * Math.PI)
    ctx.stroke()
    ctx.fill()
}

var stopIt = () => {
    window.cancelAnimationFrame(requestID) //cancel current animation
}

dotbutton.addEventListener("click", drawDot)
stopbutton.addEventListener("click", stopIt)
