// Factory Method Pattern
function Transaction(id, cid, amt, type) {
	var t = new Object();
	t.id = id; t.customer = cid;
	t.amount = amt; t.trantype = type;
	return t;
}

// var t2 = Transaction(12, 4567, 78500, 'D');
// var t3 = Transaction(12, 4567, 78500, 'D');
// var t4 = Transaction(12, 4567, 78500, 'D');

// Constructor Pattern
function BankTransaction(id, cid, amt, type) {
	this.id = id; this.customer = cid;
	this.amount = amt; this.trantype = type;
	this.getLastTran = function() {};
}

function lastTran() {}

// Prototype Pattern
function Employee(id) {
}
Employee.prototype.getId = function() {
	return this.id;
};

function Manager(id, ts) {
	this.id = id;
	this.teamSize = ts;
}

// Configure Manager to derive from Employee
Manager.prototype = new Employee();
Manager.prototype.getTeamSize = function() {
	console.log('Team size ' + this.teamSize);
};

// ---------------- CLOSURES
function GetData(id) {
	console.log('Getting data for ' + id);

	return function () {
		console.log('Result of getdata for ' + id);
		return id;
	}
}