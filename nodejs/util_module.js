//%s: String
//%d: Number
//%j: JSON

console.log('util print test')
var util = require('util');

var str1 = util.format('%d + %d + %d', 1, 2, (1+2));
console.log(str1);

var str2 = util.format('%s %s', 'Hello', ' NodeJS');
console.log(str2);

//inherit test
console.log('util inherit test');
function Father(){
}

//메모리 공간 절약 prototype
Father.prototype.sayHello = function (){
    console.log("Hello my son!!!");
}

var father = new Father();
father.sayHello();

function Son(){
}


util.inherits(Son, Father);

var son = new Son();

son.sayHello();