function Beverage(name, temp){
	this.name = name;
	this.temp = temp;
};

console.dir(Beverage);

Beverage.prototype.drink = function() {
	console.log("I am drinking.. " + this.name);
};

console.dir(Beverage);
function Coffee(type){
	Beverage.call(this, "Coffee", "Hot");
	this.type = type;
};

Coffee.prototype = Object.create(Beverage.prototype);
Coffee.prototype.sip = function(){
	console.log("Sipping my " + this.type + " " + this.name);
}

console.dir(Coffee);

var water = new Beverage("Water", "Cold");
var coffee = new Coffee("Hot Choco");

water.drink();
coffee.drink();
coffee.sip();
