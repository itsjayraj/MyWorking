var express = require("express");
var app = express();
 
app.get("/foo", function(req, resp){
    //response(resp);
	setTimeout(function(){
				var resStr;
				for(var i=0; i<100; i++){
					resStr += "Hello, World!";
				}
				var start = new Date().getTime();
				console.log(start);
				resStr += start.toString();
				resp.set("Content-type", "text/plain");
				resp.end(resStr);
			}, 1000);
});

app.get("/bar", function(req, resp){
    setTimeout(function(){
				var resStr;
				for(var i=0; i<100; i++){
					resStr += "Hello, World!";
				}
				var start = new Date().getTime();
				console.log(start);
				resStr += start.toString();
				resp.set("Content-type", "text/plain");
				resp.end(resStr);
			}, 1000);
});

 
app.listen(3000);