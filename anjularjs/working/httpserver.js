var http = require("http");

var server = http.createServer(function(req, res){
	console.log("Cleient request received...");
	res.end("hello worlslls");
});

server.listen(3000, function(){
	console.log("Server started");
});

console.log("servaer started no event loop");