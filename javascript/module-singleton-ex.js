var dom = (function(dependencies){
	var _counter = 0;
	var instance;

	function generateID(){
		return "customId" + _counter++;
	};

	function create(tagname, id){
		var el = document.createElement(tagname);

		el.id = id || generateID();
		return el;
	};

	function createInstance(){
	    return {
            generateID: generateID,
		    create: create
	    }
	};

	return {
        getInstance: function(){
            return instance || (instance = createInstance())
        }
	}

}("can also pass dependency items"));


var obj1 = dom.getInstance();
var ele1 = obj1.create("div");
console.log(ele1.id);

var obj2 = dom.getInstance("div");
var ele2 = obj2.create("div");
console.log(ele2.id);

console.log(obj1 === obj2)