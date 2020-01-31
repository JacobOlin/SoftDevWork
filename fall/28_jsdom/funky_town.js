var fact = function(n){
  if (n == 1){
    return 1;
  }
  return n * fact(n - 1);
}

var fib = function(n){
    if (n > 1){
	return fib(n-1) + fib(n-2);
    }
    if (n == 1){
	return 1;
    }
    return 0;
}

var gcd = function(a,b){
    while( b ){
	var x = b;
	b = a % x;
	a = x;
    }
    return a;
}

var studentlist = ["Bob", "Jane", "Ed", "Chan", "Jason", "Hoiley", "TP", "Steve", "Vivi"];

var randomStudent = function(a){
    var l = a.length;
    var rand = Math.floor(Math.random(l) * l + 1);
    return a[rand - 1];
}

var executeFib = function(){
  var answer = fib(7)
  console.log(answer)
}

var executeGcd = function(){
  var answer = gcd(144,188)
  console.log(answer)
}

var executeName = function(){
  var answer = randomStudent(studentlist)
  console.log(answer)
}

var fib0 = document.getElementById("fib")
fib0.addEventListener('click',executeFib)
var gcd0 = document.getElementById("gcd")
gcd0.addEventListener('click',executeGcd)
var name0 = document.getElementById("name")
name0.addEventListener('click',executeName)
