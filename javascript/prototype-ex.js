var johnDoe = {
	firstName: "John",
	lastName: "Doe",
	sayName: function(){
		return "My name is " + firstName + " " + lastName;
	}
}

var janeDoe = Object.create(johnDoe, {
	firstName: {value: "Jane"},
	greet: {
		value: function(person){
			return "Hello.. " + person.firstName; 
		}
	}
});

var jaySmith = Object.create(janeDoe, {
	firstName: {value: "Jay"},
	lastName: {value: "Smith"}
});

console.log(johnDoe.sayName());
console.log(janeDoe.sayName() + "  " + janeDoe.greet(johnDoe));
console.log(jaySmith.sayName() + "  " + jaySmith.greet(janeDoe));