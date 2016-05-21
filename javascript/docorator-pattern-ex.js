function Beverage(){
	this._cost = 5;
}

Beverage.prototype.cost = function(){
	return this._cost;
}

function BeverageDecorator(beverage){
	Beverage.call(this);
	this.beverage = beverage;
}

BeverageDecorator.prototype = Object.create(Beverage.prototype);
BeverageDecorator.prototype.cost = function(){
	return this._cost + this.beverage.cost();
};

function Small(beverage){
		BeverageDecorator.call(this, beverage);
		this._cost = -1;
}

Small.prototype = Object.create(BeverageDecorator.prototype);

function Sugar(beverage){
		BeverageDecorator.call(this, beverage);
		this._cost = 0.15;
}

Sugar.prototype = Object.create(BeverageDecorator.prototype);


function Coffee(){
	Beverage.call(this);
	this._cost = 5;
}

Coffee.prototype = Object.create(Beverage.prototype);

var coffee = new Coffee();
console.log(coffee.cost());
console.dir(BeverageDecorator);
coffee = new Small(coffee);
console.log(coffee.cost());
coffee = new Sugar(coffee);
console.log(coffee.cost());