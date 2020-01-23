console.time('Start');//수행시간 계산

//파일 생성 모듈 생성
var fs = require('fs');
var output = fs.createWriteStream('./log/stdout.log');
var errorOutput = fs.createWriteStream('./log/error.log');

//콘솔 모듈 생성
var Console = require('console').Console;
var logger = new Console(output, errorOutput);

logger.info('info message');
logger.log('log message');
logger.warn('warning');
logger.error('error message');

var sum = 0;
for(var i = 1; i<100000; i++)
{
    sum += i;
}
console.timeEnd('Start');