// demo 1
// JS event propagation

var tds = document.getElementsByTagName('td');

var clicky = function(e) {
  alert( this.innerHTML ); //this refers to the object that calls the function
};

for (var x=0; x < tds.length; x++) {
  tds[x].addEventListener('click', clicky); //returns the innerHTML of td objs. when clicked
}

//if you click on a table cell it will display an alert with the content in the cell