angular.module('spaMod',['ngRoute'])
// ----------------- CONTROLLERS
.controller('booksCtrl',['$scope','dataService',
		function(scope , service){
	scope.Books = service.Books;
	scope.search = function() {
		service.getBooks(scope.query)
			.success(function(result) {
				scope.Books = result.Books;
				service.Books = result.Books;
			})
			.error(function(err) {
				alert('Search failed: ' + err.statusText);
			});
	};
}])
.controller('detailsCtrl',['$scope','dataService','$routeParams',
		function(scope, service, routeParams){ 
				service.getDetails(routeParams.id).then(  
									function(book) {
										scope.Book = book;
								    }, function(msg) {
								   		alert(msg);
								   	}, function(status) {
								   		console.info(status);
								   	}
								  );
}])
// ----------------- SERVICE
.service('dataService',['$http','$q',function($http, $q) {
	var url = 'http://it-ebooks-api.info/v1/search/';
	var durl = 'http://it-ebooks-api.info/v1/book/';
	this.Books = null;
	this.getDetails = function(id) {
		var defer = $q.defer();
		$http.get( durl + id )
			.success(function(result){
				// process book details
				defer.notify('...response received');
				defer.resolve(result);
			})
			.error(function(err) {
				defer.notify('...failure in response');
				defer.reject(err.statusText);
			});
		// defer.notify('...Requested for details');
		return defer.promise;
	};

	this.getBooks = function(query) {
		return $http.get(url + query);
	};
}])
// ----------------- Fatory
.factory('dataFactory',['$http',function($http) { 
	var url = 'http://it-ebooks-api.info/v1/search/';
	var fo = { Books: null};
	fo.getBooks = function(query) {
		return $http.get(url + query);
	};
	return fo;
}])
// ----------------- CONFIG
.config(['$routeProvider',function(routeProvider){
	// configure valid URLs or routes
	routeProvider.when('/', 
			{ templateUrl: 'app/templates/home.html' })
	.when('/books',
			{ templateUrl: 'app/templates/books.html'
				, controller: 'booksCtrl' })
	//http://...../index.html#/book/4564578
	.when('/book/:id',
			{ templateUrl: 'app/templates/book-details.html'
				, controller: 'detailsCtrl' })
	.otherwise( { redirectTo: '/' } );
}]);