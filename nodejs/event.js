process.on('uncaughtException',function() {
    console.log('uncaughtException');
});//예외 처리


console.time('event.js');
var util = require('util');

function Person(){}

var Event = require('events').EventEmitter;


util.inherits(Person,Event);

var person = new Person();

person.on('tick',function(){
    console.log('tick');
});

person.emit('tick');

var event = new Event();

event.on('how',function(){
    console.log('i am good');
});

event.once('how2',function(){
    console.log('i am good2');
});

event.emit('how');
event.emit('how');
event.emit('how');

event.emit('how2');
event.emit('how2');
event.emit('how2');

sayError();

console.timeEnd('event.js');

process.on('exit',function(code){
    console.log('exit('+code+')')
});