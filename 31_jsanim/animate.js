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
    if (growing) {
        //window.requestAnimationFrame(drawDot)
        clear()
        drawCircle()
        radius += 10
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
stopbutton.addEventListener("click", stopIt)
