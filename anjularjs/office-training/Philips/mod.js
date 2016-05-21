var mod = (function () {	// IIFE
	var data;

	function getData() {
		console.log('From getData...');
	}
	function saveData() {
		console.log('From saveData...');
	}
	function addData() {
		console.log('From addData...');
	}

	return {
		retrieve: getData,
		save: saveData,
		insert: addData
	};
})();


function module() {
	var data;

	function getData() {
		console.log('From getData...');
	}
	function saveData() {
		console.log('From saveData...');
	}
	function addData() {
		console.log('From addData...');
	}

	return {
		// retrieve: getData,
		save: saveData,
		insert: addData
	};
}
