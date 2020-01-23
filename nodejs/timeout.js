//setTimeout, setInterval

function sayHello(who) {
    let name = "";
    if(who)
    {
        name = who;
    }
    console.log('Hello World '+ name);
}

// 2초 이후 핼로
setTimeout(function() {
    sayHello();
}, 1000);

setInterval(sayHello, 2000, 'leegunj');

