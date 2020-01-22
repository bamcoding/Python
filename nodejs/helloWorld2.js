//Node.js REPL 환경은 불편
//helloWorld.js
//127.0.0.1:3000
var localIp = '127.0.0.1';
var port = 3000;

console.log('서버 생성');
console.log(localIp+':'+port);
var http = require('http');//서버를 만들고
http.createServer(function(request,response){
    response.writeHead(200,{'Content-Type':'text/html'});
    response.end('<h1>Hello World!</h1>');
}).listen(port);//포트 3000 설정