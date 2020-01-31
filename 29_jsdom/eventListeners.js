// Devin Lin and Jacob Olin
// SoftDev pd2
// 29 -- Sequential Progression III: Season of the Witch
// 2019-12-13
var changeHeading = function(e) {
  var h = document.getElementById("h");
  h.innerHTML = e.target.innerHTML; //changes header
};

var removeItem = function(e) {
  e.target.remove();  //removes item from the DOM
};

var lis = document.getElementsByTagName("li"); //Generates a list with every item in the list

var helloWorld = function() {
  document.getElementById("h").innerHTML = "Hello World!";
};

for (var i = 0; i < lis.length; i++) {
  // console.log(lis[i]);
  lis[i].addEventListener('mouseover', changeHeading); //adds different events to occur
  lis[i].addEventListener('mouseout', helloWorld);     //when any of these actions
  lis[i].addEventListener('click', removeItem);        //happen
}

var addItem = function(e) {
    var list = document.getElementById("list");
    var item = document.createElement("li");           //creates item with tag "li"
    item.innerHTML = "WORD";
    item.addEventListener( 'mouseover', changeHeading);
    item.addEventListener( 'mouseout', helloWorld);
    item.addEventListener( 'click', removeItem);
    list.appendChild(item);                            //adds new item to list
};

var button = document.getElementById("button");
button.addEventListener('click', addItem);

var fib = function(n) {
  if(n < 2) {
    return 1;
  } else {
    return fib(n-1) + fib(n-2);
  }
};

var addFib = function(e) {
  console.log(e);
  var fiblist = document.getElementById("fibans");
  var children = fiblist.childNodes;
  var item = document.createElement("li");
  item.innerHTML = fib(children.length - 1);
  fiblist.appendChild(item);
};

var addFib2 = function(e) {
  console.log(e);
  var fiblist = document.getElementById("fibans");
  var children = fiblist.childNodes;
  var item = document.createElement("li");
  var length = children.length;

  if (length > 2) {
    item.innerHTML = parseInt(children[length - 2].innerHTML) + parseInt(children[length - 1].innerHTML);
  } else {
    item.innerHTML = "1";
  }
  fiblist.appendChild(item);
};

var fib = document.getElementById("fib");
fib.addEventListener("click", addFib2);
