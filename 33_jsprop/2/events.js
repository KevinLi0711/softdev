// demo 2
// JS event propagation

var tds = document.getElementsByTagName('td');
var trs = document.getElementsByTagName('tr');
var table = document.getElementsByTagName('table')[0];

var clicky = function(e) {
  alert( this.innerHTML );
};

for (var x=0; x < tds.length; x++) {
  tds[x].addEventListener('click', clicky); //content of cell
}

for (x=0; x < trs.length; x++) {
  trs[x].addEventListener('click', clicky); //content of tr (tds)
}

table.addEventListener('click', clicky); //content of table (trs,tds)


// Q: When user clicks on a cell, in what order will the pop-ups appear?
// A: It will appear in the order they are called (content of the cell, content of row, content of table)
