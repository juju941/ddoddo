// discode.js 모듈 불러오기
const Discord = require('discord.js');

// 디스코드 사용자(client) 생성
const client = new Discord.Client();

// client가 준비되면, 실행되는 코드
// client.once, client가 준비되면 딱 한 번 실행되는 코드
client.once('ready', () => {
	console.log('준비완료');
});

// 디스코드 앱 설정에서 확인한 토큰
client.login('NzkzMDc3NzY0NzA5NDE3MDEx.GE0ckE.2a1aXMthCNcCgxgFL8q2NBC5OnxUQEOFMzRnSY');
