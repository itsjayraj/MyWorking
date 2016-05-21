var dom = (function(dependencies){
	var _counter = 0;

	function generateID(){
		return "customId" + _counter++;
	};

	function create(tagname, id){
		var el = document.createElement(tagname);

		el.id = id || generateID();
		return el;
	};

	return {
		generateID: generateID,
		create: create
	}

}("can also pass dependency items"));


var ele = dom.create("div");
console.log(ele.id);

var ele1 = dom.create("div");
console.log(ele1.id);