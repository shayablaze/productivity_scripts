console.log('stamba')

var foo = function(el){
  console.log('hello ' + el);
}
foo(4)

function wait(ms){
   ms = ms*1000
   var start = new Date().getTime();
   var end = start;
   while(end < start + ms) {
     end = new Date().getTime();
  }
}

i = 0;
var before = new Date();
console.log('before is'+before)
while (true){
  i++;
  console.log('pre-wait');
  wait(2);  //7 seconds in milliseconds
  if (i==4){
    break;
  }
}

var after = new Date();
console.log('after is'+after)

var difference = after.getTime() - before.getTime();

var date = new Date(null);
date.setSeconds(difference/1000); // specify value for SECONDS here
difference = date.toISOString().substr(11, 8);


console.log('difference is '+ difference)
console.log('bye');
