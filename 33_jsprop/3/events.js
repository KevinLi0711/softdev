// demo 3
// JS event propagation

var tds = document.getElementsByTagName('td');
var trs = document.getElementsByTagName('tr');
var table = document.getElementsByTagName('table')[0];

var clicky = function(e) {
  alert( this.innerHTML );
  //Q: What will happen when next line is uncommented?
  //A: only one of the alerts will appear
  //e.stopPropagation();
};

for (var x=0; x < tds.length; x++) {
  tds[x].addEventListener('click', clicky);
}

for (x=0; x < trs.length; x++) {
  trs[x].addEventListener('click', clicky,  true);
}

//Predict, then test...
//Q: What effect does the boolean arg have?
//A: give priority to pop-up (seen by user first)
//   (Leave exactly 1 version uncommented to test...)

table.addEventListener('click', clicky); //gives priority to this Listener (pop-up appears first)
//table.addEventListener('click', clicky, false); //default same as 2

// Q: When user clicks on a cell, in what order will the pop-ups appear?
// A: Table pop-up, cell pop-up, row pop-up

