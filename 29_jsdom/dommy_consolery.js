// Team Joyful Jalapenos :: Julia Lee, Nicole Zhou 
// SoftDev pd7
// K28 -- Getting more comfortable with the dev console and the DOM
// 2023-04-17
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
var f = function(x) {
  var j=30;
  return j+x;
};

//instantiate an object
//If you type the object name in the consol, it will return the value of that object.
var o = { 'name' : 'Thluffy',
          age : 1024,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
        };

//In console: addItem(text)
//The variable name acts like the function name
var addItem = function(text) { //Adds an item to the end of the list with the value of the text you give. 
  var list = document.getElementById("thelist");
  var newitem = document.createElement("li"); //Creates a list element
  newitem.innerHTML = text;
  list.appendChild(newitem);
};

//Make sure to 0 index or else you will get a type error!
var removeItem = function(n) {
  var listitems = document.getElementsByTagName('li'); //Creates a list of the items in the list with the tag li from the html page
  listitems[n].remove();
};

//Adds red to the list of classes for all of the elements in the html list. 
//Red will only be a visual change when green or blue are not already in the class list.
var red = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};

//Adds red to the class of all even elements in the list and blue to the class of odd ones.
//Red will only be visible if the element does not already have blue or green in the class list.
//Blue will always be visible if it is in the class list as long as .blue class is last in the styling.
var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};

//insert your implementations here for...
function fact(n) {
    if (n < 2) {
      return 1;
    }
    else {
      return (n * fact(n - 1));
    }
  }
  
// fibonacci
function fib(n) {
    if (n == 0) {
        return 0;
    }
    else if (n == 1){
        return 1;
    }
    return (fib(n - 1) + fib(n - 2))
}
// GCD
function gcd(a,b) {
  if (a % b === 0){
    return b;
  }
  return gcd(b, a%b); //This is too much math for me T-T
}

// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const myFxn = (param1, param2) => {
  var retVal = param1*param2
  return retVal;
};

//Locates element with "demo" as the id and replaces value with the given value.
document.getElementById("fact").innerHTML = "fact(4) = " + fact(4);
document.getElementById("fib").innerHTML = "fib(4) = " + fib(4);
document.getElementById("gcd").innerHTML = "gcd(24,20) = " + gcd(24,20);
document.getElementById("mult").innerHTML = "mult(2,4) = " + myFxn(2,4);

var dasbut = document.getElementById("fibb"); 
dasbut.addEventListener('click', ()=>{
	addItem(fib(4))
});
var factbutton = document.getElementById("factb"); 
factbutton.addEventListener('click', ()=>{
	addItem(fact(4))
});
var gcdbutton = document.getElementById("gcdb"); 
gcdbutton.addEventListener('click', ()=>{
	addItem(gcd(24,20))
});